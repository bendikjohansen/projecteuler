
numbers = []
for i in range(10**6):
    n_dec = str(i)
    n_bin = str(bin(i))[2:]
    if n_dec == ''.join(reversed(n_dec)) and n_bin == ''.join(reversed(n_bin)):
        numbers.append(i)

print(sum(numbers))
