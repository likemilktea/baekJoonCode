num1 = list(map(int,input().split()))
num2 = input().split()
num3 = []
for num in num2:
    if int(num) < num1[1]:
        num3.append(num)
num3=' '.join(num3)
print(num3)