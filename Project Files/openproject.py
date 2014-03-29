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

name = form['projectname'].value

f1 = open('data/'+user+'/'+name+'.txt','r')
f2=f1.read()
f1.close()

L1 = f2.split('*#*')
#L1[0] is name
#L1[1] is due date
#L1[2] is members
#L1[3] is the actual project

f1=open('newprojecttemplate.html', 'r')
f3=f1.read()
f1.close()

f3=f3.replace("Enter Name",L1[0])
f3=f3.replace("member1,member2,member3",L1[2])
f3=f3.replace('value=""','value="'+L1[1]+'"')
f3=f3.replace('getTime(today);','getTime('+L1[1]+');')
f3=f3.replace("Project Goes Here",L1[3])
f3=f3.replace("*****",user)
f3=f3.replace('&&&&&',name)

page+=f3
print page
