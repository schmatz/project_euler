from math import sqrt, ceil

def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0 and n != i:
            return False
        
    return True

assert(is_prime(2))
assert(is_prime(5))
assert(not is_prime(6))
assert(is_prime(7))

primes: set[int] = set()

candidate = 2
while len(primes) < 10_001:
    if is_prime(candidate):
        primes.add(candidate)
    candidate += 1

print(sorted(primes)[-1])
