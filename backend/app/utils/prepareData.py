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
        for response in item['responses']:
            responses.append({'voterId': voterId,'beta_j': response})
        for randomization in item['randomizations']:
            randomizations.append({'voterId': voterId,'delta_j': randomization})
    return (responses,randomizations)

def addKeyToVector(vector,key):
    for index,item in enumerate(vector):
        vector[index]={key:item}
    return vector

def prepareData(data_dict,secparams):
    data_dict['secparams'] = secparams
    data_dict['w']=prepareElectrorateParams(data_dict['countingCircles'],max)
    data_dict['t']=prepareElectrorateParams(data_dict['numberOfCandidates'],len)
    data_dict['Ne']=prepareElectrorateParams(data_dict['voters'],len)
    data_dict['s']=prepareElectrorateParams(data_dict['partialPublicVotingCredentials'],len)
    data_dict['n']=prepareElectrorateParams(data_dict['numberOfCandidates'],sum)
    data_dict['N']=prepareElectrorateParams(data_dict['encryptions'][0],len)
    data_dict['responses'], data_dict['randomizations'] = extractResponsesAndRandomizations(data_dict['ballots'])
    data_dict['publicKeyShares'] = addKeyToVector(data_dict['publicKeyShares'],'pk_j')
    data_dict['numberOfCandidates'] = addKeyToVector(data_dict['numberOfCandidates'],'n_j')
    data_dict['numberOfSelections'] = addKeyToVector(data_dict['numberOfSelections'],'k_j')
    data_dict['partialPublicVotingCredentials'] = addKeyToVector(data_dict['partialPublicVotingCredentials'],'d_hat_j')
    return data_dict
