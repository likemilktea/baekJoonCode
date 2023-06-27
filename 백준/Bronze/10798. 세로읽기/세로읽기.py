inputList = []
outputStr = ""

for i in range(5):
    inputList.append(input().split()) # 5줄에 걸쳐 문자열 리스트를 입력 받음

maxLength = 0
for i in inputList:
    if maxLength<len(i[0]):
        maxLength=len(i[0]) # 인풋 리스트에서 가장 문자열의 값을 체크해서 그 값을 입력

for i in range(maxLength): # 가장 긴 입력값의 횟수만큼 열의 입력을 반복하며
    for j in range(len(inputList)): # 행의 순서대로 문자열을 읽어옴
        try:
            outputStr+=inputList[j][0][i] # 매 행의 문자 값을 출력값에 더함
        except: # 오류가 발생하면 컨티뉴를 하여 회피
            continue

print(outputStr) 