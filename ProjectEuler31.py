a = [1,2,5,10,20,50,100,200]

cool = {1:[1], 2:[[1,1],[2]], 5:[[5], [2,2,1], [1,1,1,1,1], [2,1,1,1]]}
cool[10] = [[10], [5,5],]
zz = sorted(list(cool.keys()), reverse=True)
print(zz)
for x in range(len(zz)):
    try:
        if zz[x]%zz[x+1] == 0:
            cool[zz[x+1]].append([x for x in cool[zz[x]]])
            print('did something')
    except IndexError as ie:
        print('why', str(ie))
        pass
from pprint import pprint
pprint(cool)