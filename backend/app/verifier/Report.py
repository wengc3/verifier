class Report(object):
    """docstring for Report."""
    def __init__(self, election_id,secparams):
        self._election_id = election_id
        self._observers = set()
        #self.current_test = None
        self._last_result = None
        self._secparams=secparams
        self._result = dict()

    def addTestResult(self,res):
        test_id = res.test.id
        parent_id = int(test_id[0])
        child_dict = self._result.get(parent_id,dict())
        child_dict[test_id]=res
        self._result[parent_id]=child_dict
        self._last_result=res
        self._notify("newResult")

    def attach(self, observer):
        observer.report = self
        self._observers.add(observer)

    @property
    def last_result(self):
        return self._last_result

    # @property
    # def current_test(self):
    #     return self._current_test
    #
    # @current_test.setter
    # def current_test(self,test):
    #     self._current_test = test
    #     self._notify("TestRunning")

    def _notify(self,state):
        for observer in self._observers:
            observer.update(state)

    @property
    def observers(self):
        return self._observers

    @property
    def result(self):
        return self._result

    @property
    def security_params(self):
        return self._secparams

    def getStat(self,id):
        res_arr = self._result.get(int(id)).values()
        correct_test = len(list(filter(lambda x: x.test_result=='successful',res_arr)))
        return str(correct_test)+"/"+str(len(res_arr)-1)
