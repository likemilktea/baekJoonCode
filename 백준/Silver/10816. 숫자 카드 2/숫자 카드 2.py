# 문제 요약 
# 주인공이 N장의 카드를 가지고 있다. 
# 우리는 그 가운데 Mlist에 존재하는 카드의 갯수를 알아내야 한다.
# 카드를 가지고 있지 않다면 0장으로 표기한다.

N = int(input())
# 리스트로 소지 카드를 입력 받는다.
Nlist = list(map(int,input().split()))
M = int(input())
# 리스트로 확인해야할 카드 넘버를 입력받는다.
Mlist = list(map(int,input().split()))

# 가진 카드별 갯수를 입력받을 딕셔너리
ansDict = {}
# ansDict 내부에 이미 값이 있다면 있는 값 +1
# 없다면 0+1
# get(a,b)의 경우 앞에는 키값,
# 뒤에는 해당 키값이 존재하지 않는다면 0을 반환하는 함수
for key in Nlist:
    ansDict[key]=ansDict.get(key,0)+1

# 마찬가지로 get 함수를 통해서 출력
# asndict에 키가 있다면 해당 밸류를 
# 없다면 0을 출력
# 출력문 끝에 개행 대신 공백을 출력
for key in Mlist:
    print(ansDict.get(key,0), end = ' ')