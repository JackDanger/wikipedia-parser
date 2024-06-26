# Wikipedia archive parser

Tools to turn the wikipedia archive xml files into usable NLP inputs.

## Usage

```
# Get the wikipedia data dump of your choice from here:
# https://meta.wikimedia.org/wiki/Data_dump_torrents#English_Wikipedia
#
# Then bunzip2 the file into a DOWNLOAD_DIR of your choice until it absolutely
# wrecks your filesystem with an XML file for each article.

python ./textualize.py DOWNLOAD_DIR OUTPUT_DIR
```

This turns XML files into plaintext. You'll get this
```
John Daniel Runkle

name:        John Daniel Runkle
order:       2nd
title:       President of the Massachusetts Institute of Technology
term_start:  1870
term_end:    1879
predecessor: William Barton Rogers
successor:   William Barton Rogers
birth_date:  1822-10-11
birth_place: New York
death_date:  1902-07-08
death_place: Southwest Harbor, Maine
alma_mater:  Lawrence Scientific School of Harvard University, (B.S., 1851)

Biography
Professor Runkle was born at Root, New York State. He worked on his father's farm until he was of age, and then studied and taught until he entered the Lawrence Scientific School of Harvard University, where he graduated in 1851. His ability as a mathematician led in 1849 to his appointment as assistant in the preparation of the American Ephemeris and Nautical Almanac, in which he continued to engage until 1884. He was professor of mathematics in the Massachusetts Institute of Technology from 1865 until his retirement in 1902. Runkle become aware of the work of Victor Della-Vos's work in Russia at the Philadelphia Centennial Exhibition in 1876, he was impressed by the combination of theoretical and practical learning.[2] Manual training was introduced into the institute curriculum largely at his instance. He founded the Mathematical Monthly in 1859 and continued its publication until 1861, and he had charge of the astronomical department of the Illustrated Pilgrim's Almanac.

In the town of Brookline, Massachusetts, Runkle was a chairman of the School Committee and an early advocate of mathematics and technical education. He received an LL.D from Wesleyan University, in Middletown, Connecticut[3]

Works
* New Tables for Determining the Values of Coefficients in the Perturbative Function of Planetary Motion (Washington, 1856)
* The Manual Element in Education (1882), reprinted from the Reports of the Massachusetts Board of Education
* Report on Industrial Education (1883)
* Elements of Plane and Solid Analytic Geometry (Boston, 1888)

Family
His brother, Cornelius A. Runkle (9 December 1832 in Montgomery County, New York–19 March 1888 in New York City) graduated from Harvard Law School in 1855, and began practice in New York City. He was subsequently made deputy collector and given charge of the law division of the New York Custom House. This rendered him familiar with the legal questions involved in tariff and internal revenue litigation, and resulted in his devoting himself largely to that class of business. For about twenty-five years, he acted as counsel for the New York Tribune association. Cornelius's wife, Lucia Isabella Gilbert Runkle (born in North Brookfield, Massachusetts on August 20, 1844), was an editorial writer and contributor to the Tribune.

Notes
 Tyler, Harry W. (1903). "John Daniel Runkle". Proceedings of the American Academy of Arts and Sciences. 38: 26 (26): 727–730. JSTOR 20021835.
 W. H. G. Armytage (1965), The Rise of the Technocrats, London: Routledge and K. Paul, OCLC 562056, OL 5955499M
 "Early Leadership Series". Archived from the original on 2010-04-10.

References
Wilson, J. G.; Fiske, J., eds. (1900). "Runkle, John Daniel" . Appletons' Cyclopædia of American Biography. New York: D. Appleton.
wikisource-logo.svg This article incorporates text from a publication now in the public domain: Gilman, D. C.; Peck, H. T.; Colby, F. M., eds. (1905). "Runkle, John Daniel". New International Encyclopedia (1st ed.). New York: Dodd, Mead.

```

