class TestResult(object):
    """docstring for TestResult."""
    def __init__(self, test,result,data):
        self._test = test
        self._test_result = result
        self._test_data = data

    @property
    def test(self):
        return self._test

    @property
    def test_result(self):
        return self._test_result

    @property
    def test_data(self):
        return self._test_data
