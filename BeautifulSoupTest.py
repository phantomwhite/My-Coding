# encoding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request

#from imp import reload
from importlib import reload
import sys,locale

# they just for python 2
# reload(sys)
# sys.setdefaultencoding('utf8')
# http://stackoverflow.com/questions/28127513/attributeerror-module-object-has-no-attribute-setdefaultencoding

print(sys.stdout.encoding)
print(locale.getpreferredencoding())

c = urllib.request.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/')
soup = BeautifulSoup(c.read())

links = soup('a')

for link in links:
    print(link)


