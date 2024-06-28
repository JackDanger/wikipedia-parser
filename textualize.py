import bs4 as bs
import mwparserfromhell
import re
import sys

"""
This module contains functions for converting Wikipedia articles from XML to
plain text.

You can call it directly to test it out before running on a whole archive
"""

def plain(article):
    title, text = xml_to_wikitext(article)
    article = wikitext_to_plain(title, text)
    article = replace_multibyte_spaces(article)
    article = replace_common_multibyte_chars(article)
    article = remove_unprintable(article)
    return article

def xml_to_wikitext(article):
    xml = bs.BeautifulSoup(article, "lxml")

    title = xml.find('title').text
    text = xml.find('text').text
    return title, text

def wikitext_to_plain(title, text):
    # Handle redirects with the copula
    if text[0:9] == '#REDIRECT':
        target = text[10:]
        article = f"{title} is {target}"
    else:
        article = f"{title}\n\n{text}"

    article = replace_multibyte(article)

    parsed_wikicode = mwparserfromhell.parse(article)

    return parsed_wikicode.strip_code() + "\n\n"

def replace_common_multibyte_chars(article):
    for multibyte, ascii in multibyte_to_ascii.items():
        article = article.replace(multibyte, ascii)
    return article


# Define a mapping of multibyte spaces and invisible characters to a single space or empty string
multibyte_spaces = [
    '\u00A0', '\u202F', '\u2060', '\u2000', '\u2001', '\u2002', '\u2003', 
    '\u2004', '\u2005', '\u2006', '\u2007', '\u2008', '\u2009', '\u200A', 
    '\u200B', '\uFEFF', '\u200C', '\u200D', '\u3000', '\u205F', '\u180E', 
    '\u200E', '\u200F', '\u2028', '\u2029'
]

# Create a regular expression pattern to match any of these characters
pattern = re.compile('|'.join(re.escape(space) for space in multibyte_spaces))

# Function to replace multibyte spaces with a single space or remove them
def replace_multibyte_spaces(text, replace_with=' '):
    return pattern.sub(replace_with, text)

def remove_unprintable(article):
    return ''.join([c for c in article if ord(c) < 128])


multibyte_to_ascii = {
    '—': '-',    # em dash
    '–': '-',    # en dash
    '‒': '-',    # figure dash
    '―': '-',    # horizontal bar
    '‐': '-',    # hyphen
    '‑': '-',    # non-breaking hyphen
    '⁃': '-',    # hyphen bullet

    '‘': "'",    # left single quotation mark
    '’': "'",    # right single quotation mark
    '‚': "'",    # single low-9 quotation mark
    '‛': "'",    # single high-reversed-9 quotation mark

    '“': '"',    # left double quotation mark
    '”': '"',    # right double quotation mark
    '„': '"',    # double low-9 quotation mark
    '‟': '"',    # double high-reversed-9 quotation mark

    '…': '...',  # ellipsis

    '‖': '||',   # double vertical line
    '¦': '|',    # broken bar
    '‗': '_',    # double low line

    '€': 'EUR',  # euro sign
    '£': 'GBP',  # pound sign
    '¥': 'JPY',  # yen sign
    '₩': 'KRW',  # won sign
    '₽': 'RUB',  # ruble sign
    '₹': 'INR',  # rupee sign
    '$': 'USD',  # dollar sign (no change but listed for completeness)

    '©': '(c)',  # copyright sign
    '®': '(r)',  # registered sign
    '™': '(tm)', # trademark sign

    '°': 'deg',  # degree sign
    '′': "'",    # prime
    '″': '"',    # double prime

    '±': '+-',   # plus-minus sign
    '×': 'x',    # multiplication sign
    '÷': '/',    # division sign

    'ƒ': 'f',    # florin sign
    'µ': 'u',    # micro sign
    '·': '.',    # middle dot
    '•': '*',    # bullet
    '⁂': '***',  # asterism
    '‰': '%',    # per mille sign

    '¤': '$',    # currency sign
    '₡': 'CRC',  # colón sign
    '₤': 'ITL',  # lira sign
    '₫': 'VND',  # dong sign
    '₪': 'ILS',  # new shekel sign
    '₦': 'NGN',  # naira sign
    '₨': 'INR',  # rupee sign
    '₴': 'UAH',  # hryvnia sign
    '₮': 'MNT',  # tugrik sign
    '₯': 'GRD',  # drachma sign
    '₲': 'PYG',  # guarani sign
    '₵': 'GHS',  # cedi sign
    '₸': 'KZT',  # tenge sign
    '₺': 'TRY',  # turkish lira sign
    '₽': 'RUB',  # ruble sign
    '₾': 'GEL',  # lari sign
    '₿': 'BTC',  # bitcoin sign

    '©': '(c)',  # copyright sign
    '®': '(r)',  # registered trademark sign
    '™': '(tm)', # trademark sign

    '←': '<-',   # leftwards arrow
    '↑': '^',    # upwards arrow
    '→': '->',   # rightwards arrow
    '↓': 'v',    # downwards arrow
    '↔': '<->',  # left right arrow
    '↕': '^v',   # up down arrow

    '⇐': '<=',   # leftwards double arrow
    '⇒': '=>',   # rightwards double arrow
    '⇔': '<=>',  # left right double arrow

    '∀': 'for all', # for all
    '∃': 'there exists', # there exists
    '∅': 'empty set',   # empty set
    '∞': 'infinity',    # infinity
    '∧': 'and',         # logical and
    '∨': 'or',          # logical or
    '∩': 'intersection',# intersection
    '∪': 'union',       # union

    'α': 'alpha',  # alpha
    'β': 'beta',   # beta
    'γ': 'gamma',  # gamma
    'δ': 'delta',  # delta
    'ε': 'epsilon',# epsilon
    'ζ': 'zeta',   # zeta
    'η': 'eta',    # eta
    'θ': 'theta',  # theta
    'ι': 'iota',   # iota
    'κ': 'kappa',  # kappa
    'λ': 'lambda', # lambda
    'μ': 'mu',     # mu
    'ν': 'nu',     # nu
    'ξ': 'xi',     # xi
    'ο': 'omicron',# omicron
    'π': 'pi',     # pi
    'ρ': 'rho',    # rho
    'σ': 'sigma',  # sigma
    'τ': 'tau',    # tau
    'υ': 'upsilon',# upsilon
    'φ': 'phi',    # phi
    'χ': 'chi',    # chi
    'ψ': 'psi',    # psi
    'ω': 'omega',  # omega

    'Æ': 'AE',    # AE
    'Ø': 'O',     # O slash
    'Å': 'A',     # A ring
    'æ': 'ae',    # ae
    'ø': 'o',     # o slash
    'å': 'a',     # a ring

    'Ç': 'C',    # C cedilla
    'É': 'E',    # E acute
    'Ñ': 'N',    # N tilde
    'Ü': 'U',    # U umlaut
    'á': 'a',    # a acute
    'é': 'e',    # e acute
    'í': 'i',    # i acute
    'ñ': 'n',    # n tilde
    'ó': 'o',    # o acute
    'ú': 'u',    # u acute
    'ü': 'u',    # u umlaut
}


if __name__  == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if filename is not None:
            with open(filename, 'r') as f:
                print(plain(f.read()))
    else:
        print(plain(sys.stdin.read()))
            