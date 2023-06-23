def solution(arr):
    answer = [[]]
    while len(arr) != len(arr[0]):
        if len(arr) > len(arr[0]):
            for i in range(len(arr)):
                arr[i].append(0)
        elif len(arr) < len(arr[0]):
            arr_temp = []
            for i in range(len(arr[0])):
                arr_temp.append(0)
            arr.append(arr_temp)
    answer = arr
    return answer