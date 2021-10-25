from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def is_divisble(number):
  for i in range(1, len(number) - 2):
    sub_number = int(number[i:i+3])
    prime = primes[i - 1]

    if sub_number % prime != 0:
      return False
  return True

digits = '1234567890'
substr_divisble_numbers = [int(''.join(number)) for number in permutations(digits, 10) if is_divisble(''.join(number))]

print(sum(substr_divisble_numbers))
