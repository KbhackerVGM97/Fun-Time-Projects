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

name = form['name'].value
members = form['members'].value
memberslist = members.split(',')
duedate = form['duedate'].value
projectdata = form['project'].value

project = name + '*#*' + duedate + '*#*' + members

projectinfo = project + '*#*' + projectdata
#update projectdata.txt
f1 = open('data/'+user+'/projectdata.txt','r')
f2=f1.read()
f1.close()

projects = f2.split('\n')
if not (project in projects):
    f2+=project+'\n'    
    f1 = open('data/'+user+'/projectdata.txt','w')
    f1.write(f2)
    f1.close()
    #writes the project file
    f1 = open('data/'+user+'/'+name+'.txt','w')
    f1.write(projectinfo)
    f1.close()

f1 = open('madeprojecttemplate.html','r')
f2=f1.read()
f1.close()
f2 = f2.replace('*****',user)
page += f2
print page


