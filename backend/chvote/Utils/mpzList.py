from gmpy2 import mpz

def mpzList(data_list):
    """
    Transform a list with numbers to a list with mpz values
    """
    return [mpz(item) for item in data_list]
