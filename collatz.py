# The number we will perform the collatz operation on. practice

n = 22

while n != 1:
    print(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1

print(n)
