#! /usr/bin/python
TheContentHeader = 'Content-type: text/html'
TheHTMLHeader = '<html><head>'
TheBeginningOfBody = '</head><body>'
TheHTMLFooter = '</body></html>'

import time
import random

print TheContentHeader
Sayings=open('Sayings.txt','r')
Sayings=Sayings.read()
Sayings=Sayings.split('\n')
Sayings.remove(Sayings[-1])
Insults=open('Insults.txt','r')
Insults=Insults.read()
Insults=Insults.split('\n')
Insults.remove(Insults[-1])
html=open('K.html','r')
html=html.read()
colors=['aqua', 'burlywood', 'coral', 'lime', 'firebrick', 'goldenrod', 'olivedrab', 'red']
text1=random.randint(0,len(colors)-1)
text2=random.randint(0,len(colors)-1)
text3=random.randint(0,len(colors)-1)
text4=random.randint(0,len(colors)-1)
text5=random.randint(0,len(colors)-1)
text6=random.randint(0,len(colors)-1)
html=html.replace("text1",colors[text1])
html=html.replace("text2",colors[text2])
html=html.replace("text3",colors[text3])
html=html.replace("text4",colors[text4])
html=html.replace("text5",colors[text5])
html=html.replace("text6",colors[text6])
date=time.asctime()
html=html.replace('???',date[11:19])
html=html.replace('!!!',date[0:9]+', '+date[-1:-4])
Saying=random.randint(0, len(Sayings)-1)
Insult=random.randint(0, len(Insults)-1)
html=html.replace('$$$', Sayings[Saying])
html=html.replace('###', Insults[Insult])
print html
