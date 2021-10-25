from math import factorial

def digit_factorial(n):
    return sum([factorial(int(m)) for m in str(n)])

print(sum([n for n in range(3, 100000) if n == digit_factorial(n)]))
        