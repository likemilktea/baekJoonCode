def changeList(listA):
    for i in range(int(len(listA)/2)):
        listA[i],listA[(i+1)*-1] = listA[(i+1)*-1],listA[i]
    return listA

import sys
sysinput = sys.stdin.readline
n,m = map(int,sysinput().split())
nList = [i for i in range(1,n+1)]
mList = []
for i in range(m):
    mList.append(list(map(int,sysinput().split())))
for i in range(len(mList)):
    nList = nList[:mList[i][0]-1]+changeList(nList[mList[i][0]-1:mList[i][1]])+nList[mList[i][1]:]
    
for i in nList:
    print(i,end=' ')