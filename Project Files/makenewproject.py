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
#memberslist=[]
#members=user
#try:
members = form['members'].value+','+user
memberslist = members.split(',')
#except:
 #S   pass

duedate = form['duedate'].value
projectdata = form['project'].value

project = name + '*#*' + duedate + '*#*' + members
projectinfo = project + '*#*' + projectdata

for i in memberslist:
    f2=""
    if os.path.exists('data/'+i+'/projectdata.txt'):
        #update projectdata.txt
        f1 = open('data/'+i+'/projectdata.txt','r')
        f2=f1.read()
        f1.close()
        projects = f2.split('\n')
    else:
        projects=""
    if not (project in projects):
        f2+=project+'\n'    
        ##doesn't seem to work
        ##f1 = open('data/'+i+'/projectdata.txt','w')
        ##f1.write(f2)
        f1 = open('data/'+i+'/projectdata.txt','a')
        f1.write(project+'\n')
        f1.close()
        #writes the project file
        f1 = open('data/'+i+'/'+name+'.txt','w')
        f1.write(projectinfo+'\n')
        f1.close()
f1 = open('madeprojecttemplate.html','r')
f2=f1.read()
f1.close()
f2 = f2.replace('*****',user)

page += f2
print page


