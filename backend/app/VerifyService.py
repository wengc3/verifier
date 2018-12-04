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
from chvote.verifier.CompletnessTest import SingleCompletnessTest
from chvote.verifier.IntegrityTest import ListBiggerThanIntegrityTest, PubKeyIntegritiyTest
from chvote.verifier.IterationTest import IterationTest
from chvote.verifier.ConsistencyTest import LenghtEqualityConsistenyTest
from chvote.verifier.EvidenceTest import BallotProofEvidenceTest
from chvote.verifier.AuthenticityTest import CertificateAuthenticityTest

class VerifyService(object):
    """docstring for VerifyService."""
    def __init__(self):
        self.root_test = MultiTest("0","Root Test","Test which conntains all Tests")
        self.setUpTests()

    def setUpTests(self):
        completness_tests = MultiTest("1","Completness Tests","Test which conntains all completness tests")
        # 1.1 pre election
        com_pre_election_tests = MultiTest("1.1","pre_election Tests","Test which conntains all pre_election tests")
        com_pre_election_tests.addTests(
            SingleCompletnessTest("1.1.1","Check Election ID","Check if ElectionID is in election_data",'electionID'),
            SingleCompletnessTest("1.1.2","Check Number of candidates","Check if vector numberOfCandidates is in election_data",'numberOfCandidates'),
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
            SingleCompletnessTest("1.1.13","Check Public keys Signatur","Check if vector of Signatur of Public keys is in election_data",'sigKgen')
        )
        # 1.2 election
        com_election_tests = MultiTest("1.2","election Tests","Test which conntains all election tests")
        com_multi_test_ballot = MultiTest("no id","Ballot Tests","Test which conntains all ballot tests")
        com_multi_test_ballot.addTests(
            SingleCompletnessTest("1.2.2","Check Voter ID","Check if voterId is in VoterBallot",'voterId'),
            SingleCompletnessTest("1.2.3","Check Ballot","Check if ballot is in VoterBallot",'ballot')
        )
        com_multi_test_resbonse = MultiTest("no id","Response Tests","Test which conntains all response tests")
        com_multi_test_resbonse.addTests(
            SingleCompletnessTest("1.2.5","Check Voter ID","Check if voterId is in response_dict",'voterId'),
            SingleCompletnessTest("1.2.6","Check OT-Responses","Check if vector OT-Responses is in response_dict",'beta_j'),
            SingleCompletnessTest("1.2.7","Check OT-Signatur","Check if OT-Signatur is in response_dict",'sigCast')
        )
        com_multi_test_confirmation = MultiTest("no id","Confirmation Tests","Test which conntains all confirmation tests")
        com_multi_test_confirmation.addTests(
            SingleCompletnessTest("1.2.9","Check Voter ID","Check if voterId is in confirmation_dict",'voterId'),
            SingleCompletnessTest("1.2.10","Check Confirmation","Check if confirmation is in confirmation_dict",'confirmation')
        )
        com_multi_test_randomization = MultiTest("no id","Randomization Tests","Test which conntains all randomization tests")
        com_multi_test_randomization.addTests(
            SingleCompletnessTest("1.2.12","Check Voter ID","Check if voterId is in randomization_dict",'voterId'),
            SingleCompletnessTest("1.2.13","Check Randomization","Check if randomization is in randomization_dict",'randomization'),
            SingleCompletnessTest("1.2.14","Check Randomization-Signatur","Check if Randomization-Signatur is in randomization_dict",'sigConf')
        )
        com_election_tests.addTests(
            SingleCompletnessTest("1.2.1","Check Ballots","Check if vector ballots is in election_data",'ballots'),
            IterationTest('ballots',"For all elements Ballots: ",com_multi_test_ballot),
            SingleCompletnessTest("1.2.4","Check Responses","Check if vector responses is in election_data",'responses'),
            IterationTest('responses',"For all elements in responses: ",com_multi_test_resbonse),
            SingleCompletnessTest("1.2.8","Check Confirmations","Check if vector confirmations is in election_data",'confirmations'),
            IterationTest('confirmations',"For all elements in confirmations: ",com_multi_test_confirmation),
            SingleCompletnessTest("1.2.11","Check Randomizations","Check if vector randomizations_list is in election_data",'randomizations'),
            IterationTest('randomizations',"For all elements in randomizations: ",com_multi_test_randomization),
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
        int_test_numberOfCandidates = ListBiggerThanIntegrityTest("2.1.7","Check NumberOfCandidates","Check if n_j >= 2",'n_j',2)
        int_test_numberOfSelections = ListBiggerThanIntegrityTest("2.1.8","Check NumberOfSelections","Check if k_j >= 1",'k_j',1)
        int_test_pk = PubKeyIntegritiyTest("2.1.15","Check Public key","For all authority test it's Public key",'pk_j')
        int_pre_election_tests.addTests(
            ListBiggerThanIntegrityTest("2.1.2","Check CountingCircles lenght","Check if w >= 1",'w',1),
            ListBiggerThanIntegrityTest("2.1.3","Check NumberOfCandidates lenght","Check if t >= 1",'t',1),
            ListBiggerThanIntegrityTest("2.1.4","Check Voters lenght","Check if Ne >= 1",'Ne',0),
            ListBiggerThanIntegrityTest("2.1.6","Check partialPublicVotingCredentials lenght","Check if s >= 1",'s',1),
            IterationTest("NumberOfCandidates","For j in {1,...,t} ",int_test_numberOfCandidates),
            IterationTest("NumberOfSelections","For j in {1,...,t} ",int_test_numberOfSelections),
        )
        integrity_tests.addTests(int_pre_election_tests)

        consistency_tests = MultiTest("3","Consistency Tests","Test which conntains all consistency tests")
        cons_pre_election_tests = MultiTest("3.1","pre_election Tests","Test which conntains all pre_election tests")
        cons_pre_election_tests.addTests(
            LenghtEqualityConsistenyTest("3.1.1","Check Number of selections","Check if numberOfSelections has the same lenght as numberOfCandidates","numberOfSelections","numberOfCandidates")
        )
        consistency_tests.addTests(cons_pre_election_tests)

        evidence_tests = MultiTest("4","Evidence Tests","Test which conntains all evidence tests")
        ev_check_proofs = MultiTest("4.1","Check all Proofs","Test which conntains all proofs tests")
        # Tests for IterationTests
        ev_test_ballotproof = BallotProofEvidenceTest("4.1.1","Check BallotProof","Check proof of Ballot","ballot")
        ev_check_proofs.addTests(
            IterationTest('ballots',"For all Ballots: ",ev_test_ballotproof)
        )
        evidence_tests.addTests(ev_check_proofs)

        authenticity_tests = MultiTest("5","Authenticiy Tests","Test which conntains all authenticiy tests")
        au_cert_tests = MultiTest("5.1","Check all Certificates","Test which conntains all certificate tests")
        au_cert_tests.addTests(
            CertificateAuthenticityTest("5.1.1","Check AdminCert","Check validity of Certificate of election administrator","certAdmin")
        )
        authenticity_tests.addTests(au_cert_tests)

        self.root_test.addTest(completness_tests)
        self.root_test.addTest(integrity_tests)
        self.root_test.addTest(consistency_tests)
        self.root_test.addTest(evidence_tests)
        self.root_test.addTest(authenticity_tests)

    def verify(self,data_dict,report):
        prepareData(data_dict)
        self.root_test.attachAll(report.observers)
        self.root_test.runTest(election_data,report)
