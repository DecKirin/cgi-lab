#!/usr/bin/env python3
import cgi, cgitb
import os,json
from templates import login_page
from secret import username,password

print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World</p>")

'''
#Question 1:
enviro_variable = os.environ
json_target = json.dumps(dict(enviro_variable),indent = 4)
print("json_target is ", json_target)

#Question 2:
for param in os.environ.keys():
	if(param == "QUERY_STRING"):
		#print(f"<em>{param}</em> = {os.environ[parm]}</li>")
		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

#Question 3:
for param in os.environ.keys():
	if(param == "HTTP_USER_AGENT"):
		print("<b>%20s</b>: %s<br>"% (param, os.environ[param]))
'''

#Question 4:
get_field = cgi.FieldStorage()
field_uname,field_pword = get_field.getvalue("username"), get_field.getvalue("password")

#Question 5:
if (field_uname,field_pword) == (username,password):
    print("Set-Cookie:UserID = " + username)
    print("Set-Cookie:Password = " + password)
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<title>SET COOCKIE</title>')
    print('</head>')
    print('<body>')
    print('<b>COOCKIE IS SET!</b>')
    print('</body>')
    print('</html>')
