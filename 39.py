from math import sqrt
from collections import Counter

numbers = [n**2 for n in range(1, 1000)]

p_values = []
for a in numbers:
    for b in numbers:
        if a + b in numbers:
            p_values.append(sqrt(a) + sqrt(b) + sqrt(a + b))

print(Counter(p_values).most_common()[2][0])
