from itertools import combinations_with_replacement

numbers = range(10000)
def is_lychrel(number, i = 0):
  if i >= 50:
    return True
  if number == number[::-1] and i != 0:
    return False

  n, rn = int(number), int(number[::-1])
  return is_lychrel(str(n + rn), i+1)

print(sum([1 for number in numbers if is_lychrel(str(number))]))
