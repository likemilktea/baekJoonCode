n,k = map(int,input().split())
mLi = list(map(int,input().split(',')))

def subList(liA,liB):
    liC=[]
    for a,b in zip(liA,liB):
        liC.append(a-b)
    return liC

for i in range(k):
    nLi = [mLi[d] for d in range(len(mLi)-1)]
    mLi = [mLi[d] for d in range(1,len(mLi))]
    mLi = subList(mLi,nLi)

mLi=list(map(str,mLi))
mLi = ','.join(mLi)
print(mLi)