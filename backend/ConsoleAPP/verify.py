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
from app.utils.prepareData import prepareData
from app.VerifyService import VerifyService
from app.verifier.Report import Report
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
from chvote.verifier.TestResult import TestResult
from chvote.verifier.MultiTest import MultiTest
from ConsoleView import ConsoleView
socketio = SocketIO('localhost',5000)
data_dict = dict()
# electionID1="5c228607ed394c0012e2abf9" # multi election second c in beta_j is Null ?
electionID1="5c0bb43740b1e1001273984f"
# electionID1="5c232c1eed394c0012e2ac03" # hacked election

def connect():
    print('connected')

def addEBold(*args):
    json_data = json.loads(args[0])
    data_dict.update({'e_bold': json_data[0]['encryptions']})

def updateData(*args):
    data_dict.update(json.loads(args[0]))

def getData(electionID):
    socketio.emit('requestFullSync',{'election':electionID})

verify_svc_1 = VerifyService.getInstance()
socketio = SocketIO('127.0.0.1',5000)
data_dict = dict()
getData(electionID1)
socketio.on('SyncBulletinBoard',updateData)
socketio.on('syncElectionAdministrator',updateData)
socketio.on('syncElectionAuthorities',addEBold)
socketio.wait(seconds=2)


seclevel = data_dict['securityLevel']

if seclevel == 1:
    secparams = secparams_l1
elif seclevel == 2:
    secparams = secparams_l2
else:
    secparams = secparams_l3

report = Report(electionID1)
console = ConsoleView(step=0.2,depth = 0)
report.attach(console)
verify_svc_1.verify(data_dict,report,secparams)

# getData(electionID1)
# socketio.wait(seconds=1)
# verify_svc_2 = VerifyService.getInstance()
# report = Report(electionID1)
# console = ConsoleView(step=0.2,depth = 1)
# report.attach(console)
# verify_svc_2.verify(data_dict,report,secparams)

# data_dict['ballots'][2].pop('voterId')
# result = report.result
# pre_election = result[1]['1.1']
# election = result[1]['1.2']
# pre_dict = parseResult(pre_election,"1.1","pre election results")
# dict = parseResult(election,"1.2","election results")
# import json
# oneway = json.dumps([pre_dict, dict])
# print(oneway)
# print(data_dict['securityLevel'])
# print(data_dict['publicKeyShares'][0])

# data_dict = prepareData(data_dict,secparams)
# temp_dic = {'responses': data_dict['responses'],'s': data_dict['s']}
# print(data_dict['w_bold'])
# print("_____________________________")
# print(data_dict['responses'][0]['beta_j'])
# print("_____________________________")
# print(data_dict['partialPublicVotingCredentials'][0]['d_hat_i'][0])
# print("_____________________________")
# print(data_dict['confirmations'][0]['confirmation'])
# print(str(data_dict['publicKey']))
# print(len(data_dict['shuffleProofs'][0]))
# print(len(data_dict['n'])
# print("_____________________________")

# a_bold = data_dict['ballots'][0]['ballot']['a_bold']
# a_bold_s = [[a_bold[x][y] for y in range(len(a_bold[0]))] for x in range(len(a_bold))]
# for i,item in enumerate(a_bold):
#     for j,str in enumerate(item):
#         a_bold[i][j]= mpz(str)
# print(a_bold_s)
