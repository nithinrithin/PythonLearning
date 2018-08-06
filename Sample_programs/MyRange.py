"""
    Myramge - it is my own range function
    
    Its a nithin program    
"""
def myrange(end, start=0, jump=1):
    """
        It take three values at most. 
        start -> from where range start
        end -> in where range end
        jump -> increment factor
    """
    if end < start: start,end = end,start
    else: raise TypeError("start is greter than end")
    while start < end:
        yield start
        start = start+jump

num = input("please enter the value")
#myrange()
myrange(num) 
myrange(num ,10)
itr = myrange(num, 10, 2)
for each in itr: print each,    

help(myrange)   
