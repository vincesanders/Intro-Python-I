import sys
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    ### We don't want to check higher that this
    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        ### If n is divisible by the divisor, it is not a prime
        if n % divisor == 0:
            return False
    return True
if len(sys.argv) < 2:
    print('You need to type a number in the command line after you call the file.')
else:
    n = int(sys.argv[1])
    result = is_prime(n)
    if result:
        print(f'{n} is a prime number.')
    else:
        print(f'{n} is NOT a prime number.')