import json
import random
import urllib.request

HOST='localhost'
PORT=8069
DB='farid'
USER='faridadwani@insat.u-carthage.tn'
PASSWD='farid'

def json_rpc(url,method,params):
    data={
        "jsonrpc":"2.0",
        "method":method,
        "params":params,
        "id":random.randint(1,47856)
    }
    req=urllib.request.Request(url=url,data=json.dumps(data).encode(), headers={"content-Type":"application/json",})
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        print('la ya baba')
        raise Exception(reply["error"])
    return reply["result"]
def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

    # log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASSWD)
    # create a new note
args = {
        'f_name': 'Farid',
        'l_name':'Adwani',
        'field_1':'field111',
        'classroom_id':'2',

    }
# student_id= call(url, "object", "execute", DB, uid, PASSWD, 'university.student','create', args)
# print(student_id)

student=call(url, "object", "execute", DB, uid, PASSWD, 'university.student','read',[8]);
print(student)

print(call(url, "object", "execute", DB, uid, PASSWD, 'university.student','write',17,args));


