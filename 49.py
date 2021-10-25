from typing import DefaultDict


is_prime = [False, False, True] + [True, False] * int(10**6 / 2)
four_digit_primes = []
for i in range(3, 10**4, 2):
  if is_prime[i]:
    if i >= 1000:
      four_digit_primes.append(i)
    for j in range(i*i, 10**6, 2*i):
      is_prime[j] = False

prime_permutations = DefaultDict(lambda: [])
for prime in four_digit_primes:
  prime_permutations[''.join(sorted(str(prime)))].append(prime)
prime_permutations = list(filter(lambda x: len(x) >= 3, prime_permutations.values()))


def check(primes, i, expected_diff):
  if i >= len(primes):
    return 0
  for j in range(i + 1, len(primes)):
    actual_diff = primes[j] - primes[i]
    if actual_diff == expected_diff:
      return check(primes, j, expected_diff) + 1

  return 0

for primes in prime_permutations:
  for i in range(1, len(primes)):
    for j in range(i+1, len(primes)):
      expected_diff = primes[j] - primes[i]

      c = check(primes, i, expected_diff)
      if c > 1:
        print(primes)
