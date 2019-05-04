from ldap3 import Server,Connection,ALL, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES

host = "my_host"
user_dn = "my_user@domain"
user_pass = "my_password"

server = Server(host=host, get_info=ALL)
conn = Connection(
	server = server,
	user = user_dn,
	password = user_pass,
	auto_bind=True,
	raise_exceptions = False

)
conn.search(
	'dc=union,dc=local',
	'(objectclass=*)',
	attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])

print()
