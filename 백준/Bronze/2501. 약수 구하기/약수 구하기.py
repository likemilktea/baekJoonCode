n,k = map(int,input().split())
nList = [i for i in range(1,n+1) if n % i == 0]
answer = 0 if len(nList)<=k-1 else nList[k-1]
print(answer)