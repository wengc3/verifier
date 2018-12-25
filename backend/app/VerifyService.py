from gmpy2 import mpz
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# for urlencoded
import os, sys
import pickle
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.utils.prepareData import prepareData
from chvote.Common.SecurityParams import secparams_l1, secparams_l2, secparams_l3
from chvote.verifier.Test import Test
from chvote.verifier.TestResult import TestResult
from chvote.verifier.MultiTest import MultiTest
from chvote.verifier.IterationTest import IterationTest

from chvote.verifier.CompletnessTest import SingleCompletnessTest
from chvote.verifier.IntegrityTests.BiggerThanIntegrityTest import BiggerThanIntegrityTest
from chvote.verifier.IntegrityTests.BallotProofIntegrityTest import BallotProofIntegrityTest
from chvote.verifier.IntegrityTests.MatrixBitIntegrityTest import MatrixBitIntegrityTest
from chvote.verifier.IntegrityTests.EligibilityMatrixIntegrityTest import EligibilityMatrixIntegrityTest
from chvote.verifier.IntegrityTests.InRangeIntegrityTest import InRangeIntegrityTest
from chvote.verifier.IntegrityTests.MathGroupeIntegritiyTest import MathGroupeIntegritiyTest
from chvote.verifier.IntegrityTests.PublicVotingCredentialIntegrityTest import PublicVotingCredentialIntegrityTest
from chvote.verifier.IntegrityTests.EncrypdetSelectionIntegrityTest import EncrypdetSelectionIntegrityTest
from chvote.verifier.IntegrityTests.SignaturIntegrityTest import SignaturIntegrityTest
from chvote.verifier.IntegrityTests.StringIntegrityTest import StringIntegrityTest
from chvote.verifier.IntegrityTests.OTResponseIntegrityTest import OTResponseIntegrityTest
from chvote.verifier.IntegrityTests.ConfProofIntegrityTest import ConfProofIntegrityTest
from chvote.verifier.IntegrityTests.FinalizationIntegrityTest import FinalizationIntegrityTest
from chvote.verifier.IntegrityTests.EncryptionIntegrityTest import EncryptionIntegrityTest
from chvote.verifier.IntegrityTests.ShuffleProofIntegrityTest import ShuffleProofIntegrityTest
from chvote.verifier.IntegrityTests.DecryptionIntegrityTest import DecryptionIntegrityTest
from chvote.verifier.IntegrityTests.DecryptionProofIntegrityTest import DecryptionProofIntegrityTest

from chvote.verifier.ConsistencyTests.VectorLengthConsistenyTest import VectorLengthConsistenyTest
from chvote.verifier.ConsistencyTests.MatrixLengthConsistenyTest import MatrixLengthConsistenyTest
from chvote.verifier.ConsistencyTests.PrimeConsistencyTest import PrimeConsistencyTest
from chvote.verifier.ConsistencyTests.VectorItemsConsistenyTest import VectorItemsConsistenyTest

from chvote.verifier.EvidenceTests.BallotProofEvidenceTest import BallotProofEvidenceTest
from chvote.verifier.EvidenceTests.ConfirmationProofEvidenceTest import ConfirmationProofEvidenceTest
from chvote.verifier.EvidenceTests.DecryptionProofEvidenceTest import DecryptionProofEvidenceTest
from chvote.verifier.EvidenceTests.ShuffleProofEveidenceTest import ShuffleProofEveidenceTest

from chvote.verifier.AuthenticityTest import CertificateAuthenticityTest, SignaturAuthenticityTest

