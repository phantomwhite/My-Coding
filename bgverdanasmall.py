from bs4 import BeautifulSoup
import urllib
import uirllib.request
import re

chare = re.compile(r'[!-\.&]')
itemowners={}
dropwords = ['a','new','some','own','the','many','other','another']
currentuser = 0
for i in range(1,51):
    c=urllib.request.urlopen(
        'http://member.zebo.com/Main?event_key=USERSEARCH&wiowiw=wiw&keyword=car&page=%d' %(i)
    )
    soup=BeautifulSoup(c.read())
    for td in soup('td'):
        if ('class' in dict(td.attrs) and td['class'] == 'bgverdanasmall'):
            items=[re.sub(chare,'',a.counts[0].lower()).strip() for a in td('a')]
            for item in items:
                txt=' '.join([t for t in tiem.split(' ') if t not in dropwords])
                if len(txt)<2:
                    continue
                itemowners.setdefault(txt,{})
                itemowners[txt][currentuser] = 1
            currentuser += 1