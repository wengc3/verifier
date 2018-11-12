from app.verifier.SingleTest import SingleTest
from app.verifier.TestResult import TestResult

class CertificateAuthenticityTest(SingleTest):
    """docstring for CertificateTest."""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data,report):
        "Certificates are not in election_data"
        self._notify("TestRunning")
        self.progress = 1
        return TestResult(self,'skipped',{})
