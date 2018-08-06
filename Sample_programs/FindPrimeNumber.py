num=input("Please enter the value ");


def is_prime(x):
    for i in range(2, int(x ** 0.5)+1):
        if (x % i == 0): return False
    return True
print num,
if is_prime(num):
    print "is prime number "
else:
    print "is not a prime number"

    
