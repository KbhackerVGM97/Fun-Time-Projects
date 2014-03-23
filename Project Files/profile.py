#!/usr/bin/python
import cgi, cgitb
import datetime
import os
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()
user = form["username"].value

f3 = open('profilepagetemplate.html','r')
f1 = f3.read()
f3.close()
f1=f1.replace("*****", user)
if os.path.exists('profiles/'+user+'profileinfo.txt'):
    f4 = open('profiles/'+user+'profileinfo.txt','r')
    f2= f4.read()
    f4.close()
    L = f2.splitlines()
    f1=f1.replace("Enter First Name", f2[0])
    f1=f1.replace("Enter Last Name", f2[1])
    f1=f1.replace("Enter Your E-mail", f2[2])

page += f1
print page
