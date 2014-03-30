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
project = form['projectname'].value
f1=open('data/'+user+'/'+project+'citation.txt','r')
citation=f1.read()
f1.close()

f4 = open("showcitation.html",'r')
f2=f4.read()
f4.close()
f2=f2.replace('%%%%%',citation)
page+= f2
print page
