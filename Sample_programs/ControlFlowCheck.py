"""
    sample program to find the flow 
"""
# def aaa(a):
#     print "in a",a;
#     def bbb(b):
#         print "in b", b
#         return bbb
#     return bbb
# 
# print "start"
# x = aaa("A")
# x(5)

def adding(x):
    print "adding"
    return x

@adding
def sum(): print "cc"

sum()
