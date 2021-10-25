from itertools import permutations

products = set()

for perm in permutations('123456789', 5):
    for k in range(1, 5):
        a, b = perm[:k], perm[k:]
        i, j = ''.join(a), ''.join(b)
        product = int(i) * int(j)
        digits = i + j + str(product)
        if '0' not in digits and len(digits) == 9 and len(set(digits)) == 9:
            products.add(product)

print(sum(products))
