def bubbleSort(arr):
    for i in range(len(arr)):  # 배열의 크기만큼 반복
        
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(len(arr) - i - 1):
            
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

# 참고로 배열은 C의 포인터 개념이라 원본 배열이 수정되었으므로 return이 필요없음


arr = [5, -2, 9, 10, 51, 2, -94, -11, 3]
bubbleSort(arr)
print(arr)