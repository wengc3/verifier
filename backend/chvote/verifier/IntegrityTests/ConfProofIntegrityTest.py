import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.Common.IsMemberOfGroupe import IsMemberOfGroupe
from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper

class ConfProofIntegrityTest(SingleTest):
    """docstring for ConfProofIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if pi is in G_q_hat x Z_q_hat
        >>> res = cpit.runTest({'pi': ['1672080953091796511557025684900844296353395227467030452781712449256225585438226809989376622796616424380092701992483510809466227459274137363033908273419033518986698324069161659406486296488968901394308170243560930766099641749889195282336128498971857298899639466152908095912659628607903985043305766334618549315588681125937334308567704989951244281584203353105355381777342588738643402509160434824486863954723970280710373541330320274618623983301233986587503372044353502768938770913960911891021681376089814871666648624632109753345178420658829721008540103904368183333282902168431883567720908711672612944538548222959380666958586543426722994873960391421586188424068282816697491148607671099215614692287764866437607483950628639915609525916412333733433730599227769656231541104561016868030869459446164614164007151913126658296340926113224092362060033889607150192859800949026609989485910677518666063321228231215086526289850697572284247507919', '132974664627115262935730375367823913373043586563628781795029924533025538885369']})
        >>> res.test_result
        'successful'
        """
        key = self.key
        param = self.election_data['secparams']
        pi = election_data['confirmation']['pi']
        res_pi_t = IsMemberOfGroupe(mpz(pi[0]),param.p_hat)
        res_pi_s = int(pi[1]) in range(param.q) # is not q_hat
        return 'successful' if res_pi_t and res_pi_s else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    cpi_test = ConfProofIntegrityTest("1.1","TEST","TEST","pi")
    cpi_test.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs = {'cpit': cpi_test})
