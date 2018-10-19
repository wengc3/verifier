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
from app.verifier.CompletnessTest import SingleCompletnessTest
electionID1="5bc6062b6d19d200125b3fb7"
client = MongoClient()
db = client.chvote
bb = db.bulletinBoardStates.find_one({'election':electionID1})
ea = db.electionAdministratorStates.find_one({'election':electionID1})
bb_state = pickle.loads(bb['state'])
ea_state = pickle.loads(ea['state'])

dict = bb_state.__dict__
dict.update(ea_state.__dict__)

test_electionID = SingleCompletnessTest(1.1,"Check for Election ID","Check if ElectionID is in dict",
                                        dict,['electionID'])
res = test_electionID.runTest()
print(test_electionID.title,":",res)
