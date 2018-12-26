import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate
from chvote.Utils.mpzList import mpzList

from chvote.Common.IsMemberOfGroupe import IsMemberOfGroupe
from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper

def multiByteArrayHelper(vector,n,k,param):
    try:
        for i in range(n):
            for j in range(k):
                c = vector[i][j]
                if not type(c) is str:
                    return False
                if not len(bytearray.fromhex(c)) == param:
                    return False
        return True
    except IndexError:
        return False

class OTResponseIntegrityTest(SingleTest):
    """docstring for OTResponseIntegrityTest."""
    @completness_decorate
    def runTest(self,election_data):
        """
        Test if beta_j is in G_q^k_i x (Beta_bold^L_M)^n*k_i x G_q
        >>> res = orit.runTest({'voterId': 0, 'beta_j': [['964544642030089042698445902050542342558108560327685534297148545195327898253053509792686279022405200614301208861175248856707000656446014850882732903130228349395831596930416338388880808014354809290512613474137099881408489775990964749120185317623421950674803684185479091743043277268697747077229770402249849355278123326033785732736433644591136051587009073346347495162835599792099287714021975282524635702991425602626239659133222816428538782096944329425735358153927032764038348447744239115993292448991413112422436071552678624471268637493040862722196199351499157968593496882662883335596430999656362000030397463013924434260456104514119577084575378001328520629867501122007197488024888387534623634553279593211725265044257473058058292830631316551286083583756048014888017411899075792728704581322473076805014550594667318384274670879228013008194128893972661335822284158407075631758633461727791392099294321516031179484185436378152502223772'], [['acaaa3e0834cf4ee044d0bd04164bef824a4e4708d357c6a0b3d8b93091b1acf273b10b95ce5d9976602695305d70496e6911d537b32ef979eefbf969a3dc8e3'], ['9ec3105183fafe6bf354feafd256351458f67fc34462b4d9a118218d5698e243b587890bf69b30a916c5b82dbf91827b00da001f9e3c36b39a7f22ffa66bbbce'], ['b463230c73ebbbae039dc6a21925af845ea1e8a96368633b02f5d6ab82ac95bf3fbfad569c243a4d820130291ddf510e7f3cbe39b127cbf9f501e704fc5a5b5b']], '182242508400083455368714174223720732507430606064574725434551012186722694637713000841983066981444915388433616661393712747020066467517327489904272661493632874641753825079181211007516843862630286811255262966599852199058747514064286077075238067623921954916952214238285776308335436032138747465680027252151759341116377526285429054242907903129177188556029093321495967468588849707501911652442780416138119633924261354114936999943056634941343988132634619339835820079334367449692502471884471299590357149968675714034286462473056317293526735522751851455101565936418119195312404770662463188415663069785711238323164792695878382640593030092491903369745852928804131736178000017628691118529917051370932383733795241242335723247241583148553500226275583921984984442698926498877252157444436680287031698071577275776186316676011730144130241323161469729375579999203259645597355543904790104428270465011855907279145169371268524621186272579382508015249']})
        >>> res.test_result
        'successful'
        """
        beta_j = self.test_data
        voterId = election_data['voterId']
        eligMatrix = self.election_data['eligibilityMatrix'][int(voterId)]['e_i']
        k = self.election_data['k']
        n = self.election_data['n']
        param = self.election_data['secparams']
        k_i = sum(eligMatrix) * k
        res_b = multiMathGroupeHelper(mpzList(beta_j[0]),k_i,param.p)
        res_c_bold = multiByteArrayHelper(beta_j[1],n,k_i,param.L_M)
        res_d = IsMemberOfGroupe(mpz(beta_j[2]),param.p)
        self.test_result.addTestData('p',param.p)
        self.test_result.addTestData('L_M',param.L_M)
        self.test_result.addTestData('n',n)
        self.test_result.addTestData('k_i',k_i)
        return 'successful' if res_b and res_c_bold and res_d else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    ori_test = OTResponseIntegrityTest("1.1","TEST","TEST",["beta_j"])
    ori_test.election_data = {'eligibilityMatrix': [{'e_i': [{'e_j': True}]}, {'e_i': [{'e_j': True}]}, {'e_i': [{'e_j': True}]}], 'k': 1, 'n': 3, 'secparams': secparams_l3}
    doctest.testmod(extraglobs = {'orit': ori_test})
