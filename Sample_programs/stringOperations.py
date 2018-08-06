data = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
     """
b = []
from string import ascii_lowercase
for c in data:
    if c in ascii_lowercase:
        a = ord(c)
        a += 2
        if a > 121: a -= 26
        b.append(ascii_lowercase[a-97])
    else :
     b.append(c)
     
print "".join(b)

f = []
#f = ascii_lowercase.append(ascii_lowercase.append(ascii_lowercase.pop()).pop())

f = ascii_lowercase[2:]+"ab"

from string import maketrans
aasd  = maketrans(ascii_lowercase, f )
print data.translate(aasd)