import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import re
from app.utils.prepareData import prepareData
from app.VerifyService import VerifyService
from app.verifier.Report import Report
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3
from chvote.verifier.TestResult import TestResult
from chvote.verifier.MultiTest import MultiTest
from ConsoleView import ConsoleView
from VerifierSocket import init_socket, getData

HOST = '127.0.0.1'
PORT = 5000
secparams_dict = {1: secparams_l1, 2: secparams_l2, 3: secparams_l3}

def getTest(root_test,id):
    points = id.count('.')
    category = find_test(root_test,id[0])
    if points == 0:
        return category
    phase = find_test(category,id[:3])
    if points == 1:
        return phase
    else:
        test = find_test(phase,id)
        root_node = MultiTest("0:","Root Test","Test which conntains all Tests")
        root_node.addTest(test)
        return root_node

def find_test(test,id):
    return next(child for child in test.test_list if child.id == id)

def run_sub_tests(root_test,test_list,data_dict):
    for id in test_list:
        test = getTest(root_test,id)
        test.runTest(data_dict)

def getSecparams(data_dict):
    sec_level = data_dict['securityLevel']
    return secparams_dict[sec_level]

def id_arg(value):
    if not re.match('[1-9](\.[1-9]){0,2}',value):
        raise argparse.ArgumentTypeError("testID has wrong format")
    return value

# Parse command line arguments
parser = argparse.ArgumentParser(description='verify election')
parser.add_argument('electionID', metavar='', type=str,
                    help='Unique election event identifier')
parser.add_argument('--step', type=float, metavar='', default=0.2,
                    help='define in which distance the progress will printed, default every 20%%')
parser.add_argument('--depth',type=int, metavar='', default=5,
                    help='set the depth of tree, which will printed, default=5')
parser.add_argument('--test',metavar='id', type=id_arg, nargs='+',
                    help='use this for runing only a certain tests ,Format: [1-9](\.[1-9]){0,2}')
parser.add_argument('--data',action='store_true',
                    help='append the test_data')
args = parser.parse_args()


def main():
    """ptionally runs only subtree,
       start verifier and print result."""
    init_socket(HOST,PORT,args.electionID)
    data_dict = getData()
    secparams = getSecparams(data_dict)
    report = Report(args.electionID)
    console = ConsoleView(step=args.step,depth = args.depth,data=args.data)
    report.attach(console)
    verify_svc = VerifyService.getInstance()
    if args.test:
        TestResult.setReport(report)
        data_dict = prepareData(data_dict,secparams)
        run_sub_tests(verify_svc.root_test,args.test,data_dict)
    else:
        verify_svc.verify(data_dict,report,secparams)



if __name__ == '__main__':
    main()
