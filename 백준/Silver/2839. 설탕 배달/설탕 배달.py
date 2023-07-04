import sys
sysinput = sys.stdin.readline
n = int(sysinput())
m = 3   # 나눌 값, 나중에 5로 바꿈.
ans = -1
c = 0
while True:
    if n!=3 and n<5: # 3이 아니면서 5 미만이라면 실패. 탈출
        break
    if n%5==0: # 5로 나누어 나머지가 0이 될 수 있을 때까지
        m=5
    n-=m # 3을 뺌.
    c+=1
    if n==0: # 만약 n이 0이라면
        ans=c # ans = 카운트

print(ans)
