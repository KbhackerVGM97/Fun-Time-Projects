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

f1=open('homepagetemplate.html','r')
f2=f1.read()
f1.close()

page+=f2
page = page.replace('*****',user)
print page
