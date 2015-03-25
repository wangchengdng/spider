import urllib
import re
num=0
for i in range(2,214):
    url='http://sc.chinaz.com/tubiao/index_'+bytes(i)+'.html'
    html=urllib.urlopen(url)
    try:
        htmltext=html.read()
        imgurls=re.findall('http://pic1.sc.chinaz.com/Files/pic/.*\.jpg',htmltext)
        for imgurl in imgurls:
            img=urllib.urlopen(imgurl)
            f=open('H:\\pic\\'+bytes(num)+'.jpg','wb')
            f.write(img.read())
            f.close()
            num=num+1
    finally:
        html.close()
