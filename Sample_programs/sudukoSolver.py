"""
    program to solve sudoko
"""
from copy import deepcopy

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
sk = suduko
"""hard"""
sudoko = [  [0,0,8,0,6,0,0,0,2],
            [0,0,0,2,0,0,0,0,7],
            [2,0,0,4,0,5,0,0,0],
            [0,2,0,6,3,0,5,1,0],
            [0,0,0,5,0,1,0,0,0],
            [0,5,7,0,4,9,0,2,0],
            [0,0,0,7,0,6,0,0,3],
            [8,0,0,0,0,2,0,0,0],
            [9,0,0,0,8,0,7,0,0],
    ]
#sk = suduko
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
findsMap = {}

if logger:
    print "="*10+"Input"+"="*10
    for i in range(9): print sk[i]
    print "="*30

def check_logger(fun):
    def innerFun(*x,**y):
        if not logger:
            print "logger off"
        else:
            return fun
    return innerFun

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

def saveGroups():
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

@check_logger
def printGroup():
    print "="*10+"print group"+"="*10
    for i in groups : print i
    print "="*10+"processing"+"="*10

def printFindsMap(d):
    print "="*10+"printing answers map"+"="*10
    for item in d.items(): print item
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


def findMissingValue(i, j, matrix, tmatrix):
    
    group_index = (i-(i%3))+(j/3)
    
    from itertools import chain
    existing = set(chain(chain(groups[group_index],
                            matrix[i][:], tmatrix[j][:])))
    
    tmpValues =  [x for x in xrange(1,10)
                   if x not in existing]
    findsMap.update({str(i)+str(j):tmpValues})
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


def solver(i, j, matrix, tmatrix):
    
#     print "index->",i,j
    group_index = (i-(i%3))+(j/3)
    
    from itertools import chain
    existing = set(chain(chain(groups[group_index],
                            matrix[i][:], tmatrix[j][:])))
    
    tmpValues =  [x for x in xrange(1,10)
                   if x not in existing]
    
    if False:
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
    
def printSolverBreaker():
    for i in range(9):
        for j in range(9):
            key = str(i)+str(j)
            if key in findsMap.keys():
                print key,"-->",findsMap.get(key)
"""
    control starts below
"""   
saveGroups()
#printfullMatrix(sk)
#printfullMatrix(skt)

for i in range(9):
    for j in range(9):
        if sk[i][j] == False:
            try:
                findMissingValue(i,j, sk, skt)
            except  StopIteration:
                print "check log"
#     break
#         else:
#             print str(sk[i][j])+" ",
print ""
print "="*10+"processing over"+"="*10
print ""

printFindsMap(findsMap)
printProcessResult()
print "="*30

import copy
dummy_sk = deepcopy(sk) 
round = 1
fm = findsMap

while (True):
    print "="*10+"round"+str(round)+"="*10
    stop = True
    dummy_skt = zip(*dummy_sk)
    for key,value in fm.items():
        i = int(key[0])
        j = int(key[1])
        if value.__len__() == 1:
            if dummy_sk[i][j] == 0:
                dummy_sk[i][j] = value[0]
                print value[0],"added to dummy",key
                del fm[key]
                stop = False
        else:
            try:
#                 print key,"-->",value
                tmp = solver(i, j, dummy_sk, dummy_skt)
                if fm[key] != tmp:
                    findsMap.update({str(i)+str(j):tmp})
                    stop = False
            except: StopIteration, "hold it"
    
    print "="*10+"end of round"+str(round)+"="*10
    
    if len(fm) == 0:
        print "\n"+"_"*5+"Solved Success!"+"_"*5+"\n"
        break
    
    if stop:
        printFindsMap(fm)
        printSolverBreaker();
        print "\n"+"_"*5+"Failed Ooch!"+"_"*5+"\n"
        break
    
#     print "keys", fm.viewkeys()
#     print "dic len",len(fm)
#     printfullMatrix(dummy_sk)
    round += 1
 
printfullMatrix(sk)
printfullMatrix(dummy_sk)