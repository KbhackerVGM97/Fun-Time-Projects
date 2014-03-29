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

f1=open('citations/citation.html','r,')
f2=f1.read()
f1.close()
f2=f2.replace('*****',user)

page+=f2
print page
