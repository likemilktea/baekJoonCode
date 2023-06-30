import sys
sysinput = sys.stdin.readline
x,y,w,h = map(int,sysinput().split())
mx = x if x < w-x else w-x
my = y if y < h-y else h-y
print(min(mx,my))