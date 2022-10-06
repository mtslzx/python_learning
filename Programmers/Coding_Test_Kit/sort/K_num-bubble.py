'''
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.
입출력 예
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.
'''

def bubbleSort(arr):
    for i in range(len(arr)):  # 배열의 크기만큼 반복
        
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(len(arr) - 1 - i):
            
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

def solution(array, commands):  # 매우 쉬운 파이썬 스타일...?
    answer = list()
    for n in range(len(commands)):  # commands의 길이만큼 반복 (commands의 길이는 1 이상 50 이하이므로.)
        # tempArray = array  # 매개변수 array를 tempArray에 저장 (원본 배열을 보존하기 위함) -> 필요없어짐 ㅋㅋ;;
        i = commands[n][0]  # commands 이중배열에서 array를 자르기 위해 필요한 i 추출 [*1]
        j = commands[n][1]  # commands 이중배열에서 array를 자르기 위해 필요한 j 추출 [*1]
        k = commands[n][2]  # commands 이중배열에서 array를 자르고 정렬한 후 k번째 숫자 추출에 필요한 k 추출 [*1]
        # answer.append(array[i - 1 : j].sort) # 이게 왜 안되는지 궁금함.
        tempArray = array[ i - 1 : j ]  # i - 1번째부터 j - 1번째까지 자르기
        bubbleSort(tempArray)  # 가장 느린 버블 정렬을 이용함
        # tempArray.sort() # 자른 배열을 정렬 (sort()는 원본 배열을 정렬하므로, sorted()를 사용하는 것이 좋음)
        answer.append(tempArray[k - 1]) # array를 정렬한 후 k번째 숫자 추출 및 answer에 추가
    return answer



print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  #테스트 케이스

# 주석.

# sorted()함수에 비해 버블 정렬 알고리즘이 느린 퍼포먼스를 보여줬다.

# [1]
# i,j,k = command # 이렇게도 가능


# [2]
# 1, 5, 2, 6, 3, 7, 4 (array)
# 0, 1, 2, 3, 4, 5, 6 (index)
# 1, 2, 3, 4, 5, 6, 7 (index + 1) = (noraml number)
# [5, 2, 6, 3] (result) (i = 2, j = 5)
# ★ slicing : [i : j] -> arr[i] ~ arr[j - 1]
# ++++++++++++++++++++++++++++++++++++++++++++++++++
# 새로운 정렬된 리스트를 반환하는 함수는 sorted 함수
# 리스트 자체를 정렬시켜버리는 것은 sort 함수 (매소드)




# 입출력 예시에서 commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]이라 되어있는데, 한번에 이차원 배열이 다 들어가는것인지.
# 아니면 solution을 호출할 때마다 배열이 바뀌는것인지..?
# 아 이차원 배열이네..


# 코드 백업.

'''
def cutting_array(array, i, j):
    result = list()
    m = 0
    for n in range (i - 1, j - 1):  # n번째 배열 자리를 구해야 하므로 -1을 해준다. (배열은 0부터 인덱싱되므로)
        result = result[n] + array[n]
        m = m + 1
    return result
# 되게 C언어적으로 생각했었음. 이렇게 하면 안되고, 이미 만들어진 slicing을 이용해야함.


def sort(array):
    result = sorted(array)
    return result

def cutting_array(array, i, j):  # array를 i번째부터 j번째까지 자르기
    result = array[ i - 1 : j ]  # i - 1번째부터 j - 1번째까지 자르기 [1]
    return result
# 역시 C 스타일...
'''

# 숏코딩?
# 람다 함수와 map, list 함수를 사용하여 한줄로 줄일 수 있음.

'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''