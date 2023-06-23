def solution(arr):
    if len(arr) == 1:
        return arr
    j = 2
    answer = []
    while(len(arr)>j):
        j = j*2
    while(len(arr)!=j):
        arr.append(0)
    answer = arr
    return answer