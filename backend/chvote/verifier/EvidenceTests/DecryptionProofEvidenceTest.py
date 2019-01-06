import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate
from chvote.Utils.mpzList import mpzList

from chvote.ElectionAuthority.CheckDecryptionProof import CheckDecryptionProof
from chvote.Types import ElGamalEncryption, DecryptionProof

def generateElgamal(data_matrix):
    return [ElGamalEncryption(mpz(item[0]),mpz(item[1])) for item in data_matrix]

def generateDecryptionProof(decryption_proof):
    pi_t = decryption_proof[0]
    pi_s = decryption_proof[1]
    t = [mpz(pi_t[0])]+[mpzList(pi_t[1])]
    s = mpz(pi_s)
    return DecryptionProof(t,s)

class DecryptionProofEvidenceTest(SingleTest):
    """docstring for DecryptionProofEvidenceTest."""
    @completness_decorate()
    def runTest(self,election_data):
        """
        >>> res = dpet.runTest({'pi_j': [['1265358721032139380715781836337448558496182681624063784971190147244360987136460031992013940636589597506682956470290541513138343217394381404797835941248736535487535881702095702191224668494553955242973502791981174101473048846057982091374182196456799539850988721094686366485655150184934167919030653307307682797173065446782414596137834662703090559835449604662857272302500826784273953115540007608886238432042646909348623297533999105728406492383733741362853003953919928226380069675017675010869481437024222431098761095246670769409821643988334366230298091961119565499840906844046265870282316628525162698695925346130843707205722696625077228566366558729017078280460126071187332656675641725163162207409033439013619001081930181553528436399202990879869892613738587164794940822286756192320538383761398329689828405224714843942180158866330610381006456274518459554581306524815102861416019552314347156740247473129631193903326427544711586077821', ['3411075207717230689760177504251743624968174228152744221679605862775283686977995054417200316188541551440291312674156314091422323981447733213425664834613786058881440125711128549822898033699082739766082148584047719612984007934096542165318207289122899424500284853343611357804500705517291182252717722927174856095067501770205305469085861309247139121374674616239213086445547061016754602261629837576521209083343890512378230475284552911834584427672466960723983468355597468016808017166371658784555042778248914818131070873918718408831160147542007254236365392083682811371216827326354091545143963977993392785191216986352971818182279354680932284793059354855188004702845440219121769812125189123110535634144964499480848618536193405941260676393943691199011213971342029463290351627997262584104240182030382033990145249520342607685757914927680614968775259519688525531803070278715177801914749618192711396286598285761119915632666901809147810600920', '2047879116176365635250998334027082224511273487032272311259281693343940043301846628422359067453826901006181756904767559157082719709722175903980865407727975674247545017912383180687441630717747772848383065016365632345303381518845957609959288815570581246516669818452200242802341422111510118839201168626137890282826446237553242104848008704468450235683222625916493083404557839665924153104544247464682916591123892966531583696441912583224137208628582239638955437408178172516745761761629718980170906254329921929716619986437292435078237069778599109520487575777014430023019278976212290341793413811560636736094321891094261693442368608835735156408224954676039523913890438431897006975933272929530009755710897087112877988730561884015667641968400969606240801435699497695935009813476278410876877938401181049958210875474362124260961867720205933482955909723138169988698342540261675442151118964891601885083520857581195368744629756964926395970539', '1765830039633851570158350184378627594794450071224004835481988848433918688973902659042741060692543505616445675823546722594420536976764780109374940172180277426200903679284099085963081268318054691568488122911030318502430827908721323798948816035948038227490850364763954500529465289302471980394928393894865750271381502899312809261664146701477830347429754901352434055054260128011516969884548496332164166913322857535563593642418235359880109924683820045450755361996992157128877232271113231191882744592945308936260021554045523508531663445859131286942568500537503902463913481427761408244736952501687929966864326280721616189482838517213554353716997114379308821540731990409154358831904594900830864250531656411812953883897315124743852555471329614014969991288845817824846775869737304526380425017730231660027702083862204782307422964386433867580360973667217284406850627978786953973873523697707482840239713564991549227442054217897096251495697']], '1479162054827085959657859083905946613705766302193190169462686733257385167003730370406150576327050549191474666840862708773329106724861124660292609309353073803794546535997060229750309039924739641852130095889943710510438952789408466486325312833669179452330842722712916283319910623654720805919655180411941498100526401494656646577608425312765043074087761641245626422938519133770030275452092120889759581302844814672908689021344376993993525573974510516681096904940411241980882362263575383982685372871763233778121433386772282195986929571992501796832986771848017041733078388465956460148653069899363108406288473433825943270178253261299709046324965924220265579483069211603442844991239650328568565912432854306433204310288465702722568362426559765595116757251031937600826017102577371503539694167177754038568401854865097184397523361561556744682581021153610465799254769173152973223853254958786616411784581781478212587329287749083223679135255'], 'e_bold': [['3573457942231889976267774062662722803608177565254592653358563465597544940266529507081569242521487783148558986152658919141512398713211302225689978203852704512493084622264054075533830967455926488003115971217369989726841039430397517323812610237658458793542634015028809112354114565852190367062467023741672571649643111178190753622755910918217165328573769835124990638313869417362830354032170000090205258672213198227395846956081652302767410279953957888062045122026651817273854216125741448821027126192092830838681911015699839785611725935369160714941418313483907402849955226005061263973430991341406867892163380166418886032334126726709207281856852048156240891587617660514766566554737006298522462822650858117536339445307719393582555004260976289892473474293574538318172241508528125313109445192424000699437005553365884090299571605726059111603187401299522145726837667563126254247658059693241068962123590632234687340005517444943807053532713', '2609085856865318107713626694757434198695232857648245103442129644157640224541223099183069339182621830104655438483529572908183414533039845355957070037216744356976502442271464316882642034602601904997194183348713574942075882041369472258247735962852473257464236450190092941285121147210826156863058960789808844458449167060843502719739714088406237470323057261842906064588683778020750466931104771239169960136741675908303472839671791133077922852650791119382697987698092403106743732831135485578430541436805488647624736329626163816941657098108919261572097690878112871398493435066583898952239813543614009057080302434295743859183165103974117925058312405811487330616788041497880845697422164179554017428513808630749005302725110703012787791985886717922034590112751590144921339197991804549355884060965211753824129131358134217988051247772771508745619794740108234159195029952320012576374457651383282558522227126547755088279975087864276153052562'], ['51092347707105879920084655517569963537532524940049328024290697399061514706005482770992340040111059419270738042130441091176074887224732082431783320313143582622694195188118595504200484793751073084141115936713600187711374573397275736144483221617166851565200340359164440628729357101427139094902604457239636893701183981432399947677794274597601564466321884407796191959781210230263862707729771930523139790127711298941561693477758514183554398945515662411233018082842080323477863085553658839329985325068173122758633573990288066872832319090891323471787351282488651892075129492943560115476227123929669268309824880597121043223124245032986440256584803033788487335115578956430712053576508874340768671028826409795262311732389617804009424017705661584090675306246498499142185094191692424916984532970185746727435173426535784290167731078703438474208444171947436727211643918170642125942914254388570244817735630816389272199089478478905400923997', '635147803659206952310397352210334154085637431406818453067486950990030356933253013484550318332917553779021412563035996419857947395906939508236121473449323179109560382708447475595351845720258330873526610935359453834349732091465111555776529877110827616436512685927641300633588812753840119778592045845962549530983529508154556065382891042189655969600699525141902923119606853697252304939384538657652241580924635706593882941226321499251851321965415041807700610035345044393166876854995504612981920110413988672651268311832514164667767099898244011133852412800715319075419566223949716288975958737615199777279009407129371574298502445947196970550920348499393282756585697264386158054056113585027240968248792295505121615893074776686581502192434180854462568626042366591837344233516233128170387456911519416279328840850481139279779467624781516652368983653564909066938853176037292286766644924899067087150509566292514438843317282444736934112288'], ['1303399384475888052937697582091487950120540109213893372516116392820122756350271446497803089454985693255226684651167876254194351316053666978328992649536974340617683203359458059603232152024643425749847812377812438930455166739054560233233534424321322671689440959821864801118723244764555269970677498276065007069833010520218834363894567139244467138568085832076643305430499313571625369698779351245287374062657778769195526889947943305657328567217242784688016316014140675585590597253830003826251320192317761948240292877496745871135722103378373383554820097087136989704270731750980930058637809825463559510037114975205875865342489606171375340887389399624482676180216435865854974582549100060679066470364487887659296008411605434218199654270876555700739366680573282191820380465344023771072616930876632560733333983969693602890514722683306045294545541772652361170926633093532550826661485036965574087372811051558270462882111869052366704887073', '2670440767310486662905299922715038644136853812847006004738606831846488833659840695333646369190820844634158719186608437135492779106897377593067636508343271785229930197594769936615769055768096999370895932621453763700476447353586081841284569618735349386054649849286011582027779202115451443536021481964217168678311708942088009676038987444101630611523018337042914935806070500835506258593962817382594560923014330456292888909197075057775252115287822682287235316485984669085624954248824186834506582438631683673516796808768593651220697178113529773332042726555614536202930822690612148343568351713250285952167696010266122673900039719961193988524085108102839530758100926116619110005751310370998595794252738741606424320757113193892127162458685820744513790345432194044032782281354051145210275639094909655759986814978591089050110368734967161279588462545526222528083061941919348577661668448622084352548237476231794523846914007283244528577602']], 'b_bold_prime_j': ['1022515636834304568338530955408098580734488050967574796458735411874389526687922802845835328335744075190543736928456638151799727007605864703418872547556279136429918240013201576865596762389022684447675276563670519407067681460071594430857713668010122907255563669770462942783977365457366880825854350134317208235172253105785525533451441357412731801298449004554102585606812139732422650435098410474299459480278425710323037624798833274788102721595314645253631942813798874401143227974948435024714642029884243487714062333046123045440227738578178322246371873231539411881108851368815395989435100170163482077220265577796786045031132586872229204580972645268731026665101389862846286073710738896451423499463298529305554070480685654230198201259323220722602658593061746505861552497870606906176818584337906764485049874345074678938451206423816508415511637621571415790846730362515472362191367412627158375163479190573884313994751891217296583227981', '3637886505155529718585013062351648361340432005291634055951393670262836363520763636484078311534826865180501570408637223008333176267149150277871072677368924786832870446375979129992100097344971961577615211874891998757069758157674973315673411388530985602853116234830554146114003327544488062967801470881304418472164261075184409190263082473822446323835058095236422008894410233370096366498783966229134309367848463893335128868662101910146039281803481965132203313227659815267712101049180439945192482347495400797151429281854335451141724468921276061141359816542693092917328947127531035318998645817193076649379428799870515508752001296462899556262653327062518669668703496577377650553048162598165621693541532263187370915338454789030132587445442501711190838981868818787601455106389371657929407463780882450951347283242233282121778237451404315525054195800858114364718301317237219837653164678135964738862414911865199698197611884154402697426317', '3432609334079079612286504642415731295126107993236664400484554993439499831802379907251328211977361967446007683492475817363608114470546633530116324108709629128927323874534875257518007044997737904361749539866199074415790974443738981082845380093313796098556232187844137089471412288316089499115395285833230913532508304293472369383344107590069753333858747887809685296727831812381312318857458654855206820041047259125143598122654002789306806097969514152345058183470269458798001612254020219244797338115146597257737854850160792130183433212390979993045805425486534072787269377517978675002595875923290884150551793297690439541133357978404633635824815484398584986281321734172838518869079444464261412471276176558615065634835975087573021995641954618033771910699669521242692681866127570540765384920921303551240831143145387418323844488174604669867500855805454208610099288663318825469549064168001599922591562136784231802773314153159133170573089'], 'pk_j': '3201698212372225591658453783168168951275784006752333889126521587653034519261557303524075629648459904856438972611991744335511254337996689709804098377454199099561093086203560944306330244066388731269936231700758945086651762373713583677424413325934051836484567831798063118139932145683479899815064397335219503126284591698188403296119474725416062468771000705041465886039073084868932309439700989084547625030234582135098004387654854422994000763949998844062228333673653082509160116002529605430949704657691128800762525616574420089635686717298908405957083717438813057362247840720644972749757581804048388988807520084202967823226243018042121805292717234057825660078770323672712003893086255380094272876373852299698555735296827083105846917093869395749376347706930683775163550316756471209549152680333941331148037066608454193420555106934123675958192962473817479134747374902639157296264900049248007333306660550257197048162003657435172762369519'})
        >>> res.test_result
        'successful'
        """
        try:
            decryptionProof = self.test_data
            pi_prime = generateDecryptionProof(decryptionProof)
            pk_j = mpz(election_data['pk_j'])
            e_bold = generateElgamal(election_data['e_bold'])
            decryption = mpzList(election_data['b_bold_prime_j'])
            secparams= self.election_data['secparams']
            res = CheckDecryptionProof(pi_prime, pk_j, e_bold, decryption, secparams)
            return 'successful' if res else 'failed'
        except KeyError:
            return 'skipped'


if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    dpe_test = DecryptionProofEvidenceTest("1.1","TEST","TEST",["pi_j"])
    dpe_test.election_data = {'secparams': secparams_l3}
    doctest.testmod(extraglobs = {'dpet': dpe_test})
