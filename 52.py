
a = 1
while True:
    multiples = [2*a,3*a,4*a,5*a,6*a]
    
    if all([sorted(str(a)) == sorted(str(b)) for b in multiples]):
        break
    
    a += 1

print(a)