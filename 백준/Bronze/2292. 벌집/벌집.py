n = int(input())
resultList = [1,6,12,18,24]
result = 0
m = 0
def hexa_add(num):
    result=0
    for i in range(num+1):
        result += i
    result *= 6 
    result += 2
    return result
while n >= m:
    m = hexa_add(result)
    result+=1
print(result)
