from chvote.verifier.Observer import Observer
import json

class ConsoleView(Observer):
    """docstring for ConsoleView."""

    def update(self,state):
        id = self.result.test.id
        if  ':' not in id and id.count('.') <= self.depth :
            try:
                func = self._functions[state]
                func(self)
            except KeyError:
                raise AttributeError('this function is not defined')

        if state == 'reportCreated':
            self._reportCreated()


    def _testRunning(self):
        test = self.result.test
        print(test.id,test.title,"is running...","0%")

    def _newProgress(self):
        result = self.result
        test = result.test
        prg = result.progress
        if prg > 0 and (prg - result.old_progress) > self.step:
            result.old_progress = prg
            print(test.id,test.title,"is {:.0%}".format(prg),"completed")

    def _newResult(self):
        result = self.result
        test = result.test
        print(test.id,test.title,"is finished",":",result.test_result)

    def _reportCreated(self):
        results = json.loads(self.report.json_result)
        import pdb; pdb.set_trace()

    _functions = {'testRunning': _testRunning ,'newProgress': _newProgress, 'newResult': _newResult,'reportCreated': _reportCreated}
