all = [[0,1],[2,3],[4,5]]
#for i in all:
#    for a in i :
#        if a == 4 :
#            continue
#        print(a)

always = [b for i in all for b in i ]
print(tuple(always))