from itertools import permutations
from math import sqrt


def is_prime(number):
  if number % 2 == 0:
    return False

  for num in range(3, int(sqrt(number)), 2):
    if number % num == 0:
      return False

  return True


digits = '987654321'

for number_of_digits in range(9, 0, -1):
  pandigital_digits = digits[9-number_of_digits:]
  digit_permutations = permutations(pandigital_digits, len(pandigital_digits))

  for digit_array in digit_permutations:
    number = int(''.join(digit_array))
    if is_prime(number):
      print(number)
      exit()
