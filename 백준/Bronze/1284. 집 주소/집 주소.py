import sys
sysinput = sys.stdin.readline
nLi = []
count = 0
while True:
    nLi.append(input())
    if nLi[-1]=='0':
        break
cLi = []
for i in range(len(nLi)-1):
    count=0
    for j in nLi[i]:
        if j == '0':
            count+=5
        elif j== '1':
            count+=3
        else:
            count+=4
    count+=1
    cLi.append(count)
for data in cLi:
    print(data)
