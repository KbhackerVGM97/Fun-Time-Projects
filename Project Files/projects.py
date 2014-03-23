#!/usr/bin/python
import cgi, cgitb
import datetime
import os
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()
user = form["username"].value

if os.path.exists('data/'+user+'/projectdata.txt'):
    #a file with the names ofall projects
    f1= open 'data/'+user+'/projectdata.txt'
    f2=f1.read()
    f1.close()
    L2=[]
    L1=f2.splitlines()
    for i in L1:
        #a file for each project with its atributes
        if os.path.exists('data/'+user+'/'+i):
            f1=open('data/'+user+'/'+i)
            L2+= f1.read()
            f1.close()
        else:
            L2+="***the project had no file***"
    #L2 now contains all the project atribute files
    
    
