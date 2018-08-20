"""
    program to solve sudoko
"""

#[[],[],[],[],[],[],[],[],[]]
suduko = [  [4,1,8,3,0,0,0,0,6],
            [0,0,0,8,4,0,0,5,0],
            [0,0,0,0,9,0,8,0,7],
            [3,0,0,0,2,5,1,0,0],
            [0,8,5,0,0,0,7,6,0],
            [0,0,4,1,7,0,0,0,3],
            [9,0,2,0,8,0,0,0,0],
            [0,7,0,0,6,2,0,0,0],
            [8,0,0,0,0,3,2,7,9]
            ]
# sk = suduko

"""pro"""
suduko = [  [0,2,8,0,7,5,0,1,0],
            [6,0,7,0,0,8,0,0,0],
            [0,5,0,0,0,0,0,0,0],
            [0,9,7,8,0,0,0,5,0],
            [0,7,0,0,6,0,0,3,0],
            [0,8,0,0,5,1,7,0,0],
            [0,0,0,0,0,0,0,2,0],
            [0,0,0,4,0,0,8,0,1],
            [0,4,0,8,1,0,3,7,0],
    ]
sk = suduko

"""hard"""
suduko = [  [0,0,8,0,6,0,0,0,2],
            [0,0,0,2,0,0,0,0,7],
            [2,0,0,4,0,5,0,0,0],
            [0,2,0,6,3,0,5,1,0],
            [0,0,0,5,0,1,0,0,0],
            [0,5,7,0,4,9,0,2,0],
            [0,0,0,7,0,6,0,0,3],
            [8,0,0,0,0,2,0,0,0],
            [9,0,0,0,8,0,7,0,0],
    ]
# sk = suduko
"""hardest"""
suduko = [  [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0],
    ]
# sk = suduko
groups = []
skt = zip(*sk)
logger = False
isSolved = False
from collections import OrderedDict
findsMap = OrderedDict()

if logger:
    print "="*10+"Input"+"="*10
    for i in range(9): print sk[i]
    print "="*30

def check_logger(fun):
    if logger:
        return fun
    else:
        def dummy():pass
        return dummy

#@check_logger
def printfullMatrix(sk):
    print "="*10+"matrix"+"="*10
    for i in range(9):
        for j in range(9):
            if sk[i][j]:
                print str(sk[i][j])+" ",
            else:
                print "* ",
        print ""
    print "="*30
    
@check_logger
def printGroupCreation():
    print "="*10+"group"+"="*10
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    print str(sk[k+(i*3)][l+(j*3)])+" ",
                print ""

def create_groups():
    print "="*10+"save group"+"="*10
    group_list = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    group_list.append(sk[k+(i*3)][l+(j*3)])
            if logger:
                print group_list
            groups.append(group_list)
            group_list = []
    print "="*30

def create_findsmap():
    for i in range(9):
        for j in range(9):
            if sk[i][j] == False:
                try:
                    val = level1solver(i,j, sk, skt)
                    findsMap.update({str(i)+str(j):val})
                except  StopIteration:
                    print "check log"
@check_logger
def printGroup():
    print "="*10+"print group"+"="*10
    for i in groups : print i
    print "="*10+"processing"+"="*10

def printFindsMap(d):
    print "="*10+"printing answers map"+"="*10
    for item in d.items(): print item
    print "----",len(d),"----"
    print "="*30

@check_logger
def get_from_map(i,j):
    key = str(i)+str(j)
    return findsMap.get(key)

@check_logger
def printProcessResult():
    print "="*10+"printing final answer"+"="*10
    for i in range(9):
        for j in range(9):
            if sk[i][j] == False:
                print get_from_map(i,j),
            else:
                print sk[i][j],
        print ""

    
def printSolverBreaker():
    for i in range(9):
        for j in range(9):
            key = str(i)+str(j)
            if key in findsMap.keys():
                print key,"-->",findsMap.get(key)

# def findMissingValue(i, j, matrix, tmatrix):
#     
#     group_index = (i-(i%3))+(j/3)
#     
#     from itertools import chain
#     existing = set(chain(chain(groups[group_index],
#                             matrix[i][:], tmatrix[j][:])))
#     
#     tmpValues =  [x for x in xrange(1,10)
#                    if x not in existing]
#     
#     if logger:
#         print "index->",i,j
#         print "group index",group_index
#         print "group", groups[group_index]
#         print "i->",matrix[i][:]
#         print "j->",tmatrix[j][:]
#         print "existing->",existing
#         print "temp - >", tmpValues
#         print findsMap
#     if len(tmpValues) == 0:
#         raise StopIteration, "pothum"
#     
#     return tmpValues