class VerifyService(object):
    """docstring for VerifyService."""
        # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if VerifyService.__instance == None:
            VerifyService()
        return VerifyService.__instance

    def __init__(self):
        """ Check if an instance is already created """
        if VerifyService.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            VerifyService.__instance = self
            self.root_test = MultiTest("0:","Root Test","Test which conntains all Tests")
            self.setUpTests()

    def setUpTests(self):
        completness_tests = MultiTest("1","Completness Tests","Test which conntains all completness tests")
        # 1.1 pre election
        com_pre_election_tests = MultiTest("1.1","Pre Election Tests","Test which conntains all pre_election tests")
        com_pre_election_tests.addTests(
            SingleCompletnessTest("1.1.1","Check Election ID","Check if ElectionID is in election_data",['electionID']),
            SingleCompletnessTest("1.1.2","Check Number of candidates","Check if vector numberOfCandidates is in election_data",['numberOfCandidates']),
            SingleCompletnessTest("1.1.3","Check Candidates","Check if vector candidates is in election_data",['candidates']),
            SingleCompletnessTest("1.1.4","Check Number of selections","Check if vector numberOfSelections is in election_data",['numberOfSelections']),
            SingleCompletnessTest("1.1.5","Check Voters","Check if vector voters is in election_data",['voters']),
            SingleCompletnessTest("1.1.6","Check CountingCircles","Check if vector countingCircles is in election_data",['countingCircles']),
            SingleCompletnessTest("1.1.7","Check EligibilityMatrix","Check if eligibilityMatrix is in election_data",['eligibilityMatrix']),
            SingleCompletnessTest("1.1.8","Check Public voting credentials","Check if vector partialPublicVotingCredentials is in election_data",['partialPublicVotingCredentials']),
            SingleCompletnessTest("1.1.9","Check Public keys","Check if vector publicKeyShares is in election_data",['publicKeyShares']),
            SingleCompletnessTest("1.1.10","Check Full Signatur","Check if Signatur of full election parameters is in election_data",['sigParam1']),
            SingleCompletnessTest("1.1.11","Check Partial Signatur","Check if Signatur of part of election parameters is in election_data",['sigParam2']),
            SingleCompletnessTest("1.1.12","Check other part Signatur","Check if Signatur of  other part of election parameters is in election_data",['sigParam3']),
            SingleCompletnessTest("1.1.13","Check Public credentials Signatur","Check if vector of Signatur of Public credentials is in election_data",['sigPrep']),
            SingleCompletnessTest("1.1.14","Check Public keys Signatur","Check if vector of Signatur of Public keys is in election_data",['sigKgen'])
        )
        # 1.2 election
        com_election_tests = MultiTest("1.2","Election Tests","Test which conntains all election tests")
        com_multi_test_ballot = MultiTest("1.2.2.0","Ballot Tests","Test which conntains all ballot tests")
        com_multi_test_ballot.addTests(
            SingleCompletnessTest("1.2.2.1.0","Check Voter ID","Check if voterId is in VoterBallot",['voterId']),
            SingleCompletnessTest("1.2.2.2.0","Check Ballot","Check if ballot is in VoterBallot",['ballot'])
        )
        com_multi_test_resbonse = MultiTest("1.2.4.0","Response Tests","Test which conntains all response tests")
        com_multi_test_resbonse.addTests(
            SingleCompletnessTest("1.2.4.1.0","Check Voter ID","Check if voterId is in response_dict",['voterId']),
            SingleCompletnessTest("1.2.4.2.0","Check OT-Responses","Check if vector OT-Responses is in response_dict",['beta_j']),
            SingleCompletnessTest("1.2.4.3.0","Check OT-Signatur","Check if OT-Signatur is in response_dict",['sigCast'])
        )
        com_multi_test_confirmation = MultiTest("1.2.6.0","Confirmation Tests","Test which conntains all confirmation tests")
        com_multi_test_confirmation.addTests(
            SingleCompletnessTest("1.2.6.1.0","Check Voter ID","Check if voterId is in confirmation_dict",['voterId']),
            SingleCompletnessTest("1.2.6.2.0","Check Confirmation","Check if confirmation is in confirmation_dict",['confirmation'])
        )
        com_multi_test_finalization = MultiTest("1.2.8.0","Finalization Tests","Test which conntains all finalization tests")
        com_multi_test_finalization.addTests(
            SingleCompletnessTest("1.2.8.1.0","Check Voter ID","Check if voterId is in finalization_dict",['voterId']),
            SingleCompletnessTest("1.2.8.2.0","Check Finalization","Check if finalization is in finalization_dict",['delta_j']),
            SingleCompletnessTest("1.2.8.3.0","Check Finalization-Signatur","Check if Finalization-Signatur is in finalization_dict",['sigConf'])
        )
        com_election_tests.addTests(
            SingleCompletnessTest("1.2.1","Check Ballots","Check if vector ballots is in election_data",['ballots']),
            IterationTest(['ballots'],"For all elements Ballots: ",com_multi_test_ballot,'Ne'),
            SingleCompletnessTest("1.2.3","Check Responses","Check if vector responses is in election_data",['responses']),
            IterationTest(['responses'],"For all elements in responses: ",com_multi_test_resbonse,'Ne'),
            SingleCompletnessTest("1.2.5","Check Confirmations","Check if vector confirmations is in election_data",['confirmations']),
            IterationTest(['confirmations'],"For all elements in confirmations: ",com_multi_test_confirmation,'Ne'),
            SingleCompletnessTest("1.2.7","Check Finalization","Check if vector finalization_list is in election_data",['finalizations']),
            IterationTest(['finalizations'],"For all elements in finalization: ",com_multi_test_finalization,'Ne'),
        )
        # 1.3 post_election
        com_post_election_tests = MultiTest("1.3","Post Election Tests","Test which conntains all post_election tests")
        com_post_election_tests.addTests(
            SingleCompletnessTest("1.3.1","Check Encryptions","Check if vector of mixed an encrypted ballot is in election_data",['encryptions']),
            SingleCompletnessTest("1.3.2","Check Shuffel Proofs","Check if vector of Shuffel Proofs is in election_data",['shuffleProofs']),
            SingleCompletnessTest("1.3.3","Check Decryptions","Check if vector of partial decrypted ballots is in election_data",['decryptions']),
            SingleCompletnessTest("1.3.4","Check Decryption Proofs","Check if vector of decryption Proofs is in election_data",['decryptionProofs']),
            SingleCompletnessTest("1.3.5","Check Election Result","Check if matrix of election result is in election_data",['votes']),
            SingleCompletnessTest("1.3.6","Check Counting Circles","Check if matrix of counting Circle is in election_data",['w_bold']),
            SingleCompletnessTest("1.3.7","Check Tallying Signatur","Check if tallying signatur is in election_data",['sigTally']),
            SingleCompletnessTest("1.3.8","Check Mixing Signatur","Check if mixing signatur is in election_data",['sigMix']),
            SingleCompletnessTest("1.3.9","Check Decryption Signatur","Check if decryption signatur is in election_data",['sigDec']),
        )
        completness_tests.addTests(com_pre_election_tests,com_election_tests,com_post_election_tests)
        # 2. Integrity Tests
        integrity_tests = MultiTest("2","Integrity Tests","Test which conntains all integrity tests")
        # 2.1 pre_election Tests
        int_pre_election_tests = MultiTest("2.1","Pre Election Tests","Test which conntains all pre_election tests")
        # Tests for IterationTests
        int_test_numberOfCandidates = BiggerThanIntegrityTest("2.1.6.0","Check NumberOfCandidates","Check if n_j >= 2",['n_j'],2)
        int_test_numberOfSelections = BiggerThanIntegrityTest("2.1.7.0","Check NumberOfSelections","Check if k_j >= 1",['k_j'],1)
        int_multi_test_eligibilityMatrix = MultiTest("2.1.8.0","Check EligibilityMatrix","Test which conntains all eligibilityMatrix tests")
        int_multi_test_eligibilityMatrix.addTests(
            MatrixBitIntegrityTest("2.1.8.1.0","Check EligibilityMatrix Bit","Check if e_ij in [0,1]",['e_i'],'t'),
            EligibilityMatrixIntegrityTest("2.1.8.2.0","Check EligibilityMatrix Vector ","Check if sum(e_ij) >= 1",["e_i"])
            )
        int_test_candidate = StringIntegrityTest("2.1.9.0", "Check Candidate","Check if Candidate is in A*_ucs",["C_i"])
        int_test_voter = StringIntegrityTest("2.1.10.0", "Check Voter","Check if Voter is in A*_ucs",["V_i"])
        int_test_countingCircle = InRangeIntegrityTest("2.1.11.0", "Check CountingCircle","Check if w_i in {1,...,w}",["w_i"],1,"w")
        int_test_pubc = PublicVotingCredentialIntegrityTest("2.1.12.0", "Check PublicVotingCredential","Check if d_hat_ij in G_q_hat^2",["d_hat_i"])
        int_test_pk = MathGroupeIntegritiyTest("2.1.13.0","Check Public key","For all authority test it's Public key",['pk_j'],'p')
        int_test_sigPrep = SignaturIntegrityTest("2.1.17.0","Check PublicVotingCredential Signatur","Check if sigPrep_j in Bit x Z_q",["sigPrep_j"])
        int_test_sigKgen = SignaturIntegrityTest("2.1.18.0","Check PublicVoting Key Signatur","Check if sigKgen_j in Bit x Z_q",["sigKgen_j"])
        int_pre_election_tests.addTests(
            StringIntegrityTest("2.1.1", "Check electionID","Check if electionID is in A*_ucs",["electionID"]),
            BiggerThanIntegrityTest("2.1.2","Check CountingCircles lenght","Check if w >= 1",['w'],1),
            BiggerThanIntegrityTest("2.1.3","Check NumberOfCandidates lenght","Check if t >= 1",['t'],1),
            BiggerThanIntegrityTest("2.1.4","Check Voters lenght","Check if Ne >= 1",['Ne'],0),
            BiggerThanIntegrityTest("2.1.5","Check partialPublicVotingCredentials lenght","Check if s >= 1",['s'],1),
            IterationTest(["NumberOfCandidates"],"For j in {1,...,t} ",int_test_numberOfCandidates,'t'),
            IterationTest(["NumberOfSelections"],"For j in {1,...,t} ",int_test_numberOfSelections,'t'),
            IterationTest(["eligibilityMatrix"],"for i in {1,...,Ne} ", int_multi_test_eligibilityMatrix,'Ne'),
            IterationTest(["candidates"],"for i in {1,...,n} ", int_test_candidate,'n'),
            IterationTest(["voters"],"for i in {1,...,Ne} ", int_test_voter,'Ne'),
            IterationTest(["countingCircles"],"for i in {1,...,Ne} ", int_test_countingCircle,'Ne'),
            IterationTest(["partialPublicVotingCredentials"],"for i in {1,...,Ne} ", int_test_pubc,'Ne'),
            SignaturIntegrityTest("2.1.14","Check Full Signatur","Check if sigParam1 in Bit x Z_q",["sigParam1"]),
            SignaturIntegrityTest("2.1.15","Check Part Signatur","Check if sigParam2 in Bit x Z_q",["sigParam2"]),
            SignaturIntegrityTest("2.1.16","Check other Part Signatur","Check if sigParam3 in Bit x Z_q",["sigParam3"]),
            IterationTest(['sigPrep'],"For j in {1,...,s}",int_test_sigPrep,'s'),
            IterationTest(['sigKgen'],"For j in {1,...,s}",int_test_sigKgen,'s')
        )
        # 2.2 election phase
        int_election_tests = MultiTest("2.2","Election Tests","Test which conntains all election tests")

        int_multi_test_ballots = MultiTest('2.2.1.0',"Ballots Tests","Test which conntains all ballots tests")
        int_multi_test_ballots.addTests(
            InRangeIntegrityTest("2.2.1.1.0","Check Voter ID","Check if voterId is in {0,...,Ne}",['voterId'],0,'Ne'),
            MathGroupeIntegritiyTest("2.2.1.2.0","Check PublicVotingCredential","Check if x_hat is in G_q_hat",["ballot","x_hat"],"p_hat"),
            EncrypdetSelectionIntegrityTest("2.2.1.3.0","Check Encrypted Selection","Check if a_bold is in G_q^2",['ballot',"a_bold"]),
            BallotProofIntegrityTest("2.2.1.4.0","Check BallotProof","Check if pi is in (G_q_hat x G_q^2) x (Z_q_hat x G_q x Z_q)",['ballot',"pi"])
        )

        int_multi_test_response = MultiTest("2.2.2.0","Response Tests","Test which conntains all response tests")
        int_multi_test_response.addTests(
            InRangeIntegrityTest("2.2.2.1.0","Check Voter ID","Check if voterId is in {0,...,Ne}",['voterId'],0,'Ne'),
            OTResponseIntegrityTest("2.2.2.2.0","Check OT Response","Check if beta_j is in G_q^k_i x (Beta_bold^L_M)^n*k_i x G_q",['beta_j']),
            SignaturIntegrityTest("2.2.2.2.3.0","Check OT Signatur","Check if sigCast in Bit^l x Z_q",["sigCast"])

        )

        int_multi_test_confirmations = MultiTest("2.2.3.0","Confirmations Tests","Test which conntains all confirmations tests")
        int_multi_test_confirmations.addTests(
            InRangeIntegrityTest("2.2.3.1.0","Check Voter ID","Check if voterId is in {0,...,Ne}",['voterId'],0,'Ne'),
            MathGroupeIntegritiyTest("2.2.3.2.0","Check Confirmation Credential","Check if y_hat in G_q_hat","y_hat",["confirmation","p.hat"]),
            ConfProofIntegrityTest("2.2.3.3.0","Check ConfirmationProof", "Check if pi is in G_q_hat x Z_q_hat",["confirmation","pi"])
        )
        int_multi_test_finalization = MultiTest("2.2.4.0","Finalization Tests","Test which conntains all finalization tests")
        int_multi_test_finalization.addTests(
            InRangeIntegrityTest("2.2.4.1.0","Check Voter ID","Check if voterId is in {0,...,Ne}",['voterId'],0,'Ne'),
            FinalizationIntegrityTest("2.2.4.2.0","Check Finalization","Check if delta_j is in Beta_bold^L_F x Z_q^2",['delta_j']),
            SignaturIntegrityTest("2.2.4.3.0","Check Finalization Signatur","Check if sigConf in Bit^l x Z_q",["sigConf"])
        )

        int_election_tests.addTests(
            IterationTest(['ballots'],"For all elements Ballots: ",int_multi_test_ballots,'Ne'),
            IterationTest(['responses'],"For all elements in responses: ",int_multi_test_response,'Ne'),
            IterationTest(['confirmations'],"For all elements in confirmations: ",int_multi_test_confirmations,'Ne'),
            IterationTest(['finalizations'],"For all elements in finalizations: ",int_multi_test_finalization,'Ne'),
        )
        int_post_election_tests = MultiTest("2.3","Post Election Tests","Test which conntains all post election tests")
        # Tests for IterationTest
        int_enc_test = EncryptionIntegrityTest("2.3.1.0", "Test Encryption",'For i in {1,..,N} Test if e_bold_j[i] is in G_q^2',['e_bold_j'])
        int_sp_test = ShuffleProofIntegrityTest("2.3.2.0", "Test ShuffleProof",'Check if pi_j in (G_q^3 x G_q^2 x G_q^N) x (Z_q^4 x Z_q^N x Z_q^N) x G_q^N x G_q^N',['pi_j'])
        int_dec_test = DecryptionIntegrityTest("2.3.3.0", "Test Decryption",'Check if b_bold_prime_j in G_q^N',['b_bold_prime_j'])
        int_dp_test = DecryptionProofIntegrityTest("2.3.4.0", "Test DecryptionProof",'Check if pi_prime_j in (G_q x G_q^N) x Z_q',['pi_j'])
        int_vote_test = MatrixBitIntegrityTest("2.3.5.0", "Test Vote",'Check if v_ij in [0,1]',['v_i'],'s')
        int_election_result_test = MatrixBitIntegrityTest("2.3.6.0", "Test Election Result",'Check if omega_ij in [0,1]',['omega_i'],'s')
        int_sig_mix_test = SignaturIntegrityTest("2.3.7.0","Check Mixing Signatur","Check if sigMix_j in Bit^l x Z_q",["sigMix_j"])
        int_sig_dec_test = SignaturIntegrityTest("2.3.8.0","Check Decryption Signatur","Check if sigDec_j in Bit^l x Z_q",["sigDec_j"])
        int_post_election_tests.addTests(
            IterationTest(['encryptions'],"For j in {1,..,s}: ",int_enc_test,'s'),
            IterationTest(['shuffleProofs'],"For j in {1,..,s}: ",int_sp_test,'s'),
            IterationTest(['decryptions'],"For j in {1,..,s}: ",int_dec_test,'s'),
            IterationTest(['decryptionProofs'],"For j in {1,..,s}: ",int_dp_test,'s'),
            IterationTest(['votes'],"For i in {1,..,N}: ",int_vote_test,'N'),
            IterationTest(['w_bold'],"For i in {1,..,N}: ",int_election_result_test,'N'),
            IterationTest(['sigMix'],"For i in {1,..,N}: ",int_sig_mix_test,'s'),
            IterationTest(['sigDec'],"For i in {1,..,N}: ",int_sig_dec_test,'s'),
            SignaturIntegrityTest("2.3.9.0","Check Tallying Signatur","Check if sigTally in Bit^l x Z_q",["sigTally"])
        )

        integrity_tests.addTests(int_pre_election_tests,int_election_tests,int_post_election_tests)
        # 3 Consistency Tests
        consistency_tests = MultiTest("3","Consistency Tests","Test which conntains all consistency tests")
        cons_pre_election_tests = MultiTest("3.1","Pre Election Tests","Test which conntains all pre election tests")
        # Tests for Integrity Tests
        cons_test_pvc = VectorLengthConsistenyTest("3.1.8.0","Check PartialPublicVotingCredential","Check if |d_hat_j| = Ne",["d_hat_j"],"Ne")
        cons_pre_election_tests.addTests(
            VectorLengthConsistenyTest("3.1.1","Check Number of Candidates","Check if |numberOfCandidates| = t",["numberOfCandidates"],"t"),
            VectorLengthConsistenyTest("3.1.2","Check Number of selections","Check if |numberOfSelections| = t",["numberOfSelections"],"t"),
            MatrixLengthConsistenyTest("3.1.3","Check EligibilityMatrix","Check if |E| = (Ne,t)",["eligibilityMatrix"],["Ne","t",'e_i']),
            VectorLengthConsistenyTest("3.1.4","Check Candidates","Check if |candidates| = n",["candidates"],"n"),
            VectorLengthConsistenyTest("3.1.5","Check Voters","Check if |votes| = Ne","voters","Ne"),
            VectorLengthConsistenyTest("3.1.6","Check CountingCircles","Check if |countingCircles| = Ne",["countingCircles"],"Ne"),
            VectorLengthConsistenyTest("3.1.7","Check PartialPublicVotingCredentials","Check if |partialPublicVotingCredentials| = s",["partialPublicVotingCredentials"],"s"),
            IterationTest("partialPublicVotingCredentials","For j in {1,...,s} ",cons_test_pvc,'s'),
            VectorLengthConsistenyTest("3.1.9","Check PublicKeyShares","Check if |publicKeyShares| = s",["publicKeyShares"],"s"),
            PrimeConsistencyTest("3.1.10","Check Primes","Check if p_n+w * prod(list) < p.",["numberOfSelections"])
        )

        cons_election_tests = MultiTest("3.2","Election Tests","Test which conntains all election tests")
        # Tests for IterationTest
        cons_ballot_test = VectorLengthConsistenyTest('3.2.1.0','Ballot Test','Check if |a_bold| = s',['ballot','a_bold'],'s')
        cons_multi_test_response = MultiTest('3.2.2.0',"Response Tests","Test which conntains all responses tests")
        cons_multi_test_response.addTests(
            VectorItemsConsistenyTest('3.2.2.1.0','Check Response','For Beta_bold_i = {Beta_bold_i,1,...,Beta_bold_i,s}, Check if |Beta_bold_i| = s',['voterId'],['responses','beta_j']),
            VectorItemsConsistenyTest('3.2.2.2.0', "Check OT-Signatur",'For sigCast_i = {sigCast_i,1,...,sigCast_i,s}, Check if |sigCast_i| = s',['voterId'],['responses','sigCast'])
        )

        cons_multi_test_finalization = MultiTest("3.2.3.0","Finalization Tests","Test which conntains all finalization tests")
        cons_multi_test_finalization.addTests(
            VectorItemsConsistenyTest('3.2.3.1.0','Check Finalization','For delta_bold_i = {delta_bold_i,1,...,delta_bold_i,s}, Check if |delta_bold_i| = s',['voterId'],['finalizations','delta_j']),
            VectorItemsConsistenyTest('3.2.3.2.0', "Check Finalization Signatur ",'For sigCast_i = {sigCast_i,1,...,sigCast_i,s}, Check if |sigCast_i| = s',['voterId'],['finalizations','sigConf'])
        )

        cons_election_tests.addTests(
            IterationTest(['ballots'],"For all elements Ballots: ",cons_ballot_test,'Ne'),
            IterationTest(['responses'],"For all elements in responses: ",cons_multi_test_response,'Ne'),
            IterationTest(['finalizations'],"For all elements in finalizations: ",cons_multi_test_finalization,'Ne'),
        )

        cons_post_election_tests = MultiTest("3.3","Post Election Tests","Test which conntains all post election tests")
        # Tests for IterationTests
        cons_encryption_test = VectorLengthConsistenyTest('3.3.2.0','Check Encryption','Check if |e_bold_j| = N',['e_bold_j'],'N')
        cons_shuffleProof_test = VectorLengthConsistenyTest('3.3.4.0','Check ShuffleProof','Check if |pi_j| = N',['pi_j'],'N')
        cons_decryption_test = VectorLengthConsistenyTest('3.3.6.0','Check Decryption','Check if |b_bold_prime_j| = N',['b_bold_prime_j'],'N')
        cons_decryptionProof_test = VectorLengthConsistenyTest('3.3.8.0','Check DecryptionProof','Check if |pi_prime_j| = N',['pi_prime_j'],'N')

        cons_post_election_tests.addTests(
            MatrixLengthConsistenyTest('3.3.1', "Check Encryptions","Check if |E_bold_prime| = (N,t)",['encryptions'],['N','t','e_bold_j']),
            IterationTest(['encryptions'],"For j in {1,..,s}: ",cons_encryption_test,'s'),
            VectorLengthConsistenyTest('3.3.3','Check ShuffleProofs','Check if |pi| = s',['shuffleProofs'],'s'),
            IterationTest(['shuffleProofs'],"For j in {1,..,s}: ",cons_shuffleProof_test,'s'),
            VectorLengthConsistenyTest('3.3.5','Check Decryptions','Check if |B_bold_prime| = s',['decryptions'],'s'),
            IterationTest(['decryptions'],"For j in {1,..,s}: ",cons_decryption_test,'s'),
            VectorLengthConsistenyTest('3.3.7','Check DecryptionProofs','Check if |pi_prime| = s',['decryptionProofs'],'s'),
            IterationTest(['decryptionProofs'],"For j in {1,..,s}: ",cons_decryptionProof_test,'s'),
            MatrixLengthConsistenyTest('3.3.9', "Check Votes","Check if |V_bold| = (N,n)",['votes'],['N','n','v_i']),
            MatrixLengthConsistenyTest('3.3.10', "Check Election Result","Check if |W_bold| = (N,w)",['w_bold'],['N','w','omega_i']),
            VectorLengthConsistenyTest('3.3.11','Check Mixing Signatur','Check if |sigMix| = s',['sigMix'],'s'),
            VectorLengthConsistenyTest('3.3.12','Check Decryption Signatur','Check if |sigDec| = s',['sigDec'],'s'),
        )
        consistency_tests.addTests(cons_pre_election_tests, cons_election_tests, cons_post_election_tests)

        evidence_tests = MultiTest("4","Evidence Tests","Test which conntains all evidence tests")
        ev_check_proofs = MultiTest("4.1","Proof Tests","Test which conntains all proofs tests")
        # Tests for IterationTests
        ev_test_ballot= BallotProofEvidenceTest("4.1.1.0","Check BallotProof","Check proof of Ballot",["ballot"])
        ev_test_conf = ConfirmationProofEvidenceTest("4.1.2.0","Check ConfirmationProof","Check proof of Confirmation",["confirmation"])
        ev_test_shuffle = ShuffleProofEveidenceTest("4.1.3.0","Check ShuffleProof","Check proof of shuffled encryptions",["pi_j"])
        ev_test_decrytion = DecryptionProofEvidenceTest("4.1.4.0","Check DecryptionProof","Check proof of Decryption",["pi_prime_j"])
        ev_check_proofs.addTests(
            IterationTest(['ballots'],"For all Ballots: ",ev_test_ballot,'Ne'),
            IterationTest(['confirmations'],"For all Confirmations: ",ev_test_conf,'Ne'),
            IterationTest(['shuffleProofs'],"For j in {1,...s}: ",ev_test_shuffle,'s'),
            IterationTest(['decryptionProofs'],"For j in {1,...s}: ",ev_test_decrytion,'s')
        )
        evidence_tests.addTest(ev_check_proofs)

        authenticity_tests = MultiTest("5","Authenticiy Tests","Test which conntains all authenticiy tests")
        au_cert_tests = MultiTest("5.1","Check all Certificates","Test which conntains all certificate tests")
        # Test for IterationTest
        au_test_c_auth = CertificateAuthenticityTest("5.1.2.0","Check AuthorityCert","Check validity of Certificate of election authority",["c_auth_j"])
        au_cert_tests.addTests(
            CertificateAuthenticityTest("5.1.1","Check AdminCert","Check validity of Certificate of election administrator",["certAdmin"]),
            IterationTest('C_auths',"For j in {1,...s}: ",au_test_c_auth,'s'),
        )
        au_sig_tests = MultiTest("5.2","Check all Signaturs","Test which conntains all signatur tests")
        # Test for IterationTest
        aut_test_sigPrep = SignaturAuthenticityTest("5.2.5.0", "Check Public Credential","Check Signatur of public credential",["sigPrep_j"])
        aut_test_sigKgen = SignaturAuthenticityTest("5.2.6.0", "Check Public Keys","Check Signatur of public keys",["sigKgen_j"])
        aut_test_sigCast = SignaturAuthenticityTest("5.2.7.0", "Check OT Response","Check Signatur of OT response",["sigCast_j"])
        aut_test_sigConf = SignaturAuthenticityTest("5.2.8.0", "Check Finalization","Check Signatur of finalization",["sigConf_j"])
        aut_test_sigMix = SignaturAuthenticityTest("5.2.9.0", "Check Mixed Result","Check Signatur of mixed and re-encrypton",["sigMix_j"])
        aut_test_sigDec = SignaturAuthenticityTest("5.2.10.0", "Check Decryption","Check Signatur of decryption",["sigDec_j"])

        au_sig_tests.addTests(
            SignaturAuthenticityTest("5.2.1", "Check Full Params","Check Signatur of full election parameters",["sigParam1"]),
            SignaturAuthenticityTest("5.2.2", "Check Part Params","Check Signatur of part of election parameters",["sigParam2"]),
            SignaturAuthenticityTest("5.2.3", "Check other Part Params","Check Signatur of other part of election parameters",["sigParam3"]),
            SignaturAuthenticityTest("5.2.4", "Check Tallying Result","Check Signatur of tallying result",["sigTally"]),
            IterationTest(['sigPrep'],"For j in {1,...s}: ",aut_test_sigPrep,'s'),
            IterationTest(['sigKgen'],"For j in {1,...s}: ",aut_test_sigKgen,'s'),
            IterationTest(['responses'],"For j in {1,...s}: ",aut_test_sigCast,'s'),
            IterationTest(['finalizations'],"For j in {1,...s}: ",aut_test_sigConf,'s'),
            IterationTest(['sigMix'],"For j in {1,...s}: ",aut_test_sigMix,'s'),
            IterationTest(['sigDec'],"For j in {1,...s}: ",aut_test_sigDec,'s'),
        )
        authenticity_tests.addTests(au_cert_tests,au_sig_tests)

        self.root_test.addTest(completness_tests)
        self.root_test.addTest(integrity_tests)
        self.root_test.addTest(consistency_tests)
        self.root_test.addTest(evidence_tests)
        self.root_test.addTest(authenticity_tests)

    def verify(self,data_dict,report,secparams):
        TestResult.setReport(report)
        election_data = prepareData(data_dict,secparams)
        root_result = self.root_test.runTest(election_data)
        report.result = root_result
