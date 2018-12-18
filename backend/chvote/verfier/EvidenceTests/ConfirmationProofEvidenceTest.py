import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.ElectionAuthority.CheckConfirmationProof import CheckConfirmationProof


class ConfirmationProofEvidenceTest(SingleTest):
    """docstring for ConfirmationProofEvidenceTest."""
    @completness_decorate
    def runTest(self,election_data):
        """
        >>> res = cpet.runTest({'confirmation': {'y_hat': '1484121251359951826104471183378273385476808659179653987458913813025841039653028785875672202336141400847991512813054120103935105866446806105895660359602490911310084175136776030446559780778246070981959478555394811620507184713378972350067472848892554269751032260991199573004127142879236094919867447026005955096669712367606732047320841147980072831354851596478690750073999300188937151468979473011073755689418365913019492171003111908825585668343259495256754299745904149779795126122788297864413663488269865030395733023170328151692094989593165899588149012782159359453976811095077850581949211082630987254356304167673355577013347893952834056484872114681455870432581919766422480245066971872362496657711569548591189237322304229753237669246240033521384802132785693275283065907181656115077843889953632434911395273755410678927825165762887206181668571329435823036449631952013857352705434047714317685519583000937405895239259979218336208892373', 'pi':['1672080953091796511557025684900844296353395227467030452781712449256225585438226809989376622796616424380092701992483510809466227459274137363033908273419033518986698324069161659406486296488968901394308170243560930766099641749889195282336128498971857298899639466152908095912659628607903985043305766334618549315588681125937334308567704989951244281584203353105355381777342588738643402509160434824486863954723970280710373541330320274618623983301233986587503372044353502768938770913960911891021681376089814871666648624632109753345178420658829721008540103904368183333282902168431883567720908711672612944538548222959380666958586543426722994873960391421586188424068282816697491148607671099215614692287764866437607483950628639915609525916412333733433730599227769656231541104561016868030869459446164614164007151913126658296340926113224092362060033889607150192859800949026609989485910677518666063321228231215086526289850697572284247507919', '132974664627115262935730375367823913373043586563628781795029924533025538885369']}})
        >>> res.test_result
        'successful'
        >>> res.test_data
        [{'confirmation': {'y_hat': '1484121251359951826104471183378273385476808659179653987458913813025841039653028785875672202336141400847991512813054120103935105866446806105895660359602490911310084175136776030446559780778246070981959478555394811620507184713378972350067472848892554269751032260991199573004127142879236094919867447026005955096669712367606732047320841147980072831354851596478690750073999300188937151468979473011073755689418365913019492171003111908825585668343259495256754299745904149779795126122788297864413663488269865030395733023170328151692094989593165899588149012782159359453976811095077850581949211082630987254356304167673355577013347893952834056484872114681455870432581919766422480245066971872362496657711569548591189237322304229753237669246240033521384802132785693275283065907181656115077843889953632434911395273755410678927825165762887206181668571329435823036449631952013857352705434047714317685519583000937405895239259979218336208892373', 'pi': ['1672080953091796511557025684900844296353395227467030452781712449256225585438226809989376622796616424380092701992483510809466227459274137363033908273419033518986698324069161659406486296488968901394308170243560930766099641749889195282336128498971857298899639466152908095912659628607903985043305766334618549315588681125937334308567704989951244281584203353105355381777342588738643402509160434824486863954723970280710373541330320274618623983301233986587503372044353502768938770913960911891021681376089814871666648624632109753345178420658829721008540103904368183333282902168431883567720908711672612944538548222959380666958586543426722994873960391421586188424068282816697491148607671099215614692287764866437607483950628639915609525916412333733433730599227769656231541104561016868030869459446164614164007151913126658296340926113224092362060033889607150192859800949026609989485910677518666063321228231215086526289850697572284247507919', '132974664627115262935730375367823913373043586563628781795029924533025538885369']}}]
        """
        confirmation = self.test_data
        pi = confirmation.get('pi')
        s,t = pi
        mpz_pi = (mpz(s),mpz(t))
        y_hat = confirmation.get('y_hat')
        secparams = self.election_data['secparams']
        res = CheckConfirmationProof(mpz_pi, mpz(y_hat), secparams)
        return 'successful' if res else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    cpe_test = ConfirmationProofEvidenceTest("1.1","TEST","TEST",["confirmation"])
    cpe_test.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs = {'cpet': cpe_test})
