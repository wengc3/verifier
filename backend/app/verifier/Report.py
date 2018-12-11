import json

class Report(object):
    """docstring for Report."""
    def __init__(self, election_id):
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
        self.generateJSONResult()

    @property
    def electionID(self):
        return self._election_id

    def generateJSONResult(self):
        report = list()
        for category in self.result.children:
            report.append(category.getJSON())
        self.json_result = json.dumps(report, default=str)
        self._notify('reportCreated')

    def _notify(self,state):
        for observer in self.result.observers:
            observer.update(state)
