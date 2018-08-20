"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import time
max = input("Please enter the value ");
start_time = time.time()
up_time = 0
for num in range(1, int(max**.5)+1):
    for i in range(2, int(num**.5)+1):
        if ((num % i) == 0):
            break
    else:
        if (max % num == 0):
            print "======",num
    up_time = time.time()-start_time
    if (up_time > 20):
        print "stop ",num
        print up_time
        exit(1)
print "total time", up_time