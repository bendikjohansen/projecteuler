
pandigital_products = []
for n in range(10000):
    concatinated_product = ''
    for i in range(1, 50):
        if len(concatinated_product) + len(str(n * i)) > 9 or '0' in concatinated_product:
            break
        concatinated_product += str(n * i)
    
    if '0' not in concatinated_product and len(concatinated_product) == len(set(concatinated_product)) == 9:
        pandigital_products.append(int(concatinated_product))

print(max(pandigital_products))