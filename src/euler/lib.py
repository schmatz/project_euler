from math import ceil, sqrt

# TODO: There are so many more efficient ways to do prime factorization, rewrite library method
def prime_factorize(n: int) -> set[int]:
    for i in range(3, ceil(sqrt(n))):
        if n % i == 0:
            return prime_factorize(n // i).union({i})
    return {n}

def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0 and n != i:
            return False
        
    return True