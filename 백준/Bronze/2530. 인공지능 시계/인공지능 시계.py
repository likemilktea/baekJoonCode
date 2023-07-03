import sys
sysinput = sys.stdin.readline().rstrip
a,b,c = map(int,sysinput().split())
s = int(input())
s = a*60*60 + b*60 + c + s
c=s%60
s-=c
b=s%3600
s-=b
a=s

print((a//3600)%24,b//60,c)