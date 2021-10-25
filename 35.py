from itertools import cycle

def erat(n):
    primes = [2]
    is_prime = [False, False, True] + [True] * n
    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n, 2*i):
                is_prime[j] = False
    return primes

primes = erat(10**6)

circular_primes = []
for p in primes:
    ps = str(p)
    
    is_circular = True
    for i in range(len(ps)):
        num = int((ps + ps)[i:i+len(ps)])
        
        is_circular = num in primes
        if not is_circular:
            break

    if is_circular:
        circular_primes.append(p)

print(len(circular_primes))    
        
