import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

from chvote.verifier.IntegrityTests.multiMathGroupeHelper import multiMathGroupeHelper

class PublicVotingCredentialIntegrityTest(SingleTest):
    """docstring for PublicVotingCredentialIntegrityTest."""

    @completness_decorate()
    def runTest(self,election_data):
        """
        Test if x_j,y_j is in G_q_hat
        >>> res = pvcit.runTest({'d_hat_i': [['10729722235944325116265925487240351218108066854272454570275986057971857440212362366387286540590242025229488950774004015883323608514429060218566527330370220337766212627504421500361939783530728713302949139931928368454826547144576626874326282472131594410286247630327282331564261574365253922044764793815526821369387502716327641478337598515846158878373256817417737368556077672274845509023292018798959766908609004182711437188847083594026377930322994611276291547370838820231537292584230330094413072421643747911593385217989636534058870393124682411414913832592733196457930724963597528512647963405757077955416910093477115445879779398469104779234126872084151022203700713382625237370790617929059595149375318182799872820822416352656165389901314440611479590788828223419876066275356606938422612279298823843774164297156463472357837879208389962048985821802465122687584615471781773574910747606692466916007985152813521822163093623945019953655', '2575203165450752312745397201322418337662420404996904691712111171548464147564941889328993977132258194891537600540304559801747881796123341269384380455473131374947298526835619311802259660622013068428168991681304173072125713955932314709602795638841916296916041243711862610211202466059353044021405944161015759539888746383768566065947139303047574011165867013638423489894877719755046795581766063473048552099547801494071463960067167430130488812739128662367043638871524596182279767968668384856430686224913969990127266806467380585568168685661842473908974450492727627455993582079388037878031437900299003250013539500540305897232603802419603361430554010924747212068308957418607513992128696263497620468010641243871868628933717647597773093956860629572288799818043303506754509966977093384172775309491843026532187383702690991762761424149233031275718549313766353945915226041150797319038449609631092899794967332042572112462940383367396620910559'], ['420298681269036825962565103431545199556875700824682900390195690293384500616093238492470333516718147009778388158618634947862954817566003095977274612118411780299515768385091416902116745375230553603188749568272336249281251680743426956152308798866332934181173831240802760856366597504795038384234636823493494248279723296141362084679950499245171973335695904746744371708952924014522282863390956588875557872170125338646893010342610918960970689090194196102197592043800211196375472653336576524129600327138547312538788874853701172205034563911792924318307616465580551761196995733529401420558867554691054456766033117035987685610697748236180306637322682922869897624742019723137632708265614931258207801495703288730948899975073423222062190612653152071746636754960440786801503522725815429600990945960251383264184766098048273458436423249027138527657398416533656136320601998939903931777923639156019537009313094075062326727712281118016686416176', '935418298427977703383712788322807185872769492711391146435618782120242952160192389418378560734199389181363483792055961756404768418966029967855519099796026869905741746183102712327039794152964040259016713555136829774080160528655133737847264965275049944286036926570091635734603695718036923015030952226152698907081670388324568947981062409132801446914019057215439212089425055532809231599974516903232144877917387698422360473780279518175667627844779975014792050018584647425903107028150898886526410743593412687916120168129438112481731042630868226246780739782068342017893885472954492319313738272792049841175147212183174417792560717689113652745611741783903919470128746345701530406623616836163122280234904000052530902374299829056159713545210358492840964484631000994692072994726530189944452521153883990792989736920187719864020834322820969237046773806072226801326232485394338348461457055491471052342796719729985387461500288674514780162708'], ['3853732774341815637505271454632876426518106856544904941581114767206486669573544954867538725261407615087537959012189192926737592514292289834370307297429260359423291776288138836837822620142233103852071864715588880544374730208386090585587288689128990469332144190411728529343036734255545116596133644660129821643915173075431432252549859966815893774213530733226162725051169221842017146481997226074078797933794764199940408117911763924510191256860904003807963383709577798259950915422903633185163290111453850037197070693234110979294669794597452542451102380808446737179146145111281529226619913535853894958983163076986786537469696377000939566014534670718462624177561044967329003068106244032241428896320683473341624369467645748806366493179837597431375730446325579013837034348810138615798962090389162172170310275922453235873767337618326546598287943784699453764077973769845111057531542125620665264257566852926775400125769472482671258147432', '331897573396037741997076445917325928338561184507193824153147940978603093778489314358059334389255984760569984650254175930004928989233635411562950086031785700131952650697420286968398993569885734233586517537112330338528047746686087963980592237433360368130490995529012436018719913171819911383085810719583360735247482426061458755569690704960084761925934909512776147963628397945311115821627114345645215730097759929265280916023588385189222178550317728347706055525165951717955842179395996557112004245247714360764488725204411637274259061399308523692757613309383036500578226784889479516000707415287662152386756311250154499214918405634182102931935234520513348818756272708862962433333826773069724379579958676201889349618099213147395099416520927340538648350061593317939598125179528308387048805541735116886697649549904740882264431947726945513248583705138207005261966692996923304281586305648193997913510776664626347487977365964466857056103']]})
        >>> res.test_result
        'successful'
        >>> res = pvcit.runTest({'d_hat_i': [['10729722235944325116265925487240351218108066854272454570275986057971857440212362366387286540590242025229488950774004015883323608514429060218566527330370220337766212627504421500361939783530728713302949139931928368454826547144576626874326282472131594410286247630327282331564261574365253922044764793815526821369387502716327641478337598515846158878373256817417737368556077672274845509023292018798959766908609004182711437188847083594026377930322994611276291547370838820231537292584230330094413072421643747911593385217989636534058870393124682411414913832592733196457930724963597528512647963405757077955416910093477115445879779398469104779234126872084151022203700713382625237370790617929059595149375318182799872820822416352656165389901314440611479590788828223419876066275356606938422612279298823843774164297156463472357837879208389962048985821802465122687584615471781773574910747606692466916007985152813521822163093623945019953655', '2575203165450752312745397201322418337662420404996904691712111171548464147564941889328993977132258194891537600540304559801747881796123341269384380455473131374947298526835619311802259660622013068428168991681304173072125713955932314709602795638841916296916041243711862610211202466059353044021405944161015759539888746383768566065947139303047574011165867013638423489894877719755046795581766063473048552099547801494071463960067167430130488812739128662367043638871524596182279767968668384856430686224913969990127266806467380585568168685661842473908974450492727627455993582079388037878031437900299003250013539500540305897232603802419603361430554010924747212068308957418607513992128696263497620468010641243871868628933717647597773093956860629572288799818043303506754509966977093384172775309491843026532187383702690991762761424149233031275718549313766353945915226041150797319038449609631092899794967332042572112462940383367396620910559'], ['420298681269036825962565103431545199556875700824682900390195690293384500616093238492470333516718147009778388158618634947862954817566003095977274612118411780299515768385091416902116745375230553603188749568272336249281251680743426956152308798866332934181173831240802760856366597504795038384234636823493494248279723296141362084679950499245171973335695904746744371708952924014522282863390956588875557872170125338646893010342610918960970689090194196102197592043800211196375472653336576524129600327138547312538788874853701172205034563911792924318307616465580551761196995733529401420558867554691054456766033117035987685610697748236180306637322682922869897624742019723137632708265614931258207801495703288730948899975073423222062190612653152071746636754960440786801503522725815429600990945960251383264184766098048273458436423249027138527657398416533656136320601998939903931777923639156019537009313094075062326727712281118016686416176', '935418298427977703383712788322807185872769492711391146435618782120242952160192389418378560734199389181363483792055961756404768418966029967855519099796026869905741746183102712327039794152964040259016713555136829774080160528655133737847264965275049944286036926570091635734603695718036923015030952226152698907081670388324568947981062409132801446914019057215439212089425055532809231599974516903232144877917387698422360473780279518175667627844779975014792050018584647425903107028150898886526410743593412687916120168129438112481731042630868226246780739782068342017893885472954492319313738272792049841175147212183174417792560717689113652745611741783903919470128746345701530406623616836163122280234904000052530902374299829056159713545210358492840964484631000994692072994726530189944452521153883990792989736920187719864020834322820969237046773806072226801326232485394338348461457055491471052342796719729985387461500288674514780162708'], ['3853732774341815637505271454632876426518106856544904941581114767206486669573544954867538725261407615087537959012189192926737592514292289834370307297429260359423291776288138836837822620142233103852071864715588880544374730208386090585587288689128990469332144190411728529343036734255545116596133644660129821643915173075431432252549859966815893774213530733226162725051169221842017146481997226074078797933794764199940408117911763924510191256860904003807963383709577798259950915422903633185163290111453850037197070693234110979294669794597452542451102380808446737179146145111281529226619913535853894958983163076986786537469696377000939566014534670718462624177561044967329003068106244032241428896320683473341624369467645748806366493179837597431375730446325579013837034348810138615798962090389162172170310275922453235873767337618326546598287943784699453764077973769845111057531542125620665264257566852926775400125769472482671258147432']]})
        >>> res.test_result
        'failed'
        >>> res = pvcit.runTest({'d_hat_i': [['10729722235944325116265925487240351218108066854272454570275986057971857440212362366387286540590242025229488950774004015883323608514429060218566527330370220337766212627504421500361939783530728713302949139931928368454826547144576626874326282472131594410286247630327282331564261574365253922044764793815526821369387502716327641478337598515846158878373256817417737368556077672274845509023292018798959766908609004182711437188847083594026377930322994611276291547370838820231537292584230330094413072421643747911593385217989636534058870393124682411414913832592733196457930724963597528512647963405757077955416910093477115445879779398469104779234126872084151022203700713382625237370790617929059595149375318182799872820822416352656165389901314440611479590788828223419876066275356606938422612279298823843774164297156463472357837879208389962048985821802465122687584615471781773574910747606692466916007985152813521822163093623945019953655', '2575203165450752312745397201322418337662420404996904691712111171548464147564941889328993977132258194891537600540304559801747881796123341269384380455473131374947298526835619311802259660622013068428168991681304173072125713955932314709602795638841916296916041243711862610211202466059353044021405944161015759539888746383768566065947139303047574011165867013638423489894877719755046795581766063473048552099547801494071463960067167430130488812739128662367043638871524596182279767968668384856430686224913969990127266806467380585568168685661842473908974450492727627455993582079388037878031437900299003250013539500540305897232603802419603361430554010924747212068308957418607513992128696263497620468010641243871868628933717647597773093956860629572288799818043303506754509966977093384172775309491843026532187383702690991762761424149233031275718549313766353945915226041150797319038449609631092899794967332042572112462940383367396620910559'], ['420298681269036825962565103431545199556875700824682900390195690293384500616093238492470333516718147009778388158618634947862954817566003095977274612118411780299515768385091416902116745375230553603188749568272336249281251680743426956152308798866332934181173831240802760856366597504795038384234636823493494248279723296141362084679950499245171973335695904746744371708952924014522282863390956588875557872170125338646893010342610918960970689090194196102197592043800211196375472653336576524129600327138547312538788874853701172205034563911792924318307616465580551761196995733529401420558867554691054456766033117035987685610697748236180306637322682922869897624742019723137632708265614931258207801495703288730948899975073423222062190612653152071746636754960440786801503522725815429600990945960251383264184766098048273458436423249027138527657398416533656136320601998939903931777923639156019537009313094075062326727712281118016686416176', '935418298427977703383712788322807185872769492711391146435618782120242952160192389418378560734199389181363483792055961756404768418966029967855519099796026869905741746183102712327039794152964040259016713555136829774080160528655133737847264965275049944286036926570091635734603695718036923015030952226152698907081670388324568947981062409132801446914019057215439212089425055532809231599974516903232144877917387698422360473780279518175667627844779975014792050018584647425903107028150898886526410743593412687916120168129438112481731042630868226246780739782068342017893885472954492319313738272792049841175147212183174417792560717689113652745611741783903919470128746345701530406623616836163122280234904000052530902374299829056159713545210358492840964484631000994692072994726530189944452521153883990792989736920187719864020834322820969237046773806072226801326232485394338348461457055491471052342796719729985387461500288674514780162708']]})
        >>> res.test_result
        'failed'
        """
        try:
            vector = self.test_data
            param = self.election_data['secparams']
            rng = self.election_data['N']
            res = 'successful'
            self.test_result.addTestData('N',rng)
            self.test_result.addTestData('p_hat',param.p_hat)
            for i in range(rng):
                if not multiMathGroupeHelper(vector[i],2,param.p_hat):
                    res = 'failed'
            return res
        except IndexError:
            return 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    pvci_test = PublicVotingCredentialIntegrityTest("1.1","TEST","TEST",["d_hat_i"])
    pvci_test.election_data = {'secparams': secparams_l3, 'N':3}
    doctest.testmod(extraglobs={'pvcit': pvci_test})
