import abc

class Observer(metaclass=abc.ABCMeta):
    """docstring for Observer."""
    def __init__(self,step,depth,report):
        self._report = report
        self._result = None
        self._step = step
        self._depth = depth

    @abc.abstractmethod
    def update(self, state):
        pass

    @abc.abstractmethod
    def _testRunning(self):
        pass

    @abc.abstractmethod
    def _newProgress(self):
        pass

    @abc.abstractmethod
    def _newResult(self):
        pass

    @abc.abstractmethod
    def _reportCreated(self):
        pass


    @property
    def depth(self):
        return self._depth

    @property
    def report(self):
        return self._report

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self,result):
        self._result = result

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self,report):
        self._test = report

    @property
    def step(self):
        return self._step
