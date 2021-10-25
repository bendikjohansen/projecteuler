from collections import defaultdict
from itertools import combinations

limit = 10**6
is_prime = [False, False, True] + [True, False] * int(limit / 2)
primes = [2]
primes_set = set()

for i in range(3, limit, 2):
    if is_prime[i]:
        if i > 10000:
            primes_set.add(i)
            primes.append(i)
        for j in range(i*i, limit, 2*i):
            is_prime[j] = False

hashed_primes = defaultdict(lambda: 0)
hashed_primes_src = defaultdict(lambda: [])
for prime in primes:
    prime_str = str(prime)
    for i, j, k in combinations(range(len(prime_str)), 3):
        if prime_str[i] != prime_str[j] or prime_str[i] != prime_str[k]:
            continue

        hash = f'{prime_str[:i]}x{prime_str[i+1:j]}x{prime_str[j+1:k]}x{prime_str[k+1:]}'
        if hash == prime_str:
            continue

        hashed_primes[hash] += 1
        hashed_primes_src[hash].append(prime)

hash = max(hashed_primes, key=hashed_primes.get)
print(min(hashed_primes_src[hash]))