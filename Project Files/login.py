#!/usr/bin/python
import cgi, cgitb
import datetime
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
page+='''
<html>
<head>
<title>Welcome</title>
</head>
<body>
'''
def hash(s):
    s = str(s)
    m=1
    ans = 0
    for letter in s:
        ans += (ord(letter) * m)
        m+=1
    return ans

form=cgi.FieldStorage()
user = form['user'].value
if 'user' in form and 'pw' in form:
    f1=open('data/registered.txt','r')
    g1=f1.read().splitlines()
    f1.close()
    ##make dictionary with usernames and passwords
    D1={}
    for a in g1:
        if a:
            L=a.split(":")
            D1[L[0]]=L[1]
    if 'register' in form: #if the user wants to register
        if form['user'].value in D1:
            page+='This username had already been taken.'
           
        else: ##registers user
            f2=open('data/registered.txt','a')
            f2.write(form['user'].value+':'+str(hash(form['pw'].value))+'\n')
            f2.close()
            page+='Congratulations! You are now registered!'
            D1[form['user'].value]=form['pw'].value
            f3=open('data/data.txt','a')
            f3.write(form['user'].value+'\n~\n-\n')

    else: ##If the user wants to log in
        if form['user'].value in D1 and str(hash(form['pw'].value))==D1[form['user'].value]:
            #page+='<h1><center>Welcome!</center></h1>'
            e1=open('homepagetemplate.html','r')
            e2=e1.read()
            e1.close()
            page='Content-type: text/html\n\n'+e2
            page.replace("*****",user)
        else:
            page+='This is not a valid username and password combination.'
else:
    page+='Please enter a username and password.'

page+='</body></html>'
print page

                
