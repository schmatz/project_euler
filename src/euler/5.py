import math 

for i in range(20, math.prod(range(1,20))):
    for j in range(1, 20 + 1):
        if i % j != 0:
            break
    else:
        print(i)
        break

    