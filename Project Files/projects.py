#!/usr/bin/python
import cgi, cgitb
import datetime
import os
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()
user = form["username"].value
f1=open('projectspagetemplate.html','r')
pages+=f1.read()
f1.close()
#pages is a complete template where only the tables will need to be replaced

if os.path.exists('data/'+user+'/projectdata.txt'):#if the path exists
    #a file with the names of all projects
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
    
    
