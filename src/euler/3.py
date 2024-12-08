from math import sqrt, ceil

target = 600_851_475_143

def prime_factorize(n: int) -> set[int]:
    for i in range(3, ceil(sqrt(n))):
        if n % i == 0:
            return prime_factorize(n // i).union({i})
    return {n}

print(max(prime_factorize(target)))