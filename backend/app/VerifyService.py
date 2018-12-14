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
from chvote.verifier.MultiTest import MultiTest
from chvote.verifier.IterationTest import IterationTest

from chvote.verifier.CompletnessTest import SingleCompletnessTest
from chvote.verifier.IntegrityTests.BiggerThanIntegrityTest import BiggerThanIntegrityTest
from chvote.verifier.IntegrityTests.BallotProofIntegrityTest import BallotProofIntegrityTest
from chvote.verifier.IntegrityTests.BitIntegrityTest import BitIntegrityTest
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

from chvote.verifier.ConsistencyTest import LenghtEqualityConsistenyTest
from chvote.verifier.EvidenceTests.BallotProofEvidenceTest import BallotProofEvidenceTest
from chvote.verifier.EvidenceTests.ConfirmationProofEvidenceTest import ConfirmationProofEvidenceTest
from chvote.verifier.EvidenceTests.DecryptionProofEvidenceTest import DecryptionProofEvidenceTest
from chvote.verifier.EvidenceTests.ShuffleProofEveidenceTest import ShuffleProofEveidenceTest

from chvote.verifier.AuthenticityTest import CertificateAuthenticityTest, SignaturAuthenticityTest

class VerifyService(object):
    """docstring for VerifyService."""
    def __init__(self):
        self.root_test = MultiTest("0:","Root Test","Test which conntains all Tests")
        self.setUpTests()

    def setUpTests(self):
        completness_tests = MultiTest("1","Completness Tests","Test which conntains all completness tests")
        # 1.1 pre election
        com_pre_election_tests = MultiTest("1.1","pre_election Tests","Test which conntains all pre_election tests")
        com_pre_election_tests.addTests(
            SingleCompletnessTest("1.1.1","Check Election ID","Check if ElectionID is in election_data",'electionID'),
            SingleCompletnessTest("1.1.2","Check Number of candidates","Check if vector numberOfCandidates is in election_data",'numberOfCandidates'),
            SingleCompletnessTest("1.1.3","Check Candidates","Check if vector candidates is in election_data",'candidates'),
            SingleCompletnessTest("1.1.4","Check Number of selections","Check if vector numberOfSelections is in election_data",'numberOfSelections'),
            SingleCompletnessTest("1.1.5","Check Voters","Check if vector voters is in election_data",'voters'),
            SingleCompletnessTest("1.1.6","Check CountingCircles","Check if vector countingCircles is in election_data",'countingCircles'),
            SingleCompletnessTest("1.1.7","Check EligibilityMatrix","Check if eligibilityMatrix is in election_data",'eligibilityMatrix'),
            SingleCompletnessTest("1.1.8","Check Public voting credentials","Check if vector partialPublicVotingCredentials is in election_data",'partialPublicVotingCredentials'),
            SingleCompletnessTest("1.1.9","Check Public keys","Check if vector publicKeyShares is in election_data",'publicKeyShares'),
            SingleCompletnessTest("1.1.10","Check Full Signatur","Check if Signatur of full election parameters is in election_data",'sigParam1'),
            SingleCompletnessTest("1.1.11","Check Partial Signatur","Check if Signatur of part of election parameters is in election_data",'sigParam2'),
            SingleCompletnessTest("1.1.12","Check other part Signatur","Check if Signatur of  other part of election parameters is in election_data",'sigParam3'),
            SingleCompletnessTest("1.1.13","Check Public credentials Signatur","Check if vector of Signatur of Public credentials is in election_data",'sigPrep'),
            SingleCompletnessTest("1.1.14","Check Public keys Signatur","Check if vector of Signatur of Public keys is in election_data",'sigKgen')
        )
        # 1.2 election
        com_election_tests = MultiTest("1.2","election Tests","Test which conntains all election tests")
        com_multi_test_ballot = MultiTest("multi:0","Ballot Tests","Test which conntains all ballot tests")
        com_multi_test_ballot.addTests(
            SingleCompletnessTest("1.2.2.0","Check Voter ID","Check if voterId is in VoterBallot",'voterId'),
            SingleCompletnessTest("1.2.3.0","Check Ballot","Check if ballot is in VoterBallot",'ballot')
        )
        com_multi_test_resbonse = MultiTest("multi:0","Response Tests","Test which conntains all response tests")
        com_multi_test_resbonse.addTests(
            SingleCompletnessTest("1.2.5.0","Check Voter ID","Check if voterId is in response_dict",'voterId'),
            SingleCompletnessTest("1.2.6.0","Check OT-Responses","Check if vector OT-Responses is in response_dict",'beta_j'),
            SingleCompletnessTest("1.2.7.0","Check OT-Signatur","Check if OT-Signatur is in response_dict",'sigCast')
        )
        com_multi_test_confirmation = MultiTest("multi:0","Confirmation Tests","Test which conntains all confirmation tests")
        com_multi_test_confirmation.addTests(
            SingleCompletnessTest("1.2.9.0","Check Voter ID","Check if voterId is in confirmation_dict",'voterId'),
            SingleCompletnessTest("1.2.10.0","Check Confirmation","Check if confirmation is in confirmation_dict",'confirmation')
        )
        com_multi_test_finalization = MultiTest("multi:0","Finalization Tests","Test which conntains all finalization tests")
        com_multi_test_finalization.addTests(
            SingleCompletnessTest("1.2.12.0","Check Voter ID","Check if voterId is in finalization_dict",'voterId'),
            SingleCompletnessTest("1.2.13.0","Check Finalization","Check if finalization is in finalization_dict",'delta_j'),
            SingleCompletnessTest("1.2.14.0","Check Finalization-Signatur","Check if Finalization-Signatur is in finalization_dict",'sigConf')
        )
        com_election_tests.addTests(
            SingleCompletnessTest("1.2.1","Check Ballots","Check if vector ballots is in election_data",'ballots'),
            IterationTest('ballots',"For all elements Ballots: ",com_multi_test_ballot,'Ne'),
            SingleCompletnessTest("1.2.4","Check Responses","Check if vector responses is in election_data",'responses'),
            IterationTest('responses',"For all elements in responses: ",com_multi_test_resbonse,'Ne'),
            SingleCompletnessTest("1.2.8","Check Confirmations","Check if vector confirmations is in election_data",'confirmations'),
            IterationTest('confirmations',"For all elements in confirmations: ",com_multi_test_confirmation,'Ne'),
            SingleCompletnessTest("1.2.11","Check Finalization","Check if vector finalization_list is in election_data",'finalizations'),
            IterationTest('finalizations',"For all elements in finalization: ",com_multi_test_finalization,'Ne'),
        )
        # 1.3 post_election
        com_post_election_tests = MultiTest("1.3","post_election Tests","Test which conntains all post_election tests")
        com_post_election_tests.addTests(
            SingleCompletnessTest("1.3.1","Check Encryptions","Check if vector of mixed an encrypted ballot is in election_data",'encryptions'),
            SingleCompletnessTest("1.3.2","Check Shuffel Proofs","Check if vector of Shuffel Proofs is in election_data",'shuffleProofs'),
            SingleCompletnessTest("1.3.3","Check Decryptions","Check if vector of partial decrypted ballots is in election_data",'decryptions'),
            SingleCompletnessTest("1.3.4","Check Decryption Proofs","Check if vector of decryption Proofs is in election_data",'decryptionProofs'),
            SingleCompletnessTest("1.3.5","Check Election Result","Check if matrix of election result is in election_data",'votes'),
            SingleCompletnessTest("1.3.6","Check Counting Circles","Check if matrix of counting Circle is in election_data",'w_bold'),
            SingleCompletnessTest("1.3.7","Check Tallying Signatur","Check if tallying signatur is in election_data",'sigTally'),
            SingleCompletnessTest("1.3.8","Check Mixing Signatur","Check if mixing signatur is in election_data",'sigMix'),
            SingleCompletnessTest("1.3.9","Check Decryption Signatur","Check if decryption signatur is in election_data",'sigDec'),
        )
        completness_tests.addTests(com_pre_election_tests,com_election_tests,com_post_election_tests)
        # 2. Integrity Tests
        integrity_tests = MultiTest("2","Integrity Tests","Test which conntains all integrity tests")
        # 2.1 pre_election Tests
        int_pre_election_tests = MultiTest("2.1","pre_election Tests","Test which conntains all pre_election tests")
        # Tests for IterationTests
        int_test_numberOfCandidates = BiggerThanIntegrityTest("2.1.7.0","Check NumberOfCandidates","Check if n_j >= 2",'n_j',2)
        int_test_numberOfSelections = BiggerThanIntegrityTest("2.1.8.0","Check NumberOfSelections","Check if k_j >= 1",'k_j',1)
        int_multi_test_eligibilityMatrix = MultiTest("2.1.9.0","Check EligibilityMatrix","Test which conntains all eligibilityMatrix tests")
        int_test_eligibilityMatrix_j = BitIntegrityTest("2.1.9.1.0","Check EligibilityMatrix Bit","Check if e_ij in [0,1]",'e_j')
        int_multi_test_eligibilityMatrix.addTests(
            IterationTest('e_i','for j in {1,...,t} ',int_test_eligibilityMatrix_j,'t'),
            EligibilityMatrixIntegrityTest("2.1.9.2.0","Check EligibilityMatrix Vector ","Check if sum(e_ij) >= 1","e_i")
            )
        int_test_candidate = StringIntegrityTest("2.1.11.0", "Check Candidate","Check if Candidate is in A*_ucs","C_i")
        int_test_voter = StringIntegrityTest("2.1.12.0", "Check Voter","Check if Voter is in A*_ucs","V_i")
        int_test_countingCircle = InRangeIntegrityTest("2.1.13.0", "Check CountingCircle","Check if w_i in {1,...,w}","w_i","w")
        int_test_pubc_j = PublicVotingCredentialIntegrityTest("2.1.14.0", "Check PublicVotingCredential","Check if d_hat_ij in G_q_hat^2","d_hat_j")
        int_test_pubc_i = IterationTest('d_i',"For j in {1,...,s}",int_test_pubc_j,'s')
        int_test_pk = MathGroupeIntegritiyTest("2.1.15.0","Check Public key","For all authority test it's Public key",'pk_j','p')
        int_test_sigPrep = SignaturIntegrityTest("2.1.19","Check PublicVotingCredential Signatur","Check if sigPrep_j in Bit x Z_q","sigPrep_j")
        int_test_sigKgen = SignaturIntegrityTest("2.1.20","Check PublicVoting Key Signatur","Check if sigKgen_j in Bit x Z_q","sigKgen_j")
        # k is not defined
        # NumberOfSelectionsIntegrityTest("2.1.5","Check NumberOfSelections","Check if k = sum(k_j)","numberOfSelections"),
        int_pre_election_tests.addTests(
            StringIntegrityTest("2.1.1", "Check electionID","Check if electionID is in A*_ucs","electionID"),
            BiggerThanIntegrityTest("2.1.2","Check CountingCircles lenght","Check if w >= 1",'w',1),
            BiggerThanIntegrityTest("2.1.3","Check NumberOfCandidates lenght","Check if t >= 1",'t',1),
            BiggerThanIntegrityTest("2.1.4","Check Voters lenght","Check if Ne >= 1",'Ne',0),
            BiggerThanIntegrityTest("2.1.6","Check partialPublicVotingCredentials lenght","Check if s >= 1",'s',1),
            IterationTest("NumberOfCandidates","For j in {1,...,t} ",int_test_numberOfCandidates,'t'),
            IterationTest("NumberOfSelections","For j in {1,...,t} ",int_test_numberOfSelections,'t'),
            IterationTest("eligibilityMatrix","for i in {1,...,Ne} ", int_multi_test_eligibilityMatrix,'Ne'),
            IterationTest("candidates","for i in {1,...,n} ", int_test_candidate,'n'),
            IterationTest("voters","for i in {1,...,Ne} ", int_test_voter,'Ne'),
            IterationTest("countingCircles","for i in {1,...,Ne} ", int_test_countingCircle,'Ne'),
            IterationTest("partialPublicVotingCredentials","for i in {1,...,Ne} ", int_test_pubc_i,'Ne'),
            SignaturIntegrityTest("2.1.16","Check Full Signatur","Check if sigParam1 in Bit x Z_q","sigParam1"),
            SignaturIntegrityTest("2.1.17","Check Part Signatur","Check if sigParam2 in Bit x Z_q","sigParam2"),
            SignaturIntegrityTest("2.1.18","Check other Part Signatur","Check if sigParam3 in Bit x Z_q","sigParam3"),
            IterationTest('sigPrep',"For j in {1,...,s}",int_test_sigPrep,'s'),
            IterationTest('sigKgen',"For j in {1,...,s}",int_test_sigKgen,'s')
        )
        # 2.2 election phase
        int_election_test = MultiTest("2.2","election Tests","Test which conntains all election tests")

        int_multi_test_ballots = MultiTest('2.2.1.0',"Ballots Tests","Test which conntains all ballots tests")
        int_multi_test_ballots.addTests(
            InRangeIntegrityTest("2.2.1.1.0","Check Voter ID","Check if voterId is in {1,...,Ne}",'voterId','Ne'),
            MathGroupeIntegritiyTest("2.2.1.2.0","Check PublicVotingCredential","Check if x_hat is in G_q_hat","x_hat","p_hat",'ballot'),
            EncrypdetSelectionIntegrityTest("2.2.1.3.0","Check Encrypted Selection","Check if a_bold is in G_q^2","a_bold"),
            BallotProofIntegrityTest("2.2.1.4.0","Check BallotProof","Check if pi is in (G_q_hat x G_q^2) x (Z_q_hat x G_q x Z_q)","pi")
        )

        int_multi_test_response = MultiTest("2.2.2.0","Response Tests","Test which conntains all response tests")
        int_multi_test_response.addTests(
            InRangeIntegrityTest("2.2.2.1.0","Check Voter ID","Check if voterId is in {1,...,Ne}",'voterId','Ne'),
            OTResponseIntegrityTest("2.2.2.2.0","Check OT Response","Check if beta_j is in G_q^k_i x (Beta_bold^L_M)^n*k_i x G_q",'beta_j')
        )

        int_multi_test_confirmations = MultiTest("2.2.3.0","Confirmations Tests","Test which conntains all confirmations tests")
        int_multi_test_confirmations.addTests(
            InRangeIntegrityTest("2.2.3.1.0","Check Voter ID","Check if voterId is in {1,...,Ne}",'voterId','Ne'),
            MathGroupeIntegritiyTest("2.2.3.2.0","Check Confirmation Credential","Check if y_hat in G_q_hat","y_hat","p.hat","confirmation"),
            ConfProofIntegrityTest("2.2.3.3.0","Check ConfirmationProof", "Check if pi is in G_q_hat x Z_q_hat","pi")
        )
        int_multi_test_finalization = MultiTest("2.2.4.0","Finalization Tests","Test which conntains all finalization tests")
        int_multi_test_finalization.addTests(
            InRangeIntegrityTest("2.2.4.1.0","Check Voter ID","Check if voterId is in {1,...,Ne}",'voterId','Ne'),
            FinalizationIntegrityTest("2.2.4.2.0","Check Finalization","Check if delta_j is in Beta_bold^L_F x Z_q^2",'delta_j'),
            SignaturIntegrityTest("2.2.4.3.0","Check Finalization Signatur","Check if sigConf in Bit^l x Z_q","sigConf")
        )

        int_election_test.addTests(
            IterationTest('ballots',"For all elements Ballots: ",int_multi_test_ballots,'Ne'),
            IterationTest('responses',"For all elements in responses: ",int_multi_test_response,'Ne'),
            IterationTest('confirmations',"For all elements in confirmations: ",int_multi_test_confirmations,'Ne'),
            IterationTest('finalizations',"For all elements in finalizations: ",int_multi_test_finalization,'Ne'),
        )
        integrity_tests.addTests(int_pre_election_tests,int_election_test)
        # 3 Consistency Tests
        consistency_tests = MultiTest("3","Consistency Tests","Test which conntains all consistency tests")
        cons_pre_election_tests = MultiTest("3.1","pre_election Tests","Test which conntains all pre_election tests")
        # Tests for Integrity Tests
        cons_test_pvc = LenghtEqualityConsistenyTest("3.1.8.0","Check PartialPublicVotingCredential","Check if |d_hat_j| = Ne","d_hat_j","Ne")
        cons_pre_election_tests.addTests(
            LenghtEqualityConsistenyTest("3.1.1","Check Number of Candidates","Check if |numberOfCandidates| = t","numberOfCandidates","t"),
            LenghtEqualityConsistenyTest("3.1.2","Check Number of selections","Check if |numberOfSelections| = t","numberOfSelections","t"),
            LenghtEqualityConsistenyTest("3.1.4","Check Candidates","Check if |candidates| = n","candidates","n"),
            LenghtEqualityConsistenyTest("3.1.5","Check Voters","Check if |votes| = Ne","voters","Ne"),
            LenghtEqualityConsistenyTest("3.1.6","Check CountingCircles","Check if |countingCircles| = Ne","countingCircles","Ne"),
            LenghtEqualityConsistenyTest("3.1.7","Check PartialPublicVotingCredentials","Check if |partialPublicVotingCredentials| = s","partialPublicVotingCredentials","s"),
            IterationTest("partialPublicVotingCredentials","For j in {1,...,s} ",cons_test_pvc,'s'),
            LenghtEqualityConsistenyTest("3.1.9","Check PublicKeyShares","Check if |publicKeyShares| = s","publicKeyShares","s"),
        )
        consistency_tests.addTests(cons_pre_election_tests)

        evidence_tests = MultiTest("4","Evidence Tests","Test which conntains all evidence tests")
        ev_check_proofs = MultiTest("4.1","Check all Proofs","Test which conntains all proofs tests")
        # Tests for IterationTests
        ev_test_ballot= BallotProofEvidenceTest("4.1.1.0","Check BallotProof","Check proof of Ballot","ballot")
        ev_test_conf = ConfirmationProofEvidenceTest("4.1.2.0","Check ConfirmationProof","Check proof of Confirmation","confirmation")
        ev_test_shuffle = ShuffleProofEveidenceTest("4.1.3.0","Check ConfirmationProof","Check proof of Confirmation","shuffleProof")
        ev_test_decrytion = DecryptionProofEvidenceTest("4.1.4.0","Check DecryptionProof","Check proof of Decryption","decryptionProof")
        ev_check_proofs.addTests(
            IterationTest('ballots',"For all Ballots: ",ev_test_ballot,'Ne'),
            IterationTest('confirmations',"For all Confirmations: ",ev_test_conf,'Ne'),
            IterationTest('shuffleProofs',"For j in {1,...s}: ",ev_test_shuffle,'s'),
            IterationTest('decryptionProofs',"For j in {1,...s}: ",ev_test_decrytion,'s')
        )
        evidence_tests.addTest(ev_check_proofs)

        authenticity_tests = MultiTest("5","Authenticiy Tests","Test which conntains all authenticiy tests")
        au_cert_tests = MultiTest("5.1","Check all Certificates","Test which conntains all certificate tests")
        # Test for IterationTest
        au_test_c_auth = CertificateAuthenticityTest("5.1.2.0","Check AuthorityCert","Check validity of Certificate of election authority","c_auth_j")
        au_cert_tests.addTests(
            CertificateAuthenticityTest("5.1.1","Check AdminCert","Check validity of Certificate of election administrator","certAdmin"),
            IterationTest('C_auths',"For j in {1,...s}: ",au_test_c_auth,'s'),
        )
        au_sig_tests = MultiTest("5.2","Check all Signaturs","Test which conntains all signatur tests")
        # Test for IterationTest
        aut_test_sigPrep = SignaturAuthenticityTest("5.2.5.0", "Check Public Credential","Check Signatur of public credential","sigPrep_j")
        aut_test_sigKgen = SignaturAuthenticityTest("5.2.6.0", "Check Public Keys","Check Signatur of public keys","sigKgen_j")
        aut_test_sigCast_i = SignaturAuthenticityTest("5.2.7.0", "Check OT Response","Check Signatur of OT response","sigCast_i")
        aut_test_sigCast_j = IterationTest('sigCast_j',"For i in {1,...Ne}: ",aut_test_sigCast_i,'Ne')
        aut_test_sigConf_i = SignaturAuthenticityTest("5.2.8.0", "Check Finalization","Check Signatur of finalization","sigConf_i")
        aut_test_sigConf_j = IterationTest('sigConf_j',"For i in {1,...Ne}: ",aut_test_sigConf_i,'Ne')
        aut_test_sigMix = SignaturAuthenticityTest("5.2.9.0", "Check Mixed Result","Check Signatur of mixed and re-encrypton","sigMix_j")
        aut_test_sigDec = SignaturAuthenticityTest("5.2.8.0", "Check Decryption","Check Signatur of decryption","sigDec_j")

        au_sig_tests.addTests(
            SignaturAuthenticityTest("5.2.1", "Check Full Params","Check Signatur of full election parameters","sigParam1"),
            SignaturAuthenticityTest("5.2.2", "Check Part Params","Check Signatur of part of election parameters","sigParam2"),
            SignaturAuthenticityTest("5.2.3", "Check other Part Params","Check Signatur of other part of election parameters","sigParam3"),
            SignaturAuthenticityTest("5.2.4", "Check Tallying Result","Check Signatur of tallying result","sigTally"),
            IterationTest('sigPrep',"For j in {1,...s}: ",aut_test_sigPrep,'s'),
            IterationTest('sigKgen',"For j in {1,...s}: ",aut_test_sigKgen,'s'),
            IterationTest('sigCast',"For j in {1,...s}: ",aut_test_sigCast_j,'s'),
            IterationTest('sigConf',"For j in {1,...s}: ",aut_test_sigConf_j,'s'),
            IterationTest('sigMix',"For j in {1,...s}: ",aut_test_sigMix,'s'),
            IterationTest('sigDec',"For j in {1,...s}: ",aut_test_sigDec,'s'),
        )
        authenticity_tests.addTests(au_cert_tests)

        self.root_test.addTest(completness_tests)
        self.root_test.addTest(integrity_tests)
        self.root_test.addTest(consistency_tests)
        self.root_test.addTest(evidence_tests)
        self.root_test.addTest(authenticity_tests)

    def verify(self,data_dict,report,secparams):
        election_data = prepareData(data_dict,secparams)
        root_result = self.root_test.runTest(election_data)
        report.result = root_result
