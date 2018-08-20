
other = set([4,6,9,1,3,4,6,9,2,4,5,9,8])
me = set([2,3,4,6,7,8,9])
me.difference_update(other)
# other.difference_update(me)
print other
print me





# for i in range(9):
#     for j in range(9):
#         print i,j," ",
#     print ""
# 
# 
# for i in range(9):
#     for j in range(9):
#         row = [[1,2,3],[4,5,6],[7,8,9]]
#         clm = [[1,2,3],[4,5,6],[7,8,9]]
# #         print i,"-",row[i/3][i%3],"|",
#         rv = row[i/3]
#         cv = clm[j/3]
#         del rv[i%3]
#         del cv[j%3]
# #         print i,"-",rv,"|",
#         print j,"-",cv,"|",
#     print ""