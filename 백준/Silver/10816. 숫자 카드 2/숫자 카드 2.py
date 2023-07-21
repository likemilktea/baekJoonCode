# 숫자 카드의 개수 N 입력
N = int(input())
# 상근이가 가지고 있는 숫자 카드 입력 및 딕셔너리로 변환
Nlist = list(map(int, input().split()))
card_count = {}
for num in Nlist:
    card_count[num] = card_count.get(num, 0) + 1

# 쿼리 개수 M 입력
M = int(input())
# 각 쿼리에 대해 결과 출력
Mlist = list(map(int, input().split()))
for num in Mlist:
    print(card_count.get(num, 0), end=' ')