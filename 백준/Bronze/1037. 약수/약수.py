import sys

sysinput = sys.stdin.readline

n = int(sysinput().rstrip())
mList = list(map(int,sysinput().split()))
i = 2
# 1. mList에서 최대 수를 구해 2를 곱한다
# 2. mList의 다른 수가 그 수의 약수인지 확인한다
# 2-1 맞다면 그 수가 정답
# 2-2 틀리다면 3, 또 틀린다면 4 그렇게 mList의 최소 숫자까지 곱해보고 비교한다
maxM = max(mList)*min(mList)
# while True:
#     maxM = max(mList) * i
#     checkM = True
#     for m in mList:
#         if maxM % m != 0:
#             False
#             break
#     if checkM:
#         break
#     i+=1
print(maxM)