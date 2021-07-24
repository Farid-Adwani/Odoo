import xmlrpc.client
HOST='localhost'
PORT=8069
DB='farid'
USER='faridadwani@insat.u-carthage.tn'
PASS='farid'
root = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

uid=xmlrpc.client.ServerProxy(root + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid: %d)" % (USER, uid))

# Create a new note
sock = xmlrpc.client.ServerProxy(root + 'object')
args = {
    'f_name': 'mta3 xml',
        'l_name':'Adwani',
        'field_1':'field111xml',
        'classroom_id':'1',
}
note_id = sock.execute(DB, uid, PASS, 'university.student', 'write',20, args)
