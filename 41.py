from math import sqrt
from itertools import permutations

# limit = 10**8
# is_prime = [False, False, True] + [True, False] * int(limit / 2)

# for i in range(3, int(sqrt(limit) / 2)):
#     if is_prime[i]:
#         for j in range(i*i, limit, 2*i):
#             is_prime[j] = False

# print(f'found primes {len(is_prime)}')

for i in range(1,10,1):
    digits = ''.join('123456789'[:i])

    for n in permutations(digits, i):
        number = int(''.join(n))
        if number % 2 == 0:
            continue
        print(sqrt(number))