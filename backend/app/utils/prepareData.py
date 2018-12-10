def prepareElectrorateParams(data,func):
    if data:
        return func(data)
    else:
        return 0


def extractResponsesAndRandomizations(ballots):
    responses = list()
    randomizations = list()
    for item in ballots:
        voterId = item['voterId']

        # prepare responses
        responses.extend(createVectorWithVoterId(
            item.get('responses',[]),
            voterId,
            'beta_j'))

        # prepare randomization
        randomizations.extend(createVectorWithVoterId(
            item.get('randomizations',[]),
            voterId,
            'delta_j'))
    return (responses,randomizations)

def addKeyToVector(vector,key):
    for index,item in enumerate(vector):
        vector[index]={key:item}
    return vector

def createVectorWithVoterId(items,voterId,key):
    vector = list()
    for item in items:
        vector.append({'voterId': voterId, key: item})
    return vector


def prepareData(data_dict,secparams):
    data_dict['secparams'] = secparams
    data_dict['w']=prepareElectrorateParams(data_dict.get('countingCircles'),max)
    data_dict['t']=prepareElectrorateParams(data_dict.get('numberOfCandidates'),len)
    data_dict['Ne']=prepareElectrorateParams(data_dict.get('voters'),len)
    data_dict['s']=prepareElectrorateParams(data_dict.get('partialPublicVotingCredentials'),len)
    data_dict['n']=prepareElectrorateParams(data_dict.get('numberOfCandidates'),sum)
    data_dict['N']=prepareElectrorateParams(data_dict.get('encryptions')[0],len)
    data_dict['responses'], data_dict['randomizations'] = extractResponsesAndRandomizations(data_dict.get('ballots',[]))
    data_dict['publicKeyShares'] = addKeyToVector(data_dict.get('publicKeyShares',[]),'pk_j')
    data_dict['numberOfCandidates'] = addKeyToVector(data_dict.get('numberOfCandidates',[]),'n_j')
    data_dict['numberOfSelections'] = addKeyToVector(data_dict.get('numberOfSelections',[]),'k_j')
    data_dict['partialPublicVotingCredentials'] = addKeyToVector(data_dict.get('partialPublicVotingCredentials',[]),'d_hat_j')
    return data_dict
