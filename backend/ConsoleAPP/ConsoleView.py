from chvote.verifier.Observer import Observer
from chvote.verifier.MultiTest import MultiTest

class ConsoleView(Observer):
    """docstring for ConsoleView."""
    def update(self,state):
        report = self.report
        test = self.test
        if state == "TestRunning":
            print(test.id,test.title,"is running...","0%")
        elif state == "newProgress":
            prg = test.progress
            if prg > 0 and (prg - test.old_progress) > self.step:
                test.old_progress = prg
                print(test.id,test.title,"is {:.0%}".format(prg),"completed")

        else:
            res = report.last_result
            test = res.test
            print(test.id,test.title,"is finished",":",res.test_result)
