// filter function
function filterItems (result, filter) {
  return result.children.filter(function (elem) {
    return filter === elem.value
  })
}

const getDefaultState = () => {
  return {
    categories: [
      {id: 1, title: 'Completness', state: 'idle', value: '', results: []},
      {id: 2, title: 'Integrity', state: 'idle', value: '', results: []},
      {id: 3, title: 'Consistency', state: 'idle', value: '', results: []},
      {id: 4, title: 'Evidence', state: 'idle', value: '', results: []},
      {id: 5, title: 'Authenticity', state: 'idle', value: '', results: []}
    ],
    currentResults: [],
    currentTest: '',
    progress: 0,
    completed: false
  }
}

// initial state
const state = getDefaultState()

// mutations
const mutations = {

  SOCKET_NEWSTATE: (state, data) => {
    let runningState = JSON.parse(data)
    let category = state.categories[Number(runningState.id) - 1]
    category.state = runningState.value
    console.log('newState:', runningState)
    if (runningState.value === 'running') {
      category.value = 'successful'
    }
  },

  SOCKET_CURRENTTEST: (state, title) => {
    state.currentTest = title
    console.log('currentTest:', title)
  },

  SOCKET_ALLRESULTS: (state, data) => {
    let results = JSON.parse(data)
    results.forEach(function (result) {
      state.categories[result.id - 1].results = result.children
    })
    console.log('allResults:', results)
    console.log('categories:', state.categories)
    state.completed = true
  },

  SOCKET_NEWPROGRESS: (state, prg) => {
    state.progress = Number(prg)
    console.log('newProgress:', prg)
  },

  SOCKET_RESULTFAILED: (state, data) => {
    let failedResult = JSON.parse(data)
    state.categories[Number(failedResult.id) - 1].value = failedResult.value
    console.log('resultFailed:', failedResult.id, failedResult.value)
  },

  // testData: function () {
  //   state.categories[0].results = [{'id': '1.1', 'title': 'pre election results', 'results': [{'id': '1.1.1', 'title': 'Check Election ID', 'description': 'Check if ElectionID is in election_data', 'value': 'successful', 'data': {'electionID': '5bc6062b6d19d200125b3fb7'}, 'children': []}, {'id': '1.1.2', 'title': 'Check Number of candidates', 'description': 'Check if vector numberOfCandidates is in election_data', 'value': 'successful', 'data': {'numberOfCandidates': [3]}, 'children': []}, {'id': '1.1.3', 'title': 'Check Candidates', 'description': 'Check if vector candidates is in election_data', 'value': 'successful', 'data': {'candidates': ['Yes', 'No', 'Blank']}, 'children': []}, {'id': '1.1.4', 'title': 'Check Number of selections', 'description': 'Check if vector numberOfSelections is in election_data', 'value': 'successful', 'data': {'numberOfSelections': [1]}, 'children': []}, {'id': '1.1.5', 'title': 'Check Voters', 'description': 'Check if vector voters is in election_data', 'value': 'successful', 'data': {'voters': ['Voter 1', 'Voter 2', 'Voter 3']}, 'children': []}, {'id': '1.1.6', 'title': 'Check CountingCircles', 'description': 'Check if vector countingCircles is in election_data', 'value': 'successful', 'data': {'countingCircles': [1, 1, 1]}, 'children': []}, {'id': '1.1.7', 'title': 'Check Public voting credentials', 'description': 'Check if vector partialPublicVotingCredentials is in election_data', 'value': 'successful', 'data': {'partialPublicVotingCredentials': [[['2203750606489041849508417003814726465144505976531115510880568745982975803365401209753438391719594855197313497652905210656911889709520702705941190351198991803193123516599523847017163156368107603171843070713205379245369402302555901665381563872817563536662377914055165483653681440392423568974937194362763516339398623714276791797309440147512380225777793623813164752357826065012352160749730505087013098988229691528610724139039445469078251398231969156518384374539370008075833185112571994378769148686985731343564587120018665550186455420003714739120354706342840721949488787698281556551513915558498900588657714438872447136752709609191912808942726991366497359566180594997411916553607299125733335336125274140250078298134089870356121301194944055286380536711994196954561775880422442247245956435921943317919874662139791736352879179393731416611249379599096475859989799194423766753405780674382592406177066103157369265725498672534176103096857', '1279044544361874994201766231168647290208833344813213822423573013170174512724519867385915387608600873601727333378985526802572534637637330261974507528567890586302267152155640551236157528442107432814453681141522329698605444368396083878525876574976200404141814057356614355093666032887033216371083606820464555199177667524342272942497975764958226444848450441880009823269018000356417391519709543651916835916825474572095768440922215152379594401740362578230303733118371169085335061390319385059954131591944487128579088350266791010660922649992773293180129976198152732465360980493243763714464317925745775059631932902334049410474021219436555245715332008758883114277283545902798165291852041837430960760159199464155859091158153771958523286553320259003369611565507715405904616529838171869135344419720463191896051455045574089367247657631989059768631371553099491168891462759843815133771154617840840133386444952061081571585263773870590568574441'], ['2121812477152561437640240603393546278879433977200969181612432218009262335121114726081679626729691531612431885266773435999754472799047646014857680123842075131673719526382702064982189495418201153525905153796095550668061363235309569789594916897959822344439708269033905521007521098371007790515069884455195403836577788408462910076763350304333176051835973622611769536148699525021268767592639336176469567425350358397010395857275453931266979413761204198315211501083346142832147554136499389515015494782626500397661315269488945357458653972188201564665305411029005171730786502756190212004988839518460157830119834237610197886348007172234277516354943845454793268455639705817179598591712170481567232428594378669994787127114129830089703233947983984479383962613077264379411350234692615649203623681809752097065673468165381516697745757510228605985342340170160514796068443074292709930424843785596486188398959281648091595162486751670212319355559', '2831857738507820989102731329910663297673941013240528518066962477199454874581448581620172793231126996812876047235691431684850173864766410761004104173617392323219440888048760388487593778668904605727850170002682920434022364943193029666261672837352754814681250537208664847073927400601333414019849205233977474033524294963921411547189643173836054670495476683678771692582856898691313585448425867255943168327800048277373643828347552562018182837928962832566208663972784902401375785098982292480186829778925177390342908768873161921128342384480807436167154548214407283273982468144326926482911475667492458906095207204506172742403316127307788552089581385781507228075346659972727186996549036748808839021279315919081542051910608599542329619658083708104383894319547212664539517182212224349871397739902808711477799315185179810730409716234667949401512814744524388285142578847278527140912230206677203595518368214437682678834668229011045556104150'], ['2443553609226673679255134375963399630281072646604953808760356103802681460641381019542966649388740869761052789881523476611534655774982518811293103116226442499346750140821713232045319694974754866069599253317633888732664488606902256755518890057652620780002784157761342010897486969237413397196533496964131298252497003333749868977591956362761361228964762437846808874300241408712850288165841785917004051138011015596855499320447190264949913160704881189468390695110934095855132795658515179264084425148236466313464052380754692083904932244098388212144227852097272393379671055486556501647350902567564042108701554906396789458130472087891724365322397196137887774389296228093506300252298378487554394930354052797665565050261830719182216427917594553451383093428542181124975447918867037104686784372398060672914388621298696561017093603311502855171998348591075983006240280649819195031376531338431393910359127148326406078689372215788196751030631', '2508801554809587755171224279396425149679581186194621749876544941688033400900636341705120792316180509462381731605528424346181497413484079012612351391249932633975130253702236830682502356448780084440029568734805058117135273348239300389884212032902146225659783921212129794185198387569887401833345424168957459960934931000950358033284971877960107930195282482004332013559930838922312229510951308079659153031493009084503507818952419719970871874728069326618426000259953743889627226759932290228395974176041988252036194531863476405922079458450595637979954655879629873380761285477638245309480694864735995528575475714578647234550055252212776540793971294431610160371998909610511177446484488690542487596573488691445582374434076711644134603936547760036328843734687095293070611576582517152149797401848731472285990485621588778281668504079374540711944010235571623569760368334462002565797089197572291289226848859747757096074218463824295296149752']], [['1565760321085587577072709326155307539960209107037837204018056989428518038166182351382721134004872438800578553820516207633918137637447816566809075796107772881538853554039616886003080963406677532264831934822047618249530634973570165259773206051902736280656000214698329221551052498223923445476589381844657465665017491621133195111847468717082611644815859326998623723637484935306576475930108294296444872348449026988113946645679875396987502397707608769030880389809869247737049676842134975615341962013263689711194777886610409084530424605792594040163342758730469271077056633963381836061799515849680877033236569528086606152439434952620652307220900330467630679890618112218115636980204610089398370583685030271292673006221564435507930054989485428855048581061558051963451553309700977765221980187379305150331361182973994037072601389798131777534249543685733630953268728081990303254232942430621190994807521788773697270653398468205576260784944', '3344639193832209554952198346193025768499607157424919785061619499896028837556193629097503929111188859088671526865702890164947466470584737502687759389974731997624511808363813131312544662871706224696260912690781220029087764524895739415059648027699630292381478544648892234066663651942526575470317616946051182532834763239612300211781883283499682954803854808347144297592424674757533270595016980613828335495415107709050115903020494528942652708262124313837948571001749732882669843689329970593635418589805423631297022144842877339664068496710149840718316228979684743677154894659890979262302984023245663704179344706831057234946161465413989670029635171314506287283578056886113180492739280207751845911251724558864486599101045549402505305420676160722271286413698427900644219864664757192959821591611324339458276896956634995238026375257672887284334206882899477368797576976143943439584318350287525397207997637217873507217818151620538709806'], ['2516035363288525795235871790432172135431692083819238001568273758523983221862980755132218277999668983329219246261425977279809395416066068754669018485878178557151573077050896625793021962597658245337822144549177430233684763225226616146218867970957302190272398690593216812934103449957285934697009221669454132882443164990569657806116586377420246420006736977910591399405288980030748307312423674691288926438253400036716374424298084486265601918210574129091870975085476110481980828543059573018294348325663159960121395399720541056651514556509281798897604373739689725828008771837958906927974167802999807185239804408216576563382786437910880972699452145583161587829421177093650879613826422067207297503382164071174794472874779249354492014106221888869998674737350362429430537127933877447536048026953293267298135647760505145132434188214622664059622040399060102568923791328029135728663498752513065515883601546581465106883236028362889752240373', '3597099963989309468923374112228938917265278432525324248621599683995568059297155849682502520765345484531338560365469195490011476537899173883931099132195283747974909019865996242577243369817752980309813091893094994430623399853643965560709141864591508261826858997166195856718805935858462265717708773416922087098991718799955925362285475697564097078662974856278965542459112695295959415445431366949497085688043840549975317766111051542234080910822543338403960049456809484465296484222858182890367912672202213129129705471601667901968878415395104846694969571885706294423405947504045194716685930131123761383651911932153173878621982845777379612569288442705102493694663412112145533661836539869700997805089386663269506988942434862336107247144409508271735871866419669509191802881929697496735350233811615645043741736697798913227439626559009875013775103955618512590390105479877289448487860836843700080627996449914975265146343113299567908331913'], ['3923761655091668227287987081608327554751854344266474744581239293733165074713570006709851059247040971439748168257387817928925776019114425067779793268088466733693672485030032967526842571027078523657730660550169445502597406714971986009010082375896697532712809289004161026073902120861460629769886669573466804438190277246305629194098703887038809504364411622340293908609853173133301295840891029472358443256448334540599911740448684031371657005092558687459544764603101194763260839747085978379714176970916594154321621843903791772192393189612068561832337265458293923607607601363626434758170672703201150923307044243190827600731304823549914979432707785481916632119791265926797281640995878189640574514897845350939731790464124675736363953679249098177972343207128896283419767331732922929767353652162805871581667329172224126746596034955572654249089335716876367252909348447019262141915688502061733197362430532443801934664956163233913796079963', '1456303302892140580345401683659286567489399086507075098061244522303855169508667701315853902122461244497392871576047136100607774213709278098098440493787658137564346794988093142801396215320263423834392342920559482430626684412845822319879787838992378802673003501416904099896761170371962021745235152874432420208953215665985812100750785748013451372081375593175278018338880615408094615759450538809185597087101870333432086462899120037824193886949948914560439161751235728716346314638735537134013304563879952206573774779118113741453483145109835798383725514300058945521624706318953127925422270352106324776817621450055360623239061839748079018298971668086903573723128209672607486057174750239597114504941918000642142111926456536054784719995467299195043400628417801368302547963305763957752283143018220127201848144067849424007850018852603345797758777559938960252985829540962955748367151166719447981461529336787737050776209579492825999995404']], [['3565724394447858151013366275922391713862565396744730101164262273214787726775287756212210381135444227794934793213991156502928322529926996754595381093040389545755343061249584034049926773453042826557252980613101165613801198133233490830802509593121011327532803870674772695868628799297661628079003147242554826393917228796381287199253190745641883821272823248510454353245762775026859100502206861379948518913556486997672170034013857539085695511112818575313383530596956036169140438599672907778890254540922468343818993067422157120297161510922880818460096761611920198053890079453243425218564629963867181002767674610614699385804926167562880009055585573014637640859265079507595851326919505503949935724067740231081591692912084051598528873375428961960447915482880114839997511099692640634216307361278815996902083450311228475701000378314204236598698792978484987833152986452142732330133301359669063380668922908787428300474942004997724997901554', '385541578961651110468026028396327365344565847295854282450804131928256266129517712539288924581683118522715682957416779840916415752949067436434651152767103860447299501139786262745856718549082471538424573092950058532209867704527377508907921461698142252396667820009241432362388474703170115263406751388139230236681936085708708462739427264636780781624052697063297543361068444668358753094089006187280182193965322620191688937320085573664963808073345157596013896799155153182826807623929949372485695846961392111689462001187872677299038957004928890091655692084824827059696493300011752845938529044632476536717499296291920502441119616328697783446928765328302441561023179208822016104628443717532121285497170401360024335599046031385593545409965615709711292250604354728660385905958989476856467040833088147719123930909309742629256264391292751285121266185893094093497077967469689471140545803843783854630344544749067851291478484106305360605942'], ['1000937643215427747361846155329759113149835382167166815949881594493822999269525494530975130893283854536796652065551306260898542964084604209134481627063124165932332527342444323090029177708269635727269468402968910908309282485530225409697174472765422407191925254880727411187222865446149874195794879185204811464778952089149807741972001472232527661965321826650764320259728945961763559319226521606960388308079643671615483231981538571497322319184967618815693994063096450182494232113917367055064896924333545250309684955845794324576866482227953281357977109059642046026544031839633439263570197852830095616958058053339298239022417502259565108210705509900978740248596649551626486973646877839290161175276985965410348706188556395914898514581552651846708103372574738531351685743024847770990384324810322364974395633192342535427297474156065124160847867300447116056041342771968572203276019322786997126409474074236418906081713607403459636009160', '2419102378162688829945014540350160089280444902036852625261917146376000594067701309694369979704893245797771196805434531699726219093380706367394498233038237075136360465660991238594852486616592399820054572281039211481050316666770469799679386350186415656889720868535307899551224711492541651887604209242595099373258231299887753520412246114839171363285684498189463445865906935629820388967332962017227821383003060577355875976240890448638979828798244095001545663614373303025570190600809327281232830615499931410412030311257871407715446834664963779872688884974926040014979012786290376692070086118858182334829214800584492530788445686533268398858488070482499620326919914835879587121518693883160271660988676508255960715384682033719800913239344392298866007356271973922819272813965741216244967395584977862320891249414520912598222004875876860912576325181130418374560046156015392925783141133202704821845190374608127738965848127046380605114356'], ['2561849056791614960107436575937215982070879897018853837620436116124424966237314541815795257634175578907923784235126505162767158146303415126306331747401385779309021633661849029707739946093566723114467263246784539725534331796507461557331747059987875591488303272240121578000310714698691391192302843974513028371633633764387565382721083762574033737752472803311227573301783693104504479191243372549917641280524137118307087811079235186682735460803497024609628745882532370663600631168869386574509931585309628412252827892964455883123327634520616479458898121993338496876586366440868182447127432637090016786522192465227268225724710265498521701156667262743913525914578821789687674640392272421170330889082090362418472866989887122068161794508209848428215313350763351880333687629953920784348091362732653395951754784498554535291338420361920695744422943256559996506524477788437684034916542467663371632325899938615707494528873078626060095410710', '3413409190925992346482883968870933076374212134941946306576801606130309094899313146242889957463027981343377552949985334082228931380397124380083845193653516373924350603358210479441851527384659478719061522620886605754954938524500509833476454219381816538366270260265729508282511062660300002605282846253483274562837748162605480458191842082966720473900120008824170180753821569253010149758920217265147239478311553011919384466700556210380745512989731007831110107198672325282454437657858087629014041244264808840799902770358101280896487602328097756023337173836865123561040126569631259808944831544552237233766747015781353697109378638356523990750111627428292657280115722669600261736289657956853733317626986769045476506891856901245056522843101688883576431181007326176108626203120546423870826749525103840446648545616042573828483584117682605096063759150265859246896904996706947083342015161993168099576668183828403087422299483766709441478218']]]}, 'children': []}]}, {'id': '1.2', 'title': 'election results', 'results': [{'id': '1.2.1', 'title': 'For all Ballots: Check Voter ID', 'description': 'For all ballots check if they have a voterID ', 'value': 'successful', 'data': null, 'children': [{'id': '1.2.1.1', 'title': 'Check Voter ID', 'description': 'For all ballots check if they have a voterID ', 'value': 'successful', 'data': {'voterId': 0}, 'children': []}, {'id': '1.2.1.2', 'title': 'Check Voter ID', 'description': 'For all ballots check if they have a voterID ', 'value': 'successful', 'data': {'voterId': 1}, 'children': []}, {'id': '1.2.1.3', 'title': 'Check Voter ID', 'description': 'For all ballots check if they have a voterID ', 'value': 'successful', 'data': {'voterId': 2}, 'children': []}]}]}]
  // },

  calcResult: function (state, payload) {
    state.currentResults = []
    let results = JSON.parse(JSON.stringify(state.categories[payload.id - 1].results)) // a coppy of results
    // let results = state.categories[payload.id - 1].results
    if (payload.filter === 'all') {
      state.currentResults = results
    } else {
      results.forEach(function (elem) {
        elem.children = filterItems(elem, payload.filter)
        if (elem.children.length > 0) {
          state.currentResults.push(elem)
        }
      })
    }
  },
  resetState: function (state) {
    Object.assign(state, getDefaultState())
  }
}

export default {
  state,
  mutations
}
