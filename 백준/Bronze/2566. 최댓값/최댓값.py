import sys
sysinput = sys.stdin.readline
nLi = []
for i in range(9):
    nLi.append(list(map(int,sysinput().split())))
mNo = nLi[0][0]
x=0
y=0
for i in range(9):
    for j in range(9):
        if nLi[i][j]>=mNo:
            mNo = nLi[i][j]
            x=i+1
            y=j+1
print(mNo)
print(x,y)