from functools import reduce

concatinated_number = ''
i = 1
while len(concatinated_number) < 1000001:
    concatinated_number += str(i)
    i += 1

numbers = [int(concatinated_number[10**place - 1]) for place in range(7)]

print(reduce(lambda x, y: x * y, numbers, 1))