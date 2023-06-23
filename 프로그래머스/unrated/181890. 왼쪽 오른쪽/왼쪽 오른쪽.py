def solution(str_list):
    answer = []
    
    for i in range(len(str_list)): # str_list 순회
        if str_list[i] == 'l': # 만약 l이 나온다면
            answer=str_list[:i] # l의 왼쪽 문자열 슬라이싱으로 할당
            return answer
    
        elif str_list[i] == 'r': # 만약 r이 나온다면
            answer=str_list[i+1:] # r의 오른쪽 문자열 슬라이싱으로 할당
            return answer
    return answer