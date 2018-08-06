"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
total = 0
for i in xrange(1,1000):
    if i % 3==0 and i % 5 ==0:
        total = total +i
        
print "by C coding", total

total = sum ( [i for i in xrange(1,1000) if i % 3 == 0 and i % 5 ==0 ])
print "by nested for",total

total = sum (filter( lambda i: i % 3 == 0 and i % 5 == 0,  xrange(1,1000)))
print "by lambda", total