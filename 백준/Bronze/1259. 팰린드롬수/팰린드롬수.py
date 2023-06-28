import sys

def palin(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[(i+1)*-1]:
            return "no"
    return "yes"

sysinput = sys.stdin.readline
nList = []
while True:
    nList.append(sysinput().rstrip())
    if nList[-1]=='0':
        break
    
for s in nList:
    if s=='0':break
    print(palin(s))

