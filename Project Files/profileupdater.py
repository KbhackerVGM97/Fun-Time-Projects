#!/usr/bin/python
import cgi, cgitb
import datetime
import os
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()
user = form["user"].value
s=""

s+=form["firstname"].value
s+='\n'
s+=form["lastname"].value
s+='\n'
s+=form["email"].value

f1=open('profiles/'+user+'profileinfo.txt','w')
f1.write(s)
f1.close()

f1 = open('profileupdatedcheck.html', 'r')
f2=f1.read()
f1.close()
page += f2
page = page.replace('*****',user)
print page
