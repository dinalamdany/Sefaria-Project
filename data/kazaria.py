from BeautifulSoup import BeautifulSoup
import urllib2
import re

def fetchSource(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(url)
    source = page.read()
    return source

def soup(source):
    soup = BeautifulSoup(source)
    texts = soup.findAll(text=True)
    visible_texts = filter(visible,texts)
#    line = ""
#   text = ""
#    for x in visible_texts:
#        if re.match('\d+.', str(x)):
#            parts = re.split('(\d+.)', str(x))
#            parsed = {
#                "language": "en",
#                "versionTitle": "Wikisource Khazari",
#                "versionUrl": "http://en.wikisource.org/wiki/Kuzari",
#                "line": line,
#                "text": text
#                }
#            line = parts[1]
#            text = parts[2]
#            print parsed
#        else:
#            text += str(x) 
#    parsed = {
#        "language": "en",
#        "versionTitle": "Wikisource Khazari",
#        "versionUrl": "http://en.wikisource.org/wiki/Kuzari",
#        "line": line,
#        "text": text
#        }
#    print parsed
    return visible_texts
    
def visible(element):
    if element.parent.name in ['style','a', 'script', '[document]', 'head', 'title', 'li', 'b', 'h5', 'span', 'td', 'i', 'alt']:
        return False
    elif re.match('.*<!--.*-->.*', str(element), re.DOTALL):
        return False
    elif re.search('\n', str(element)):
        return False
    elif re.match(' ', str(element)):
        return False
    elif re.search('\t', str(element)):
        return False
    return True

if __name__ == '__main__':
    try:
        print soup(fetchSource("http://en.wikisource.org/wiki/Kitab_al_Khazari/Part_One"))
    except urllib2.HTTPError, e:
        print e

