from itertools import combinations_with_replacement
from functools import reduce
import operator

bawkie = set(combinations_with_replacement([1,1,0,0], 2))
shn = []
for num in range(10, 101):
    for den in range(10, 101):
        if num != den and not '0' in str(num) and not '0' in str(den):
            a, b = str(num), str(den)

            for (i, j) in bawkie:
                if a[i] == b[j] and int(a[j]) / int(b[i]) == num / den:
                    print(a[j], b[i], num, den)
                    shn.append(num / den)

print(reduce(operator.mul, shn, 1))