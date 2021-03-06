class TestResult(object):
    _report = None
    """docstring for TestResult."""
    def __init__(self, test,result,data):
        self.id = test.id
        self._test = test
        self._test_result = result
        self._test_data = list()
        self._children = list()
        self._old_progress = 0
        self._notify('testRunning')

    @property
    def test(self):
        return self._test

    @property
    def test_result(self):
        return self._test_result

    @test_result.setter
    def test_result(self,res):
        if res in ['successful','failed','skipped']:
            self._test_result = res

    @property
    def test_data(self):
        return self._test_data

    def addTestData(self,key,data):
        if data and isinstance(data,str) and all(isinstance(x, dict) for x in data):
            self.test_data.extend(data)
        else:
            self.test_data.append({key: data})

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self,children):
        self._children = children

    def getJSON(self):
        test = self.test
        children = list()
        for child in self.children:
            children.append(child.getJSON())
        return {'id': self.id, 'title': test.title, 'description': test.description, 'value': self.test_result, 'data': self.test_data, 'children': children}

    def addChild(self,child):
        self.children.append(child)
        self.last_child = child
        child._notify("newResult")

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self,new_progress):
        self._progress = new_progress
        self._notify("newProgress")

    @property
    def old_progress(self):
        return self._old_progress

    @old_progress.setter
    def old_progress(self,old_prg):
        self._old_progress = old_prg

    @property
    def observers(self):
        return self._report.observers

    @staticmethod
    def setReport(report):
        TestResult._report = report


#observer method
    def _notify(self,state):
        for observer in self.observers:
            observer.result = self
            observer.update(state)
