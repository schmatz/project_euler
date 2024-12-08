from euler.lib import is_prime

print(sum([x for x in range(2, 2_000_000) if is_prime(x)]))
