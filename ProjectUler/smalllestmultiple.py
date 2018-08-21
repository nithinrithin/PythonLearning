"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
#         num = input("Please enter a number")
result = None
import time
start = time.time()
for num in xrange(1,20):
    for i in xrange(num,232792561,num):
        result = set()
        for div in xrange(num,0,-1):
            if i % div != 0:
                break
            else:
                result.add(div)
        if len(result) == num:
            print num,"->",i
            break
    else:
        print i
print time.time()-start