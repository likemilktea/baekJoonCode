## 문제 요약
# 포켓몬 도감 N과 문제 M이 주어진다.
# N에서 M이 필요로하는 값을 뽑아내는 문제로
# 최대한 빨리 값을 찾아내는 게 관건

# 입력이 최대 10만건이라 최대한 빨리 읽을 수 있는 readline 함수 이용
import sys
sysinput = sys.stdin.readline

# 도감 갯수 N과
# 질문 갯수 M 입력
N,M = map(int,sysinput().split())

# readline과 리스트 컴프리헨션을 이용해 도감 값을 입력받는다.
# 리스트 컴프리헨션이란 리스트와 반복문을 간결히 표현한 형식
Nlist = [sysinput().rstrip() for i in range(N)]
# 딕셔너리를 만드는 이유는 어디에 있을지 모르는 값에의 빠른 접근을 위해
# 비선형 구조 중 딕셔너리를 선택
# 도감 번호로를 키로, 이름을 밸류로 갖는 딕셔너리 하나와
# 이름을 키로, 번호를 밸류로 갖는 딕셔너리 생성
# 딕셔너리도 마찬가지로 컴프리헨션을 통해 간결히 표현
# enumerate 를 통해서 인덱스 값을 출력하면 0부터 시작하므로
# 매 키값을 대입할 때 1씩 가중치를 주어 출력을 용이하게 한다
Ndict = {key+1 : value for key, value in enumerate(Nlist)}
NdictSwap = {key : value+1 for value, key in enumerate(Nlist)}

# 질문 리스트 또한 컴프리헨션으로 간단히 표현
Mlist = [sysinput().rstrip() for i in range(M)]

# Mlist의 요소를 키값으로 반복문을 돌리되
# 만약 키값이 숫자라면 숫자를 키로 갖는 Ndict에 키값을 넣고
# 그렇지 않다고 문자열 등의 값을 키로 갖는 다면 NdictSwap에 키값을 넣어
# 결과를 출력한다.
for key in Mlist:
    if key.isdigit():
        print(Ndict[int(key)])
    else:
        print(NdictSwap[key])