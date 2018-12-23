import os, sys
from gmpy2 import mul
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from chvote.Common.SecurityParams import secparams_l1,secparams_l2,secparams_l3

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate
from chvote.Common.GetPrimes import GetPrimes

def sum_elig_matrix(matrix,numberOfSelections,t,i):
    return sum([matrix[i][j]*numberOfSelections[j] for j in range(t)])

def prime_prod(primes,k_prime,n):
    prime_list = primes[n-k_prime + 1:n - 1]
    product = 1
    for item in prime_list:
        product = item * product
    return product

class PrimeConsistencyTest(SingleTest):
    """
    docstring for PrimeConsistenyTest.
    """

    @completness_decorate
    def runTest(self,election_data):
        """
        Check if p_n+w * prod(list) < p.
        >>> res = pct.runTest({'numberOfSelections': [{'k_j': 1}], 't': 1, 'w': 1, 'n': 3, 'Ne': 3, 'eligibilityMatrix': [{'e_i': [True]}, {'e_i': [True]}, {'e_i': [True]}], 'secparams': secparams_l3})
        >>> res.test_result
        'successful'
        """
        try:
            numberOfSelections = [elem['k_j']for elem in self.test_data]
            Ne = election_data['Ne']
            t = election_data['t']
            n = election_data['n']
            w = election_data['w']
            elig_matrix = [elem['e_i'] for elem in election_data['eligibilityMatrix']]
            k_prime = max([sum_elig_matrix(elig_matrix,numberOfSelections,t,i) for i in range(Ne)])
            param = election_data['secparams']
            primes = GetPrimes(n+w,param)
            p_prod = primes[-1]*prime_prod(primes,k_prime,n)
            return 'successful' if p_prod < param.p else 'failed'
        except KeyError:
            return 'skipped'

if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    doctest.testmod(extraglobs={'pct': PrimeConsistenyTest("1.1","TEST","TEST",["numberOfSelections"])})
