import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.Common.IsMemberOfGroupe import IsMemberOfGroupe

class BiggerThanIntegrityTest(SingleTest):
    """docstring for ListBiggerThanIntegrityTest."""
    def __init__(self,id,title,description,key,min_size):
        SingleTest.__init__(self, id,title,description,key)
        self.min_size = min_size

    @completness_decorate
    def runTest(self,election_data):
        """
        >>> res = btit.runTest({'test': 1})
        >>> res.test_result
        'successful'
        >>> res.test_data
        [{'test': 1}, {'min_size': 1}]
        >>> res = btit.runTest({'test': 0})
        >>> res.test_result
        'failed'
        >>> res.test_data
        [{'test': 0}, {'min_size': 1}]
        >>> res = btit.runTest({'bla': 1})
        >>> res.test_result
        'skipped'
        >>> res.test_data
        []
        """
        key = self.key
        value = election_data[key]
        self.test_result.addTestData('min_size',self.min_size)
        return 'successful' if  value >= self.min_size else 'failed'


class MathGroupeIntegritiyTest(SingleTest):
    """docstring for PubKeyIntegritiyTest."""
    def __init__(self,id,title,description,key,param):
        SingleTest.__init__(self, id,title,description,key)
        self.param = param


    @completness_decorate
    def runTest(self,election_data):
        """
        >>> res = pkit.runTest({'test':'2825134674255547482436547907372221026434167202542988730403107244543935989073998107827897533200684397769901947864744899330853790529762173410352107316894267271071231613989642479886116788007728269696555346745739381719994925852572019178816292186600074152031788324354411179326764125539035768027512464861267686265464479546323305741983169247395100545365925464419371891324950256121360162846641147611152110968173031342322989594644161777190784803351114112250146765793437740083895462785414690792273536925158387344576381837283839670637022835874580307742992512739900221204359744540288315056786501728048526741487627409593545469309543806208592479750770087081917814970917489914190870812924255144003202143839896664036901786607181539843182760343048108652015555124151072095519332464107223841447674750685349789885642356149776526376547998748277364472839670997609170135831066767283234117044295221380571925026012544165415783294007273059965817860223'})
        >>> res.test_result
        'successful'
        >>> res.test_data
        [{'test': '2825134674255547482436547907372221026434167202542988730403107244543935989073998107827897533200684397769901947864744899330853790529762173410352107316894267271071231613989642479886116788007728269696555346745739381719994925852572019178816292186600074152031788324354411179326764125539035768027512464861267686265464479546323305741983169247395100545365925464419371891324950256121360162846641147611152110968173031342322989594644161777190784803351114112250146765793437740083895462785414690792273536925158387344576381837283839670637022835874580307742992512739900221204359744540288315056786501728048526741487627409593545469309543806208592479750770087081917814970917489914190870812924255144003202143839896664036901786607181539843182760343048108652015555124151072095519332464107223841447674750685349789885642356149776526376547998748277364472839670997609170135831066767283234117044295221380571925026012544165415783294007273059965817860223'}, {'p': mpz(4172934416980964965169201951325235733279240114847017455430592564077918886073641276586591389004355462305973678333170208639939088255121687131786362360215111403351065309592969637680716009236830711810152064190853843544408910676143305334871951860867924554435441203493181159798485763406603105153501704547766243664786045439065352932048014751002587847119946822822046319865934012391473272070904218816772115153556686556266502473705385467188396395051748108633385151379651157033036473175759056135044203623900979383111145851128240938779457100859422200697223513525500908222436171337452217611384500565599401229274630892207902574777517046260946681290072126388118955012886408492137365891503147095623663121959125421800149860024839568125839106274340172921428312269003251077695557686543670945684591732570428494731067233985519130887627478786060954867707429567371112131601380152365880179827354833609656564228760058727175683162963370189000001297623)}]
        >>> res = pkit.runTest({'test':'123'})
        >>> res.test_result
        'failed'
        >>> res.test_data
        [{'test': '123'}, {'p': mpz(4172934416980964965169201951325235733279240114847017455430592564077918886073641276586591389004355462305973678333170208639939088255121687131786362360215111403351065309592969637680716009236830711810152064190853843544408910676143305334871951860867924554435441203493181159798485763406603105153501704547766243664786045439065352932048014751002587847119946822822046319865934012391473272070904218816772115153556686556266502473705385467188396395051748108633385151379651157033036473175759056135044203623900979383111145851128240938779457100859422200697223513525500908222436171337452217611384500565599401229274630892207902574777517046260946681290072126388118955012886408492137365891503147095623663121959125421800149860024839568125839106274340172921428312269003251077695557686543670945684591732570428494731067233985519130887627478786060954867707429567371112131601380152365880179827354833609656564228760058727175683162963370189000001297623)}]
        >>> res = pkit.runTest({'bla':'123'})
        >>> res.test_result
        'skipped'
        >>> res.test_data
        []
        """
        key = self.key
        param = getattr(self.election_data['secparams'],'p')
        num = mpz(election_data[key])
        self.test_result.addTestData(self.param,param)
        return 'successful' if IsMemberOfGroupe(num,param) else 'failed'


if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    pktest= MathGroupeIntegritiyTest("1.1","TEST","TEST","test","p")
    pktest.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs={'btit': BiggerThanIntegrityTest("1.1","TEST","TEST","test",1),
                                'pkit':pktest})
