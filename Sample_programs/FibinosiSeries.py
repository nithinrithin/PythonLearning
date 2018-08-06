print "Program Starts"
num = input("Please enter the max limit of series:")
x = 0
y = 1
for i in range(num):
    print x,
    x, y = y, x+y
    
    