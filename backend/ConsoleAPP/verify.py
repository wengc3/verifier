from socketIO_client import SocketIO
from pprint import pprint
import os, sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
from app.VerifyService import VerifyService
from app.verifier.Report import Report
from app.verifier.MultiTest import MultiTest
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
socketio.on('connect',connect)
socketio.on('SyncBulletinBoard',updateData)
socketio.on('syncElectionAdministrator',updateData)
socketio.wait(seconds=1)

def printResult(res):
    test = res[0]
    if not isinstance(test,MultiTest):
        print(test.getId(),test.getTitle(),":", res[1])
    else:
        print(test.getId(),test.getTitle(),":", res[1],"are correct")

seclevel = data_dict['securityLevel']

if seclevel == 1:
    secparams = secparams_l1
elif seclevel == 2:
    secparams = secparams_l2
else:
    secparams = secparams_l3

#report = Report(electionID1,printResult,secparams)
#data_dict['ballots'][2].pop('voterId')
#verify_svc.verify(data_dict,report)
#pprint(report.getResult())
#print(data_dict['securityLevel'])
#print(data_dict['publicKeyShares'][0]['pk_j'])
