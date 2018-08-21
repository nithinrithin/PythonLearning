"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def getDivisor(pn):
    for i in range(999,100,-1):
        if (pn % i) == 0:
            val = pn / i
            if len(str(val)) == 3:
                print "%d * %d = %d"%(i,val,pn)
                
                

for i in range(9,1,-1):
    for j in range(9,1,-1):
        for k in range(9,1,-1):
            num = str(i)+str(j)+str(k)
            pn =  int(num+num[::-1])
            getDivisor(pn)