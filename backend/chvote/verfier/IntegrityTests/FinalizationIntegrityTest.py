import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper

class FinalizationIntegrityTest(SingleTest):
    """docstring for RandomizationIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if delta_j is in Beta_bold^L_F x Z_q^2
        >>> res = finit.runTest({'delta_j': ['bd71d6', ['1831986403262649955652904389706541889254686449140033370003149202152642562915758661734516250605240923667581542550295288360751908860491525748857585757379333805614802585908751713030563292455211190765858064047348414137968893671431031232130157439416680557203978473162987442561384874146014722020096830442190571393561891460012537103086439534652630054317804602238483504682101910335390171158361346309050480125803816562557708095961069062760077507849986450152023329283851502046690940369788582237640538405048977535412600484909245244481823978547030045971312515882289201679615889127758107687714016430393760132202668677287260585051467034499728388168139240800781345634322137421253701332434952149141137177793512365714943675305028559127129169707241364743794063012690638372421090431195368180367326094917051282864769810527243143422245325157851974903254370033051943790293357966419634576614893079320794896735722781762905193357879247101095832881172', '1103374979108424535163799151219973971122127057687892019877419095849809925036021347351797578564676402345896845570978623021689948842911884547630996357389998028627000751795144747263870847373150678732028902965181782207572078347010952719246587618413281268275262023894170389622204731067209394279757690247216541827235765003993179150714481113923394922336808407274501667749402168922722150390772317762422966242672836328752704837524293121717674509415755349279687281174236287854888772716338068214799786902140626579653592622129120819793322969016183621749276103884183389716009782927613030534897561237639907066274295788775470256307720773601991332354400996416688687490750043963851624200480570893664508578854262913336841198737468526336245545352396840556915762350338492949674459631969747744321387169585557957933840677128763976983272136671327017211917677308666179920337004254616813130591442417700259223841354675233592526117225170327370785700130']]})
        >>> res.test_result
        'successful'
        """
        delta_j = self.test_data
        param = self.election_data['secparams']
        res_f = len(bytearray.fromhex(delta_j[0])) == param.L_F
        res_rand = int(delta_j[1][0]) in range(param.q) and int(delta_j[1][1]) in range(param.q)
        return 'successful' if res_f and res_rand else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    fini_test = FinalizationIntegrityTest("1.1","TEST","TEST",["delta_j"])
    fini_test.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs = {'finit': fini_test})
