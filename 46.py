from math import sqrt

is_prime = [False, False, True] + [True, False] * int(10**6 / 2)
for i in range(3, 10**6, 2):
  if is_prime[i]:
    for j in range(i*i, 10**6, 2*i):
      is_prime[j] = False

found_smallest = False
i = 3
while not found_smallest:
  i += 2
  found_smallest = True
  for j in range(0, int(sqrt(i))):
    number = i - 2 * j**2
    if is_prime[number]:
      found_smallest = False
      break

print(i)