def solver(item, matrix):
    key, value = item
    tmatrix = zip(*matrix)
    i = int(key[0])
    j = int(key[1])
    group_index = (i-(i%3))+(j/3)
    group_value_index = (i%3)+(2*(i%3))+(j%3)
    is_updated = False
    if value.__len__() == 1:
        if matrix[i][j] == 0:
            matrix[i][j] = value[0]
            groups[group_index][group_value_index] = value[0]
            print "At1 [{0:d}][{1:d}] -> {2:d}".format(i,j,value[0])
            del findsMap[key]
            is_updated = True
    else:
        try:
            tmp = level1solver(i, j, matrix, tmatrix)
#             print key,"-l1-->",tmp
            if findsMap[key] != tmp:
                findsMap.update({str(i)+str(j):tmp})
        except: StopIteration, "hold it"
    
    if len(findsMap) == 0:
        print "\n"+"_"*5+"Solved Success!"+"_"*5+"\n"

    if not is_updated:
#         print "\n"+"_"*5+"Calling level 2!"+"_"*5+"\n"
        tmp  = level2solver(key, matrix, tmatrix)
        if tmp is None:
            return matrix
        if len(tmp) == 1:
            matrix[i][j] = tmp[0]
            groups[group_index][group_value_index] = value[0]
            print "at2 [{0:d}][{1:d}] -> {2:d}".format(i,j,value[0])
            del findsMap[key]
        else:
            print "l2:",findsMap[key],tmp
            if findsMap[key] != tmp:
                findsMap.update({str(i)+str(j):tmp})
        print tmp
        
    return matrix

def level1solver(i, j, matrix, tmatrix):
#     print "="*10+"Level 1"+"="*10
    group_index = (i-(i%3))+(j/3)
    
    from itertools import chain
    existing = set(chain(chain(groups[group_index],
                            matrix[i][:], tmatrix[j][:])))
    
    tmpValues =  [x for x in xrange(1,10)
                   if x not in existing]
    
    if logger:
        print "index->",i,j
        print "group index",group_index
        print "group", groups[group_index]
        print "i->",matrix[i][:]
        print "j->",tmatrix[j][:]
        print "existing->",existing
        print "temp - >", tmpValues
        print findsMap
    if len(tmpValues) == 0:
        raise StopIteration, "pothum"
    
    return tmpValues
                
def level2solver(key, matrix, tmatrix):
#     print "="*10+"Level 2"+"="*10
#         print key,value
    i = int(key[0])
    j = int(key[1])
    row = [[1,2,3],[4,5,6],[7,8,9]]
    clm = [[1,2,3],[4,5,6],[7,8,9]]
    rv = row[i/3]
    cv = clm[j/3]
    del rv[i%3]
    del cv[j%3]
    group_index = (i-(i%3))+(j%3)
    commonRowsValues = set(matrix[rv[0]-1]).intersection(set(matrix[rv[1]-1]))
    commonClmValues = set(tmatrix[cv[0]-1]).intersection(set(tmatrix[cv[1]-1]))
    avail_values = commonRowsValues.intersection(commonClmValues)
    avail_values = avail_values.difference(set(groups[group_index]))
    avail_values = avail_values.intersection(findsMap[key])
    if key=='27':
        print "========",i,j,findsMap[str(i)+str(j)]
        print "rv",commonRowsValues
        print "cv",commonClmValues
        print "kk",avail_values
        print "group index", groups[group_index]
        print "========"
    
    if ((avail_values is not None) and len(avail_values)):
        avail_values.difference(set([0]))
        tmp = list(avail_values)
        tmp.sort()
        return tmp
    
    return None
                    
                    
"""
    control starts below
"""   
create_groups()
create_findsmap()


#     break
#         else:
#             print str(sk[i][j])+" ",

printFindsMap(findsMap)
printfullMatrix(sk)
printProcessResult()
print "="*30

from copy import deepcopy
dummy_sk = deepcopy(sk) 
loop = 1

while (True):
    print "="*10+"round"+str(loop)+"="*10
    for item in findsMap.items():
#         print "--start--",item
        solver(item, dummy_sk)
#         print "--end--\n"
    print "="*10+"end of round"+str(loop)+"="*10
    printfullMatrix(dummy_sk)
    loop += 1
    if not len(findsMap):
        break;
    elif loop > 5:
        break
 
printfullMatrix(sk)
printfullMatrix(dummy_sk)
printFindsMap(findsMap)