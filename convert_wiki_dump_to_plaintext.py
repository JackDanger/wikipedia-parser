import sys
import os
import xml.sax
import xml
import bz2
import tqdm
import textualize

class WikiReader(xml.sax.ContentHandler):
    """
    This streaming XML parser cribbed straight from James Thorne at
    https://jamesthorne.com/blog/processing-wikipedia-in-a-couple-of-hours/
    """
    def __init__(self, ns_filter, callback):
        super().__init__()

        self.filter = ns_filter
        
        self.read_stack = []
        self.read_text = None
        self.read_title = None
        self.read_namespace = None
        
        self.status_count = 0
        self.callback = callback


    def startElement(self, tag_name, attributes):
        if tag_name == "ns":
            self.read_namespace = None
            
        elif tag_name == "page":
            self.read_text = None
            self.read_title = None
            
        elif tag_name == "title":
            self.read_title = ""
            
        elif tag_name == "text":
            self.read_text = ""
            
        else:
            return

        self.read_stack.append(tag_name)


    def endElement(self, tag_name):
        if len(self.read_stack) and tag_name == self.read_stack[-1]:
            del self.read_stack[-1]

        if self.filter(self.read_namespace):
            if tag_name == "page" and self.read_text is not None:
                self.status_count += 1
                self.callback(self.read_title, self.read_text)
                

    def characters(self, content):
        if len(self.read_stack) == 0:
            return

        if self.read_stack[-1] == "text":
            self.read_text += content

        if self.read_stack[-1] == "title":
            self.read_title += content

        if self.read_stack[-1] == "ns":
            self.read_namespace = int(content)
  

def process(src, dst):
    with open(src, 'rb') as f:
        with open(dst, 'wb') as g:

            bzip_reader = bz2.BZ2File(f, 'rb')
            bzip_writer = bz2.BZ2File(g, 'wb')
            
            with tqdm.tqdm(total=os.path.getsize(src), unit='M', unit_scale=True) as pbar:

                def write(title, text):
                    plain = textualize.wikitext_to_plain(title, text)
                    written = bzip_writer.write(plain.encode('utf-8'))
                    pbar.update(written)

                parser = xml.sax.make_parser()
                parser.setContentHandler(WikiReader(lambda ns: ns == 0, write))

                for chunk in bzip_reader:
                    parser.feed(chunk)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <archive.bz2> <output.txt.gz>")
        sys.exit(1)
    

    src = sys.argv[1]
    dst = sys.argv[2]

    if not src.endswith('.bz2'):
        print("Error: input file should be a bz2 archive")
        sys.exit(1)
    
    if not os.path.dirname(dst):
        os.makedirs(dst)

    process(src, dst)

