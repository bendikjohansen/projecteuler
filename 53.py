from math import comb, factorial

count = 0
for n in range(1, 101):
    n_fac = factorial(n)
    break_early = False
    for r in range(1, n + 1):
        r_fac = factorial(r)
        rn_fac = factorial(n - r)

        combinations = int(n_fac/(r_fac * rn_fac))
        if combinations > 10**6:
            count += 1
            break_early = True
        if combinations < 10**6 and break_early:
            break

print(count)