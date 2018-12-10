class TestResult(object):
    _observers = set()
    """docstring for TestResult."""
    def __init__(self, test,result,data):
        self.id = test.id
        self._test = test
        self._test_result = result
        self._test_data = dict()
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
        if data and isinstance(data,list) and all(isinstance(x, dict) for x in data):
            for item in data:
                self.test_data.update(item)
        else:
            self.test_data[key] = data

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
            if 'multi' in child.id:
                iter_results = child.extractTests()
                for iter_result in iter_results:
                    children.append(iter_result.getJSON())
            else:
                children.append(child.getJSON())
        return {'id': self.id, 'title': test.title, 'description': test.description, 'value': self.test_result, 'data': self.test_data, 'children': children}

    def extractTests(self):
        iter_res_list = list()
        child = self.children[0]
        for sub_child in child.children:
            test = sub_child.test
            res = TestResult(test,"",self.test_data)
            res.id = test.id[:-2]
            res.children = self.getChildsById(res.id)
            res.test_result = 'successful' if all(r.test_result == "successful" for r in res.children) else 'failed'
            iter_res_list.append(res)
        return iter_res_list

    def getChildsById(self,id):
        children_list = list()
        for child in self.children:
            for sub_child in child.children:
                if id in sub_child.id:
                    children_list.append(sub_child)
        return children_list


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

    def reportCreated(self):
        self._notify("reportCreated")

#observer methods
    def _notify(self,state):
        for observer in self.observers:
            observer.result = self
            observer.update(state)

    @property
    def observers(self):
        return self._observers

    @staticmethod
    def attach(observer):
        TestResult._observers.add(observer)
