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
f1=open('projectspagetemplate.html','r')
pages=f1.read()
f1.close()
#pages is a complete template where only the tables will need to be replaced
splitpages = pages.split('<div id="insert"></div>')
prelist = splitpages[0]
page+=prelist
postlist = splitpages[1]

if os.path.exists('data/'+user+'/projectdata.txt'):#if the path exists
    #a file with the names of all projects
    f1= open ('data/'+user+'/projectdata.txt','r')
    f2=f1.read()
    f1.close()
    L2=[]
    L1=f2.splitlines()
##    for i in L1:
##        #a file for each project with its atributes
##        if os.path.exists('data/'+user+'/'+i):
##            f1=open('data/'+user+'/'+i,'r')
##            L2+= f1.read()
##            f1.close()
##        else:
##            L2+="***the project had no file***"
    for i in L1:
        #L1[i] is the ith project for that user
        L2=L1[i].split(':')
        #L2[0] is name
        #L2[1] is due date
        #L2[2] is members
        page+='<tr><td>'+L2[0]+'</td>'
        page+='<td>'+L2[1]+'</td>'
        page+='<td>'+L2[2]+'</td></tr>'
else:
    if not os.path.exists('data/'+user):
        os.mkdir('data/'+user,0777);
    f1 = open ('data/' + user + '/projectdata.txt','w')
    os.chmod('data/'+user+'/projectdata.txt',0777)
    f1.close()

    
page+=postlist
print page
    
    
