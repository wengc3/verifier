from socketIO_client import SocketIO
from pprint import pprint
import os, sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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


report = Report(electionID1,printResult)
verify_svc.verify(data_dict,report)
