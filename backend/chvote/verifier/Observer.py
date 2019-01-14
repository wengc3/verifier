import abc

class Observer(metaclass=abc.ABCMeta):
    """docstring for Observer."""
    def __init__(self):
        self._report = None
        self._result = None

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
    def report(self):
        return self._report

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self,result):
        self._result = result
