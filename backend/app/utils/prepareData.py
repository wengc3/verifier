import operator
from functools import reduce

def prepareElectrorateParams(data,func):
    if data:
        return func(data)
    else:
        return 0


def extractValues(matrix,vector_key,item_key):
    dict_list = list()
    for vector in matrix:
        voterId = vector.get('voterId')
        for item in vector.get(vector_key,[]):
            dict_list.append({'voterId': voterId, item_key: item})
    return dict_list


def addKeyToVector(vector,key):
    for index,item in enumerate(vector):
        vector[index]={key:item}
    return vector


def prepareShufleProofs(shuffle_proofs,e_bold,e_prime_bold,secparams):
    try:
        shuffle_proof_list = [{
            'pi_j': shuffle_proofs[0],
            'e_bold': e_bold,
            'e_prime_bold': e_prime_bold[0]}]

        for j in range(secparams.s):
            j = j + 1
            shuffle_proof_list.append({
                'pi_j': shuffle_proofs[j],
                'e_bold': e_prime_bold[j - 1],
                'e_prime_bold': e_prime_bold[j]})

        return shuffle_proof_list
    except IndexError:
        return shuffle_proof_list

def prepareDecryptenProofs(decryption_proofs,publicKeyShares,e_bold,decryptions):
    decryption_proof_list = list()
    for index in range(len(publicKeyShares)):
        decryption_dict = {
            'pi_prime_j': decryption_proofs[index],
            'e_bold' : e_bold,
            'b_bold_prime_j': decryptions[index]
        }
        decryption_dict.update(publicKeyShares[index])
        decryption_proof_list.append(decryption_dict)
    return decryption_proof_list



def prepareData(data_dict,secparams):
    data_dict['secparams'] = secparams
    data_dict['alpha'] = 3
    data_dict['w']=prepareElectrorateParams(data_dict.get('countingCircles'),max)
    data_dict['t']=prepareElectrorateParams(data_dict.get('numberOfCandidates'),len)
    data_dict['Ne']=prepareElectrorateParams(data_dict.get('voters'),len)
    data_dict['s']=prepareElectrorateParams(data_dict.get('partialPublicVotingCredentials'),len)
    data_dict['n']=prepareElectrorateParams(data_dict.get('numberOfCandidates'),sum)
    data_dict['N']=prepareElectrorateParams(data_dict.get('encryptions')[0],len)
    data_dict['k']=prepareElectrorateParams(data_dict.get('numberOfSelections'),sum)
    data_dict['candidates'] = addKeyToVector(data_dict.get('candidates',[]),'C_i')
    data_dict['voters'] = addKeyToVector(data_dict.get('voters',[]),'V_i')
    data_dict['eligibilityMatrix'] = addKeyToVector(data_dict.get('eligibilityMatrix',[]),'e_i',)
    data_dict['countingCircles'] = addKeyToVector(data_dict.get('countingCircles',[]),'w_i')
    data_dict['responses'] = extractValues(data_dict.get('ballots',[]),'responses','beta_j')
    data_dict['publicKeyShares'] = addKeyToVector(data_dict.get('publicKeyShares',[]),'pk_j')
    data_dict['numberOfCandidates'] = addKeyToVector(data_dict.get('numberOfCandidates',[]),'n_j')
    data_dict['numberOfSelections'] = addKeyToVector(data_dict.get('numberOfSelections',[]),'k_j')
    data_dict['partialPublicVotingCredentials'] = addKeyToVector(data_dict.get('partialPublicVotingCredentials',[]),'d_hat_i')
    data_dict['finalizations'] = extractValues(data_dict.get('confirmations',[]),'finalizations','delta_j')
    data_dict['shuffleProofs'] = prepareShufleProofs(
                                data_dict.get('shuffleProofs',[]),
                                data_dict.get('e_bold',[]),
                                data_dict.get('encryptions',[]),secparams
                                )
    data_dict['decryptionProofs'] = prepareDecryptenProofs(
                                data_dict.get('decryptionProofs',[]),
                                data_dict.get('publicKeyShares',[]),
                                data_dict.get('encryptions',[])[-1],
                                data_dict.get('decryptions',[])
                                )
    data_dict['encryptions'] = addKeyToVector(data_dict.get('encryptions',[]),'e_bold_j')
    data_dict['decryptions'] = addKeyToVector(data_dict.get('decryptions',[]),'b_bold_prime_j')
    data_dict['votes'] = addKeyToVector(data_dict.get('votes',[]),'v_i',)
    data_dict['w_bold'] = addKeyToVector(data_dict.get('w_bold',[]),'omega_i',)
    return data_dict
