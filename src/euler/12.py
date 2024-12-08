import array
import math 
def get_prime_numbers_under_n(n: int) -> list[int]:
    OFFSET = 2
    candidates = array.array('Q', range(OFFSET,n))
    
    for i in range(len(candidates)):
        prime = candidates[i]
        if prime == 0:
            continue
        
        for j in range(i+1, len(candidates)):
            if (j + OFFSET) % prime == 0:
                candidates[j] = 0
    return [i for i in candidates if i != 0]

sieved_primes = get_prime_numbers_under_n(10_000)

def prime_factorize_number(n: int, sieved_primes: list[int]) -> dict[int, int]:
    factors: dict[int,int] = {}
    
    for prime in sieved_primes:
        if prime > n:
            break
        divided: int = 0
        while n % prime == 0:
            divided += 1
            n = int(n / prime)
        if divided != 0:
            factors[prime] = divided
        if n == 1:
            break  
    return factors

max_divisors = 1
for n in range(1, 1_000_000):
    factorized_n = prime_factorize_number(n, sieved_primes)
    factorized_n_plus_one = prime_factorize_number(n+1, sieved_primes)

    for key, value in factorized_n_plus_one.items():
        if key in factorized_n:
            factorized_n[key] += value
        else:
            factorized_n[key] = value

    factorized_n[2] -= 1
    if factorized_n[2] == 0:
        del factorized_n[2]
    
    number_of_divisors = math.prod([num_divided + 1 for num_divided in factorized_n.values()])
    max_divisors = max(max_divisors, number_of_divisors)
    if max_divisors > 500:
        triangular_number = int((n*(n+1)) / 2)
        print(n, triangular_number, max_divisors)
        break



