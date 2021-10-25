is_prime = [False, False, True] + [True, False] * int(10**6 / 2)
primes = [2]
prime_set = set([2])
for i in range(3, 10**6, 2):
  if is_prime[i]:
    primes.append(i)
    prime_set.add(i)
    for j in range(i*i, 10**6, 2*i):
      is_prime[j] = False

longest_sum_prime = 2
primes_used = []
for i in range(len(primes)):
  prime_sum = primes[i]
  temp = [primes[i]]
  for j in range(i+1,len(primes)):
    prime_sum += primes[j]
    temp.append(primes[j])

    if prime_sum > 10**6:
      break

    if prime_sum in prime_set and len(temp) > len(primes_used):
      primes_used = temp.copy()
      longest_sum_prime = prime_sum

print(longest_sum_prime)
