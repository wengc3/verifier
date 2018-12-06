from app.utils.JsonParser import mpzconverter
import json

class Report(object):
    """docstring for Report."""
    def __init__(self, election_id,secparams):
        self._election_id = election_id
        self._json_result = None
        self._result = None

    @property
    def json_result(self):
        return self._json_result

    @json_result.setter
    def json_result(self,json):
        self._json_result = json

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self,result):
        self._result = result
        self.generateReport()

    @property
    def electionID(self):
        return self._election_id

    def generateReport(self):
        report = list()
        for category in self.result.children:
            report.append(category.getJSON())
        self.final_result = json.dumps(report, default=mpzconverter)
        self._notify('reportCreated')

    def _notify(self,state):
        for observer in self.result.observers:
            observer.update(state)
