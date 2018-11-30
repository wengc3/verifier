class TestResult(object):
    """docstring for TestResult."""
    def __init__(self, test,result,data):
        self._test = test
        self._test_result = result
        self._test_data = data
        self._children = dict()

    @property
    def test(self):
        return self._test

    @property
    def test_result(self):
        return self._test_result

    @property
    def test_data(self):
        return self._test_data

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self,children):
        self._children = children

    def getJSON(self,id):
        test = self.test
        children = list()
        for key, child in self.children.items():
            children.append(child.getJSON(key))
        return {'id': id, 'title': test.title, 'description': test.description, 'value': self.test_result, 'data': self.test_data, 'children': children}
