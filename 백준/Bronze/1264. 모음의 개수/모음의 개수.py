import sys
sysinput = sys.stdin.readline
sLi = []
while True:
    sLi.append(sysinput().rstrip())
    if sLi[-1]=='#':
        break
c = 0
aeiou = "aeiou"
for s in range(len(sLi)-1):
    for i in sLi[s].lower():
        if i in aeiou:
            c+=1
    print(c)
    c=0
