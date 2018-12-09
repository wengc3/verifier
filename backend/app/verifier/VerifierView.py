from chvote.verifier.Observer import Observer
from app.api.syncService import emitToClient, SyncType

class VerifierView(Observer):
    """docstring for VerifierView."""

    def update(self,state):
        id = self.result.test.id
        if  id not in ['0','no id'] and id.count('.') <= self.depth :
            try:
                func = self._functions[state]
                func(self)
            except KeyError:
                raise AttributeError('this function is not defined:'+state)

        if state == 'reportCreated':
            self._reportCreated()


    def _testRunning(self):
        test = self.result.test
        emitToClient('testRunning',test.title,SyncType.ROOM,self.report.electionID)
        if test.id.count('.') == 0:
            emitToClient('newState','{'id': id,'value': 'running'}',SyncType.ROOM,self.report.electionID)

    def _newProgress(self):
        id = self.result.test.id
        if id.count('.') == 0:
            prg = self.result.progress
            if prg == 1:
                emitToClient('newState',{'id': id,'value': 'completed'},SyncType.ROOM,self.report.electionID)
            newprg = int(20*prg) + ((int(id) - 1)*20)
            emitToClient('newProgress',str(newprg),SyncType.ROOM,self.report.electionID)


    def _newResult(self):
        result = self.result
        if result.test_result == 'failed':
            id = result.test.id[0]
            emitToClient('resultFailed',id,SyncType.ROOM,self.report.electionID)

    def _reportCreated(self):
        emitToClient('allResults',self.report.final_result,SyncType.ROOM,self.report.electionID)

    _functions = {'testRunning': _testRunning ,'newProgress': _newProgress, 'newResult': _newResult, 'reportCreated': _reportCreated}