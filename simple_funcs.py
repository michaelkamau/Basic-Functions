# Generate prime number up to n
def primes_to_n(limit):
    """
    Generates prime numbers up to n
    :param limit:
    :return: list of prime numbers
    """
    res = []

    for num in range(2, limit + 1):
        isPrime = True
        # test if num is prime
        for i in range(2, num):
            if num % i == 0:
                # num is not prime
                isPrime = False
                break
            else:
                continue
        if isPrime:
            res.append(num)
    return res


def fibs(terms):
    """
    Generates a list of Fibonacci nummbers with number of elements = terms
    :param terms:
    :return:
    """
    first = 0
    second = 1
    third = 0
    res = [first, second]
    for i in range(terms - 2):
        third = first + second
        res.append(third)
        first = second
        second = third
    return res
