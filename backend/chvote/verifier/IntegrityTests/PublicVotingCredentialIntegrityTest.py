import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper

class PublicVotingCredentialIntegrityTest(SingleTest):
    """docstring for PublicVotingCredentialIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if x_j,y_j is in G_q_hat
        >>> res = pvcit.runTest({'d_hat_j': ['10729722235944325116265925487240351218108066854272454570275986057971857440212362366387286540590242025229488950774004015883323608514429060218566527330370220337766212627504421500361939783530728713302949139931928368454826547144576626874326282472131594410286247630327282331564261574365253922044764793815526821369387502716327641478337598515846158878373256817417737368556077672274845509023292018798959766908609004182711437188847083594026377930322994611276291547370838820231537292584230330094413072421643747911593385217989636534058870393124682411414913832592733196457930724963597528512647963405757077955416910093477115445879779398469104779234126872084151022203700713382625237370790617929059595149375318182799872820822416352656165389901314440611479590788828223419876066275356606938422612279298823843774164297156463472357837879208389962048985821802465122687584615471781773574910747606692466916007985152813521822163093623945019953655', '2575203165450752312745397201322418337662420404996904691712111171548464147564941889328993977132258194891537600540304559801747881796123341269384380455473131374947298526835619311802259660622013068428168991681304173072125713955932314709602795638841916296916041243711862610211202466059353044021405944161015759539888746383768566065947139303047574011165867013638423489894877719755046795581766063473048552099547801494071463960067167430130488812739128662367043638871524596182279767968668384856430686224913969990127266806467380585568168685661842473908974450492727627455993582079388037878031437900299003250013539500540305897232603802419603361430554010924747212068308957418607513992128696263497620468010641243871868628933717647597773093956860629572288799818043303506754509966977093384172775309491843026532187383702690991762761424149233031275718549313766353945915226041150797319038449609631092899794967332042572112462940383367396620910559']})
        >>> res.test_result
        'successful'
        >>> res = pvcit.runTest({'d_hat_j': ['2575203165450752312745397201322418337662420404996904691712111171548464147564941889328993977132258194891537600540304559801747881796123341269384380455473131374947298526835619311802259660622013068428168991681304173072125713955932314709602795638841916296916041243711862610211202466059353044021405944161015759539888746383768566065947139303047574011165867013638423489894877719755046795581766063473048552099547801494071463960067167430130488812739128662367043638871524596182279767968668384856430686224913969990127266806467380585568168685661842473908974450492727627455993582079388037878031437900299003250013539500540305897232603802419603361430554010924747212068308957418607513992128696263497620468010641243871868628933717647597773093956860629572288799818043303506754509966977093384172775309491843026532187383702690991762761424149233031275718549313766353945915226041150797319038449609631092899794967332042572112462940383367396620910559']})
        >>> res.test_result
        'failed'
        """
        vector = self.test_data
        param = self.election_data['secparams']
        return 'successful' if multiMathGroupeHelper(vector,2,param.p_hat) else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    pvci_test = PublicVotingCredentialIntegrityTest("1.1","TEST","TEST",["d_hat_j"])
    pvci_test.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs={'pvcit': pvci_test})
