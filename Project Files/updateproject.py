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


newmembers = form['members'].value+','+user
newmemberslist = newmembers.split(',')

newduedate = form['duedate'].value
newprojectdata = form['project'].value

project = name + '*#*' + newduedate + '*#*' + newmembers
projectinfo = project + '*#*' + newprojectdata

for i in newmemberslist:
    f2=""
    ##update projectdata.txt
    f1 = open('data/'+i+'/projectdata.txt','r')
    f2=f1.read()
    f1.close()
    projects = f2.split('\n')
    L = []
    #L[0] = name
    #L[1] = duedate
    newmember=true
    for p in projects:
        L = p.split('*#*')
        if L[0]==name:
            newmember=false
            p = project
            f1 = open('data/'+user+'/projectdata.txt','w')
            f1.write(projects.join('\n')+'\n')
            f1.close()
    if newmember:
        f1=open('data/'+user+'/projectdata.txt','a')
        f1.write(project+'\n')
        f1.close()

    ##rewrite project file
    f1 = open('data/'+i+'/'+name+'.txt','w')
    f1.write(projectinfo+'/n')
    f1.close()

f1 = open('madeprojecttemplate.html','r')
f2=f1.read()
f1.close()
f2 = f2.replace('*****',user)

page += f2
print page
        
