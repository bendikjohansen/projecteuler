def generate_primes():
    limit = 10**6
    is_prime = [False, False, True] + [True, False] * int(limit / 2)
    primes = [2]

    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit, 2*i):
                is_prime[j] = False

    return primes, is_prime

def is_truncatable_prime(is_prime, number):
    number_str = str(number)
    truncated_numbers = ([int(number_str[i:]) for i in range(len(number_str))] 
        + [int(number_str[:-i]) for i in range(1, len(number_str))]
    )
    return all([is_prime[number] for number in truncated_numbers])

primes, is_prime = generate_primes()
truncatable_primes = []
for prime in primes[4:]:
    if is_truncatable_prime(is_prime, prime):
        truncatable_primes.append(prime)

print(sum(truncatable_primes))