import sys
sysInput = sys.stdin.readline

n,m = map(int,sysInput().split()) # 행렬 입력

nCastle = [sysInput().split() for i in range(n)] # n행 m열로 입력받을 리스트
mCastle = [] # m행 n열로 변환받을 리스트

for i in range(m): # m번 반복
    temp = "" # 임시 문자열
    for j in range(n): # n번 반복
        temp+=nCastle[j][0][i] # n번 동안 문자열로 추가
    mCastle.append(temp) # n번 입력받은 문자열을 행으로 추가

nCount=0 # n행 m열의 공백 리스트
mCount=0 # m행 n열의 공백 리스트

for i in range(n):
    if 'X' not in nCastle[i][0]: # 문자열로 이루어진 행마다 x가 있는지 체크
        nCount+=1 # 없다면 n카운트 증가
for i in range(m):
    if 'X' not in mCastle[i]: # 문자열로 이루어진 행마다 x가 있는지 체크
        mCount+=1 # 없다면 m카운트 증가
    
print(max(nCount,mCount)) # 두 카운트 중에 높은 쪽을 출력