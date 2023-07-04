import sys
sysinput = sys.stdin.readline
a,b = list(map(int,sysinput().split()))
c = int((a+b)/2)
d = c-b
if (a + b) % 2 == 0 and (a - b) % 2 == 0 and c >= 0 and d >= 0:
    print(max(c, d), min(c, d))
else:
    print(-1)