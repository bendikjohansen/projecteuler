
def triangle(n): return int(n * (n + 1) / 2)
def pentagonal(n): return int(n * (3*n - 1) / 2)
def hexagonal(n): return int(n * (2*n - 1))

p_numbers = set()
h_numbers = set()
found = 0

i = 1
while found < 3:
  t_number, p_number, h_number = triangle(i), pentagonal(i), hexagonal(i)
  p_numbers.add(p_number)
  h_numbers.add(h_number)

  if t_number in p_numbers and t_number in h_numbers:
    print(t_number)
    found += 1

  i += 1
