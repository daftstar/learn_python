def genPrimes():
    """
    genPrimes returns infinite sequence of
    prime numbers on successive calls to its next() method:
        2, 3, 5, 7, 11, ...

    Inputs: None:
    Outputs: Sequence of prime numbers
    """
    primes_list = []    # list of prime numbers
    test_number = 1     # set starting point

    while True:
        # we know 1 isn't a prime number, so start at 2
        test_number += 1

        for p in primes_list:
            if test_number % p == 0:
                break   # breaks loop, skips else clause, increments by 1

        # Else clause executed when the loop terminates
        # through exhaustion of the list but not
        # when the loop is terminated by a break statement.
        else:
            primes_list.append(test_number)
            yield test_number


prime = genPrimes()

for i in range(45):
    print (prime.__next__())
