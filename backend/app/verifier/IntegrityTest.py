import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.verifier.SingleTest import SingleTest
from chvote.Common.IsMember import IsMember
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3

class VotingCircleIntegrityTest(SingleTest):
    """docstring for VotingCircleIntegrityTest."""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        """
        >>> vsct.runTest({'test':[1,1,1]})
        (True, [1, 1, 1])
        >>> vsct.runTest({'test':[]})
        (False, [])
        >>> vsct.runTest({'bla':123})
        (False, None)
        """
        key = self.getKey()
        try:
            w_bold = election_data[key]
            if not w_bold:
                return (False,w_bold)
            return (max(w_bold) >= 1,w_bold)
        except KeyError:
            return (False,None)

class PubKeyIntegritiyTest(SingleTest):
    """docstring for PubKeyIntegritiyTest."""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        """
        >>> pkit.runTest({'test':'2825134674255547482436547907372221026434167202542988730403107244543935989073998107827897533200684397769901947864744899330853790529762173410352107316894267271071231613989642479886116788007728269696555346745739381719994925852572019178816292186600074152031788324354411179326764125539035768027512464861267686265464479546323305741983169247395100545365925464419371891324950256121360162846641147611152110968173031342322989594644161777190784803351114112250146765793437740083895462785414690792273536925158387344576381837283839670637022835874580307742992512739900221204359744540288315056786501728048526741487627409593545469309543806208592479750770087081917814970917489914190870812924255144003202143839896664036901786607181539843182760343048108652015555124151072095519332464107223841447674750685349789885642356149776526376547998748277364472839670997609170135831066767283234117044295221380571925026012544165415783294007273059965817860223'})
        (True, '2825134674255547482436547907372221026434167202542988730403107244543935989073998107827897533200684397769901947864744899330853790529762173410352107316894267271071231613989642479886116788007728269696555346745739381719994925852572019178816292186600074152031788324354411179326764125539035768027512464861267686265464479546323305741983169247395100545365925464419371891324950256121360162846641147611152110968173031342322989594644161777190784803351114112250146765793437740083895462785414690792273536925158387344576381837283839670637022835874580307742992512739900221204359744540288315056786501728048526741487627409593545469309543806208592479750770087081917814970917489914190870812924255144003202143839896664036901786607181539843182760343048108652015555124151072095519332464107223841447674750685349789885642356149776526376547998748277364472839670997609170135831066767283234117044295221380571925026012544165415783294007273059965817860223')
        >>> pkit.runTest({'test':'123'})
        (False, '123')
        >>> pkit.runTest({'bla':'123'})
        (False, None)
        """
        key = self.getKey()
        try:
            pk_j = mpz(election_data[key])
            #secparams = Test.report.getSecurityParams() # uncomment for doctest
            secparams = self.getReport().getSecurityParams();
            return (IsMember(pk_j,secparams),election_data[key])
        except KeyError:
            return (False,None)

if __name__ == '__main__':
    import doctest
    from Report import Report
    from Test import Test
    Test.report = Report('id',None,secparams_l3);
    doctest.testmod(extraglobs={'vsct': VotingCircleIntegrityTest("1.1","TEST","TEST","test"),
                                'pkit': PubKeyIntegritiyTest("1.1","TEST","TEST","test")})
