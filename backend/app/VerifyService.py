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

class VerifyService(object):
    """docstring for VerifyService."""
    def __init__(self, election_data,return_methode):
        Test.return_methode = return_methode
        self.election_data = election_data
        self.root_test = MultiTest("0","Root Test","Test which conntains all Tests",self.election_data)
        self.setUpTests()

    def setUpTests(self):
        completness_tests = MultiTest("1","Completness Tests","Test which conntains all Completness tests",
                                      self.election_data)
        test_electionID = SingleCompletnessTest("1.1","Check Election ID","Check if ElectionID is in election_data",
                                        self.election_data,['electionID'])
        completness_tests.addTest(test_electionID)
        self.root_test.addTest(completness_tests)
        
        test_w = VotingCircleIntegrityTest("2.2","Check Voting Circle","Check integrity of voting circle",
                                           self.election_data,['countingCircles'])

    def runTest(self):
        self.root_test.runTest()
