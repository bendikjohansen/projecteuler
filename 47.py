from math import sqrt

is_prime = [False, False, True] + [True, False] * int(10**6 / 2)
primes = [2]
for i in range(3, 10**6, 2):
  if is_prime[i]:
    primes.append(i)
    for j in range(i*i, 10**6, 2*i):
      is_prime[j] = False


def find_factors(n):
  i = 0
  factors = set()
  number = n

  while primes[i] < sqrt(number):
    while number % primes[i] == 0:
      factors.add(primes[i])
      number = int(number / primes[i])
    i += 1
  factors.add(number)
  return factors



consecutives = 4
found_consecutive = False
i = 0
while not found_consecutive:
  i += 1

  found_consecutive = True
  consecutive_count = 0
  for j in range(consecutives):
    num = i + j

    if is_prime[num]:
      i = num
      found_consecutive = False
      break

    if len(find_factors(num)) == consecutives:
      consecutive_count += 1
    else:
      found_consecutive = False
      i = num
      break

print(i)
