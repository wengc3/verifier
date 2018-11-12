from gmpy2 import mpz
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# for urlencoded
import os, sys
import pickle
import inspect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chvote.Common.SecurityParams import secparams_l1, secparams_l2, secparams_l3
from app.verifier.Test import Test
from app.verifier.MultiTest import MultiTest
from app.verifier.CompletnessTest import SingleCompletnessTest
from app.verifier.IntegrityTest import VotingCircleIntegrityTest, PubKeyIntegritiyTest
from app.verifier.IterationTest import IterationTest
from app.verifier.ConsistencyTest import LenghtEqualityConsistenyTest
from app.verifier.EvidenceTest import BallotProofEvidenceTest
from app.verifier.AuthenticityTest import CertificateAuthenticityTest

class VerifyService(object):
    """docstring for VerifyService."""
    def __init__(self):
        self.root_test = MultiTest("0","Root Test","Test which conntains all Tests")
        self.setUpTests()

    def setUpTests(self):

        completness_tests = MultiTest("1","Completness Tests","Test which conntains all completness tests")
        com_test_electionID = SingleCompletnessTest("1.1.1","Check Election ID","Check if ElectionID is in election_data",'electionID')
        com_test_numberOfCandidates =SingleCompletnessTest("1.1.2","Check Number of candidates","Check if vector numberOfCandidates is in election_data",'numberOfCandidates')
        com_test_candidates= SingleCompletnessTest("1.1.3","Check Candidates","Check if vector candidates is in election_data",'candidates')
        com_test_numberOfSelections = SingleCompletnessTest("1.1.4","Check Number of selections","Check if vector numberOfSelections is in election_data",'numberOfSelections')
        com_test_voters = SingleCompletnessTest("1.1.5","Check Voters","Check if vector voters is in election_data",'voters')
        com_test_countingCircles = SingleCompletnessTest("1.1.6","Check CountingCircles","Check if vector countingCircles is in election_data",'countingCircles')
        com_test_eligibilityMatrix = SingleCompletnessTest("1.1.6","Check EligibilityMatrix","Check if eligibilityMatrix is in election_data",'eligibilityMatrix')
        com_test_publicVotingCredentials = SingleCompletnessTest("1.1.7","Check Public voting credentials","Check if vector partialPublicVotingCredentials is in election_data",'partialPublicVotingCredentials')
        com_test_voterID = SingleCompletnessTest("1.2.1.1","Check Voter ID","For all ballots check if they have e voterID ",'voterId')
        com_iteration_test_voterID= IterationTest('ballots',"For all Ballots: ",com_test_voterID)
        completness_tests.addTest(com_test_electionID)
        completness_tests.addTest(com_test_numberOfCandidates)
        completness_tests.addTest(com_test_candidates)
        completness_tests.addTest(com_test_numberOfSelections)
        completness_tests.addTest(com_test_voters)
        completness_tests.addTest(com_test_eligibilityMatrix)
        completness_tests.addTest(com_test_publicVotingCredentials)
        completness_tests.addTest(com_test_countingCircles)
        completness_tests.addTest(com_iteration_test_voterID)

        integrity_tests = MultiTest("2","Integrity Tests","Test which conntains all integrity tests")
        int_test_voting_circle = VotingCircleIntegrityTest("2.1.2","Check Voting Circle","Check integrity of voting circle",'countingCircles')
        int_test_pk = PubKeyIntegritiyTest("2.1.15","Check Public key","For all authority test it's Public key",'pk_j')
        int_iteration_test_pk = IterationTest("publicKeyShares","For j in {1,...,s} ",int_test_pk)
        integrity_tests.addTest(int_test_voting_circle)
        integrity_tests.addTest(int_iteration_test_pk)

        consistency_tests = MultiTest("3","Consistency Tests","Test which conntains all consistency tests")
        cons_test_numberOfSelection=LenghtEqualityConsistenyTest("3.1.1","Check Number of selections","Check if numberOfSelections has the same lenght as numberOfCandidates","numberOfSelections","numberOfCandidates")
        consistency_tests.addTest(cons_test_numberOfSelection)

        evidence_tests = MultiTest("4","Evidence Tests","Test which conntains all evidence tests")
        ev_test_ballotproof = BallotProofEvidenceTest("4.1","Check BallotProof","Check proof of Ballot","ballot")
        ev_iteration_test_ballotproof = IterationTest('ballots',"For all Ballots: ",ev_test_ballotproof)
        evidence_tests.addTest(ev_iteration_test_ballotproof)

        authenticity_tests = MultiTest("5","Authenticiy Tests","Test which conntains all authenticiy tests")
        au_test_admin_cert = CertificateAuthenticityTest("5.1.1","Check AdminCert","Check validity of Certificate of election administrator","certAdmin")
        authenticity_tests.addTest(au_test_admin_cert)

        self.root_test.addTest(completness_tests)
        self.root_test.addTest(integrity_tests)
        self.root_test.addTest(consistency_tests)
        self.root_test.addTest(evidence_tests)
        self.root_test.addTest(authenticity_tests)

    def prepareData(self,data_dict):
        vector = data_dict['publicKeyShares']
        for index,item in enumerate(vector):
            vector[index]={'pk_j':item}
        data_dict['publicKeyShares'] = vector
        return data_dict

    def verify(self,data_dict,report):
        election_data = self.prepareData(data_dict)
        self.root_test.attachAll(report.observers)
        self.root_test.runTest(election_data,report)
