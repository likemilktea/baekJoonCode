import sys
sysinput = sys.stdin.readline
n = int(sysinput())
answers = []
for i in range(n):
    answers.append(str(i+1)+". "+sysinput().rstrip())
for a in answers:
    print(a)