def reverse_string(my_string): # string을 받아 
    my_list=list(my_string) # 배열로 전환한 뒤
    my_list.reverse() # reverse함수로 역전시켜서
    my_string=''.join(my_list) # 다시 string으로 전환하여
    return my_string # 리턴

def solution(my_string, queries):
    answer = ''
    for i in queries: # queries를 순회 할당
        # i 앞의 값 + i에 해당하는 값 reverse_string함수에 할당해 뒤집기 + i 이후의 값
        my_string=my_string[:i[0]]+reverse_string(my_string[i[0]:i[1]+1])+my_string[i[1]+1:]
    answer=my_string
    return answer