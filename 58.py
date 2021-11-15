def generate_primes(limit):
  is_prime = [False, False, True] + [True] * limit
  primes = [2]
  for i in range(3, limit, 2):
    if is_prime[i]:
      primes.append(i)
      for j in range(i*i, limit, 2*i):
        is_prime[j] = False
  return primes


def generate_diagonals(limit):
  diagonals = [1, 1, 1]
  for n in range(limit):
    diagonals = [diagonal + (index + 1) * 2 + n * 8 for index, diagonal in enumerate(diagonals)]
    yield diagonals


def is_prime(number, primes):
  number_sqrt = number**0.5
  for prime in primes:
    if number % prime == 0:
      return False
    if number_sqrt < prime:
      return True
  return False


primes = generate_primes(10**6)
diagonal_primes_count = 0
side_length = 1
total_diagonals = float(1)
print(total_diagonals)
for diagonals in generate_diagonals(100000):
  side_length += 2
  total_diagonals += 4
  for diagonal in diagonals:
    if is_prime(diagonal, primes):
      diagonal_primes_count += 1

  print(total_diagonals)
  if diagonal_primes_count / total_diagonals < 0.10:
    break

print(side_length)
