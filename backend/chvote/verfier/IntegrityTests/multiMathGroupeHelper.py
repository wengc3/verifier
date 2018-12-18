from gmpy2 import mpz
from chvote.Common.IsMemberOfGroupe import IsMemberOfGroupe

def multiMathGroupeHelper(vector,rng,param):
    try:
        for j in range(rng):
            if not IsMemberOfGroupe(mpz(vector[j]),param):
                return False
        return True
    except IndexError:
        return False
