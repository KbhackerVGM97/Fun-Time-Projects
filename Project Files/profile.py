#!/usr/bin/python
import cgi, cgitb
import datetime
#from datetime import *
cgitb.enable()

page='Content-type: text/html\n\n'
form=cgi.FieldStorage()
user = form[username].value

