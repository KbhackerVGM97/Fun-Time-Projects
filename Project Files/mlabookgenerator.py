#!/usr/bin/python
import cgi, cgitb
import datetime
import os
import sys
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()

user = form["username"].value
project=form['projectname'].value

firstname = form['firstname'].value
lastname=form['lastname'].value
title=form['title'].value
city=form['city'].value
publisher=form['publisher'].value
year = form['year'].value
medium=form['medium'].value

citation=''
citation += lastname+', '+firstname+'. '+title+'. '+city+': '+publisher+', '+year+', '+medium+'.'

f2=''
if os.path.exists('data/'+user+'/'+project+'citation.txt'):
    f1=open('data/'+user+'/'+project+'citation.txt','r')
    f2=f1.read()+'\n'
    f1.close()

f2+=citation
f1=open('data/'+user+'/'+project+'citation.txt','w')
f1.write(f2)
f1.close()

f1=open('citationadded.html','r')
f2=f1.read()
f1.close()

f2=f2.replace('*****',user)
page+= f2
print page
