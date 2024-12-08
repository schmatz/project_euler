def find_triple_with_sum(s: int) -> int | None:
    for c in range(3, s):
        for b in range(2, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2 and a + b + c == s:
                    print(a,b,c)
                    return a * b * c
    return None

print(find_triple_with_sum(1000))
                    