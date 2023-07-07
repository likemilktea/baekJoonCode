n = int(input())
sDi = {}
for i in range(n):
    c = input()[0]
    if c in sDi:
        sDi[c]+=1
    else:
        sDi[c]=1
ans = []
for k,v in sDi.items():
    if v >= 5:
        ans.append(k)
ans.sort()
if len(ans)>=1:
    for i in ans:
        print(i,end='')
else:
    print('PREDAJA')