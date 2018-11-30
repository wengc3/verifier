from socketIO_client import SocketIO
from pprint import pprint
import os, sys
import json
from gmpy2 import mpz


def parseResult(dict,phase,title):
    results = list()
    for key, result in dict.items():
        results.append(result.getJSON(key))
    return {'id': phase, 'title': title, 'results': results}

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
from app.VerifyService import VerifyService
from app.verifier.Report import Report
from app.verifier.MultiTest import MultiTest
from app.verifier.ConsoleView import ConsoleView
socketio = SocketIO('localhost',5000)
data_dict = dict()
electionID1="5bc6062b6d19d200125b3fb7"

def connect():
    print('connected')

def updateData(*args):
    data_dict.update(json.loads(args[0]))

def getData(electionID):
    socketio.emit('requestFullSync',{'election':electionID})

verify_svc = VerifyService()
socketio = SocketIO('127.0.0.1',5000)
data_dict = dict()
getData(electionID1)
socketio.once('connect',connect)
socketio.once('SyncBulletinBoard',updateData)
socketio.once('syncElectionAdministrator',updateData)
socketio.wait(seconds=1)


seclevel = data_dict['securityLevel']

if seclevel == 1:
    secparams = secparams_l1
elif seclevel == 2:
    secparams = secparams_l2
else:
    secparams = secparams_l3

report = Report(electionID1,secparams)
console = ConsoleView(0.2)
report.attach(console)
#data_dict['ballots'][2].pop('voterId')
verify_svc.verify(data_dict,report)
result = report.result
pre_election = result[1]['1.1']
election = result[1]['1.2']
pre_dict = parseResult(pre_election,"1.1","pre election results")
dict = parseResult(election,"1.2","election results")
import json
oneway = json.dumps([pre_dict, dict])
print(oneway)
#print(data_dict['securityLevel'])
#print(data_dict['publicKeyShares'][0]['pk_j'])
# print(data_dict['ballots'][0])
# print("_____________________________")
# print(data_dict['ballots'][0]['ballot']['a_bold'])
# print("_____________________________")
# print(str(data_dict['publicKey']))

# a_bold = data_dict['ballots'][0]['ballot']['a_bold']
# a_bold_s = [[a_bold[x][y] for y in range(len(a_bold[0]))] for x in range(len(a_bold))]
# for i,item in enumerate(a_bold):
#     for j,str in enumerate(item):
#         a_bold[i][j]= mpz(str)
# print(a_bold_s)
