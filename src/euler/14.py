import functools

@functools.cache
def collatz_sequence(start: int) -> list[int]:
    seq: list[int] = [start]
    while start != 1:
        if start % 2 == 0:
            start //= 2
        else:
            start = 3 * start + 1
        seq.extend(collatz_sequence(start))
        return seq
    
    return seq

seq_13 = collatz_sequence(13)
assert seq_13 == [13,40,20,10,5,16,8,4,2,1]

longest_seq = 1
for i in range(2, 1_000_000):
    seq = collatz_sequence(i)
    if len(seq) > longest_seq:
        print("Sequence", i, "has length", len(seq))
        longest_seq = len(seq)
    
