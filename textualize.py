import bs4 as bs
import mwparserfromhell
import sys

"""
This module contains functions for converting Wikipedia articles from XML to
plain text.

You can call it directly to test it out before running on a whole archive
"""

def plain(article):

    title, text = xml_to_wikitext(article)
    return wikitext_to_plain(title, text)

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

    parsed_wikicode = mwparserfromhell.parse(article)

    return parsed_wikicode.strip_code() + "\n\n"

if __name__  == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if filename is not None:
            with open(filename, 'r') as f:
                print(plain(f.read()))
    else:
        print(plain(sys.stdin.read()))
            


