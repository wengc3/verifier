import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate
from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper
from chvote.Common.IsMemberOfGroupe import IsMemberOfGroupe

class DecryptionProofIntegrityTest(SingleTest):
    """docstring for DecryptionProofIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if pi_prime_j in (G_q x G_q^N) x Z_q
        >>> res = dpit.runTest({'pi_j': [['1265358721032139380715781836337448558496182681624063784971190147244360987136460031992013940636589597506682956470290541513138343217394381404797835941248736535487535881702095702191224668494553955242973502791981174101473048846057982091374182196456799539850988721094686366485655150184934167919030653307307682797173065446782414596137834662703090559835449604662857272302500826784273953115540007608886238432042646909348623297533999105728406492383733741362853003953919928226380069675017675010869481437024222431098761095246670769409821643988334366230298091961119565499840906844046265870282316628525162698695925346130843707205722696625077228566366558729017078280460126071187332656675641725163162207409033439013619001081930181553528436399202990879869892613738587164794940822286756192320538383761398329689828405224714843942180158866330610381006456274518459554581306524815102861416019552314347156740247473129631193903326427544711586077821', ['3411075207717230689760177504251743624968174228152744221679605862775283686977995054417200316188541551440291312674156314091422323981447733213425664834613786058881440125711128549822898033699082739766082148584047719612984007934096542165318207289122899424500284853343611357804500705517291182252717722927174856095067501770205305469085861309247139121374674616239213086445547061016754602261629837576521209083343890512378230475284552911834584427672466960723983468355597468016808017166371658784555042778248914818131070873918718408831160147542007254236365392083682811371216827326354091545143963977993392785191216986352971818182279354680932284793059354855188004702845440219121769812125189123110535634144964499480848618536193405941260676393943691199011213971342029463290351627997262584104240182030382033990145249520342607685757914927680614968775259519688525531803070278715177801914749618192711396286598285761119915632666901809147810600920', '2047879116176365635250998334027082224511273487032272311259281693343940043301846628422359067453826901006181756904767559157082719709722175903980865407727975674247545017912383180687441630717747772848383065016365632345303381518845957609959288815570581246516669818452200242802341422111510118839201168626137890282826446237553242104848008704468450235683222625916493083404557839665924153104544247464682916591123892966531583696441912583224137208628582239638955437408178172516745761761629718980170906254329921929716619986437292435078237069778599109520487575777014430023019278976212290341793413811560636736094321891094261693442368608835735156408224954676039523913890438431897006975933272929530009755710897087112877988730561884015667641968400969606240801435699497695935009813476278410876877938401181049958210875474362124260961867720205933482955909723138169988698342540261675442151118964891601885083520857581195368744629756964926395970539', '1765830039633851570158350184378627594794450071224004835481988848433918688973902659042741060692543505616445675823546722594420536976764780109374940172180277426200903679284099085963081268318054691568488122911030318502430827908721323798948816035948038227490850364763954500529465289302471980394928393894865750271381502899312809261664146701477830347429754901352434055054260128011516969884548496332164166913322857535563593642418235359880109924683820045450755361996992157128877232271113231191882744592945308936260021554045523508531663445859131286942568500537503902463913481427761408244736952501687929966864326280721616189482838517213554353716997114379308821540731990409154358831904594900830864250531656411812953883897315124743852555471329614014969991288845817824846775869737304526380425017730231660027702083862204782307422964386433867580360973667217284406850627978786953973873523697707482840239713564991549227442054217897096251495697']], '1479162054827085959657859083905946613705766302193190169462686733257385167003730370406150576327050549191474666840862708773329106724861124660292609309353073803794546535997060229750309039924739641852130095889943710510438952789408466486325312833669179452330842722712916283319910623654720805919655180411941498100526401494656646577608425312765043074087761641245626422938519133770030275452092120889759581302844814672908689021344376993993525573974510516681096904940411241980882362263575383982685372871763233778121433386772282195986929571992501796832986771848017041733078388465956460148653069899363108406288473433825943270178253261299709046324965924220265579483069211603442844991239650328568565912432854306433204310288465702722568362426559765595116757251031937600826017102577371503539694167177754038568401854865097184397523361561556744682581021153610465799254769173152973223853254958786616411784581781478212587329287749083223679135255']})
        >>> res.test_result
        'successful'
        """
        pi = self.test_data
        N = self.election_data['N']
        param = self.election_data['secparams']
        res_pi_t= IsMemberOfGroupe(mpz(pi[0][0]),param.p) and multiMathGroupeHelper(pi[0][1],N,param.p)
        res_pi_s = int(pi[1]) in range(param.q)
        return 'successful' if res_pi_t and res_pi_s else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    dpi_test = DecryptionProofIntegrityTest("1.1","TEST","TEST",["pi_j"])
    dpi_test.election_data = {'secparams': secparams_l3,'N': 3}
    doctest.testmod(extraglobs={'dpit': dpi_test})
