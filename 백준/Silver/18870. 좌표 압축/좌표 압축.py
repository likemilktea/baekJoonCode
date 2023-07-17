def coordinate_compression(coordinates):
    # 중복 제거 및 정렬
    unique_coordinates = sorted(set(coordinates))
    
    # 좌표 압축
    compressed_coordinates = {coord: i for i, coord in enumerate(unique_coordinates)}
    
    # 결과 출력
    compressed_values = [compressed_coordinates[coord] for coord in coordinates]
    return compressed_values

# 예제 입력
n = int(input())
coordinates = list(map(int, input().split()))

# 좌표 압축 적용
compressed = coordinate_compression(coordinates)

# 결과 출력
for value in compressed:
    print(value, end=' ')