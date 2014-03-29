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
project=form["projectname"].value

citationtype=form['style'].value
citationtype+=form['type'].value

f1=open(citationtype+'.html','r')
f2=f1.read()
f1.close()

page+=f2
page=page.replace("*****",user)
page=page.replace("&&&&&",project)
print page