From an article like this:
```
<page>
    <title>John Daniel Runkle</title>
    <ns>0</ns>
    <id>747646</id>
    <revision>
      <id>1185645760</id>
      <parentid>1179662629</parentid>
      <timestamp>2023-11-18T02:51:09Z</timestamp>
      <contributor>
        <username>Uzume</username>
        <id>51070</id>
      </contributor>
      <comment>/* Family */ [[Lucia Runkle</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text bytes="5184" xml:space="preserve">{{Infobox officeholder
| name        = John Daniel Runkle
| image       = JOHN DANIEL RUNKLE (3x4).jpg
| order       = 2nd
| title       = [[President of the Massachusetts Institute of Technology]]
| term_start  = 1870
| term_end    = 1879
| predecessor = [[William Barton Rogers]]
| successor   = William Barton Rogers
| birth_date  = {{birth date|1822|10|11}}
| birth_place = [[Root, New York|Root]], [[New York (state)|New York]]
| death_date  = {{Death date and age|1902|7|8|1822|10|11}}
| death_place = [[Southwest Harbor, Maine|Southwest Harbor]], [[Maine]]
| alma_mater  = [[Lawrence Scientific School]] of [[Harvard University]], (B.S., 1851)
}}
'''John Daniel Runkle''' (October 11, 1822 – July 8, 1902&lt;ref&gt;{{cite journal|last=Tyler|first=Harry W.|date=1903|title=John Daniel Runkle|journal=Proceedings of the American Academy of Arts and Sciences|volume=38: 26|issue=26|pages=727–730|jstor=20021835}}&lt;/ref&gt;) was a [[United States of America|U.S.]] educator and [[mathematician]]. He served as acting president of [[MIT]] from 1868 to 1870 and president between 1870 and 1878.

==Biography==
Professor Runkle was born at [[Root, New York|Root]], [[Montgomery County, New York|New York State]]. He worked on his father's farm until he was of age, and then studied and taught until he entered the [[Lawrence Scientific School]] of [[Harvard University]], where he graduated in 1851. His ability as a mathematician led in 1849 to his appointment as assistant in the preparation of the ''American Ephemeris and Nautical Almanac'', in which he continued to engage until 1884. He was [[professor]] of mathematics in the Massachusetts Institute of Technology from 1865 until his retirement in 1902. Runkle become aware of the work of [[Victor Della-Vos]]'s work in [[Russia]] at the [[Philadelphia Centennial Exhibition]] in 1876, he was impressed by the combination of theoretical and practical learning.&lt;ref&gt;{{Citation
| publisher         = Routledge and K. Paul
| publication-place = London
| title             = The Rise of the Technocrats
| ol=5955499M
| author            = W. H. G. Armytage
| publication-date  = 1965
| oclc              = 562056
}}&lt;/ref&gt;  Manual training was introduced into the institute [[curriculum]] largely at his instance. He founded the ''Mathematical Monthly'' in 1859 and continued its publication until 1861, and he had charge of the astronomical department of the ''Illustrated Pilgrim's Almanac''.

In the town of [[Brookline, Massachusetts]], Runkle was a chairman of the School Committee and an early advocate of mathematics and technical education. He received an [[Legum Doctor|LL.D]] from [[Wesleyan University]], in [[Middletown, Connecticut]]&lt;ref&gt;{{cite web| url = http://atmae.org/foundation/history1.html |url-status=dead |archive-url=https://web.archive.org/web/20100410211314/http://atmae.org/foundation/history1.html |archive-date=2010-04-10 |title=Early Leadership Series}}&lt;/ref&gt;

==Works==
* ''New Tables for Determining the Values of Coefficients in the Perturbative Function of Planetary Motion'' (Washington, 1856)
* ''The Manual Element in Education'' (1882), reprinted from the ''Reports'' of the [[Massachusetts Board of Education]]
* ''Report on Industrial Education'' (1883)
* ''Elements of Plane and Solid Analytic Geometry'' (Boston, 1888)

==Memorials==
[[John D. Runkle School]], an elementary school located at 50 Druce Street in Brookline, was established in his name in 1897.

==Family==
His brother, Cornelius A. Runkle (9 December 1832 in [[Montgomery County, New York]]–19 March 1888 in [[New York City]]) graduated from [[Harvard Law School]] in 1855, and began practice in New York City.  He was subsequently made deputy collector and given charge of the law division of the New York Custom House. This rendered him familiar with the legal questions involved in tariff and internal revenue litigation, and resulted in his devoting himself largely to that class of business. For about twenty-five years, he acted as counsel for the ''[[New York Tribune]]'' association.  Cornelius's wife, [[Lucia Runkle|Lucia Isabella Gilbert Runkle]] (born in [[North Brookfield, Massachusetts]] on August 20, 1844), was an editorial writer and contributor to the ''Tribune''.

==Notes==
{{Reflist}}

==References==
*{{Cite Appletons'|wstitle=Runkle, John Daniel|year=1900}}
* {{NIE|title=Runkle, John Daniel}}

{{s-start}}
{{s-aca}}
{{s-bef|before=[[William Barton Rogers]]}}
{{s-ttl|title=President of the [[Massachusetts Institute of Technology]]|years=1870 – 1879}}
{{s-aft|after=[[William Barton Rogers]]}}
{{s-end}}

{{MIT presidents}}

{{Authority control}}

{{DEFAULTSORT:Runkle, John Daniel}}
[[Category:Presidents of the Massachusetts Institute of Technology]]
[[Category:Massachusetts Institute of Technology School of Science faculty]]
[[Category:American science writers]]
[[Category:People from Montgomery County, New York]]
[[Category:Academics from Brookline, Massachusetts]]
[[Category:Harvard John A. Paulson School of Engineering and Applied Sciences alumni]]
[[Category:Wesleyan University people]]
[[Category:1822 births]]
[[Category:1902 deaths]]
[[Category:School board members in Massachusetts]]</text>
      <sha1>2skq3vujs4066pd7x5xobd29wpcazrx</sha1>
    </revision>
  </page>

```

