from fractions import Fraction
from functools import reduce

def generate_fraction(depth):
  return 1 + reduce(lambda frac, _: Fraction(1, 2 + frac), range(depth - 1), Fraction(1, 2))

total = 0
for i in range(1000):
  frac = generate_fraction(i)
  if len(str(frac.numerator)) > len(str(frac.denominator)):
    total += 1

print(total)
