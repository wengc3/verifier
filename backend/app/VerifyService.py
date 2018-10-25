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
from app.verifier.IntegrityTest import VotingCircleIntegrityTest
from app.verifier.IterationTest import IterationTest

class VerifyService(object):
    """docstring for VerifyService."""
    def __init__(self):
        self.root_test = MultiTest("0","Root Test","Test which conntains all Tests")
        self.setUpTests()

    def setUpTests(self):

        test_electionID = SingleCompletnessTest("1.1","Check Election ID","Check if ElectionID is in election_data",'electionID')
        test_voterID = SingleCompletnessTest("1.10.1","Check Voter ID","For all ballots check if they have e voterID ",'voterId')
        iteration_test_voterID= IterationTest('ballots',test_voterID)
        completness_tests = MultiTest("1","Completness Tests","Test which conntains all completness tests")
        completness_tests.addTest(iteration_test_voterID)
        completness_tests.addTest(test_electionID)

        test_voting_circle = VotingCircleIntegrityTest("2.2","Check Voting Circle","Check integrity of voting circle",'countingCircles')
        integrity_tests = MultiTest("2","Integrity Tests","Test which conntains all integrity tests")
        integrity_tests.addTest(test_voting_circle)

        self.root_test.addTest(completness_tests)
        self.root_test.addTest(integrity_tests)

    def verify(self,election_data,report):
        Test.report = report
        self.root_test.runTest(election_data)
