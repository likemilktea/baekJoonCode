N = int(input())
xy=[list(map(int,input().split())) for i in range(N)]
xy.sort()
for data in xy:
    print(*data)
