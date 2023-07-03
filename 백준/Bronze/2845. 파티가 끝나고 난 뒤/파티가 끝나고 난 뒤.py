import sys
sysinput = sys.stdin.readline
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sA=a[0]*a[1]

print(*list(map(lambda x: x-sA,b)))