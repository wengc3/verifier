import json
from socketIO_client import SocketIO, BaseNamespace

data_dict = dict()

def addEBold(*args):
    json_data = json.loads(args[0])
    data_dict.update({'e_bold': json_data[0]['encryptions']})

def updateData(*args):
    data_dict.update(json.loads(args[0]))


def init_socket(host, port, electionID):
        socketio = SocketIO(host, port)
        socketio.on('SyncBulletinBoard',updateData)
        socketio.on('syncElectionAdministrator',updateData)
        socketio.on('syncElectionAuthorities',addEBold)
        socketio.emit('requestFullSync',{'election':electionID})
        socketio.wait(seconds=2)

def getData():
    return data_dict
