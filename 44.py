
def generate_pentagonal_number(n): return int(n*(3*n-1) / 2)

numbers = [1]
numbers_set = set()
i = 2
last_number = 1
d_numbers = set()
while i < 10000:
  number = generate_pentagonal_number(i)
  for previous in reversed(numbers):
    second_previous = number - previous
    if second_previous > last_number:
      break
    if second_previous not in numbers_set:
      continue
    prev_diff = abs(previous - second_previous)
    if prev_diff in numbers_set:
      d_numbers.add(prev_diff)

  numbers.append(number)
  numbers_set.add(number)
  last_number = number
  i += 1

print(d_numbers)
