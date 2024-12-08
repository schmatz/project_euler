def fib(l: int, r: int, max: int) -> set[int]:
    s = set((l,r))
    if l + r > max:
        return s
    return fib(r, l+r, max).union(s)


print(sum([x for x in fib(1,2, 4_000_000) if x % 2 == 0]))