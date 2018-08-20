import sys

if len(sys.argv) != 3: 
    print "give 2 values"
    exit(1)
source_file, des_file = sys.argv[1:]

with open(source_file) as sf, open(des_file,"w") as df:
#     for sf_line in sf.readlines():
#         df.write(sf_line)
    df.write(sf.read())