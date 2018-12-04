class Observer(object):
    """docstring for Observer."""
    def __init__(self,step):
        self._report = None
        self._test = None
        self._step = step
        self._old_progress = 0

    @property
    def report(self):
        return self._report

    @report.setter
    def report(self,report):
        self._report = report

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self,report):
        self._test = report

    @property
    def step(self):
        return self._step
