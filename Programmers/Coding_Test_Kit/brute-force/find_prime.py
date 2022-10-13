'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
11과 011은 같은 숫자로 취급합니다.
'''
from itertools import permutations  # 순열로 풀기 위해 라이브러리 임포트

def solution(numbers):
    answer = 0
    arr = list(numbers)  # 문자열을 리스트로 쪼개기
    permu_arr = list()  # 빈 임시배열 생성
    for i in range(len(arr) + 1):
        for j in list(permutations(arr, i)):  # 문자열들로 모든 수 조합하기
            permu_arr.append(j)  # 위에서 만든 값을 하나씩 빈 배열에 추가
    del permu_arr[0]  # 배열의 공백 제거 (예외 처리) (배열 맨 앞에 공백이 생기더라..)
    temp_arr = list()  # 빈 임시 배열 생성
    for i in range(len(permu_arr)):  # 문자열 리스트(모든 경우의 수) 만큼 반복
        temp_str = str()  # 빈 임시 문자열 생성(초기화)
        for j in range(len(permu_arr[i])):  # 이중 배열인 문자열 리스트의 원소 길이만큼 반복
            temp_str = temp_str + permu_arr[i][j]  # 임시 문자열에 숫자 문자열을 더해서 자릿수 맞추기(?)
        temp_arr.append(int(temp_str))  # 문자열을 정수로 바꾸어 임시 배열에 담기 

    # 리스트 정리
    temp_arr = list(set(temp_arr)) # 중복값 없애기
    if 0 in temp_arr:  # 0과 1은 소수가 아니므로 제거
        temp_arr.remove(0) #
    if 1 in temp_arr:
        temp_arr.remove(1) #
  
    # 소수 찾기
    for i in range(len(temp_arr)):  # 임시 배열의 모든 원소 길이 만큼 반복
        isPrime = True  # 소수 플래그
        for j in range(2, temp_arr[i]):  # 2부터 임시배열 n-1까지 반복.
            if temp_arr[i] % j == 0:  # 임시 배열의 수를 2부터 n-1까지 모든 수로 나누어보기 (소수찾기))
                isPrime = False  # 만약 나누어진다면, 소수가 아니므로 False
                break  # 반복문 종료
        if isPrime:  # 끝까지 안 나누어졌다면 소수이므로, answer에 1추가.
            answer += 1
    return answer

numbers = "1231"
print(solution(numbers))

'''
from itertools import permutations  # 순열로 풀기 위해 라이브러리 임포트

def solution(numbers):
    answer = 0
    arr = list(numbers)  # 문자열을 리스트로 쪼개기
    permu_arr = list()  # 빈 임시배열
    for i in range(len(arr) + 1):
        for j in list(permutations(arr, i)):
            permu_arr.append(j)
    del permu_arr[0]  # 배열의 공백 제거 (예외 처리)
    print(permu_arr)
    temp_arr = list()  # 빈 임시 배열 생성
    for i in range(len(permu_arr)):  # 문자열 리스트(모든 경우의 수) 만큼 반복
        temp_str = str()  # 빈 임시 문자열 생성(초기화)
        for j in range(len(permu_arr[i])):  # 이중 배열인 문자열 리스트의 원소 길이만큼 반복
            temp_str = temp_str + permu_arr[i][j]  # 임시 문자열에 숫자 문자열을 더해서 자릿수 맞추기(?)
        temp_arr.append(int(temp_str))  # 문자열을 정수로 바꾸어 임시 배열에 담기 
    
    # # 순열로 만들어지지 않는 한자리 수 추가하기
    # for i in range(len(arr)):  # 리스트로 쪼개진 문자열 원소 길이 만큼 반복
    #     if (int(arr[i]) != 1) and (int(arr[i]) != 0):  # 1과 0은 소수가 아니므로 제외
    #         temp_arr.append(int(arr[i]))  # 임시 배열에 한자리 수 담기
    
    # 리스트 정리
    temp_arr = list(set(temp_arr)) # 중복값 없애기
    if 0 in temp_arr:  # 0과 1은 소수가 아니므로 제거
        temp_arr.remove(0) #
    if 1 in temp_arr:
        temp_arr.remove(1) #
    
    # 소수 찾기
    for i in range(len(temp_arr)):  # 임시 배열의 모든 원소 길이 만큼 반복
        isPrime = True  # 소수 플래그
        for j in range(2, temp_arr[i]):  # 2부터 임시배열 n-1까지 반복.
            if temp_arr[i] % j == 0:  # 임시 배열의 수를 2부터 n-1까지 모든 수로 나누어보기 (소수찾기))
                isPrime = False  # 만약 나누어진다면, 소수가 아니므로 False
                break  # 반복문 종료
        if isPrime:  # 끝까지 안 나누어졌다면 소수이므로, answer에 1추가.
            print(temp_arr[i])
            answer += 1
    return answer

numbers = "1231"
print(solution(numbers))
'''

'''
값 = "1231"
결과 = 18
[2, 3, 11, 13, 23, 31, 113, 131, 211, 311, 1123, 1213, 1231, 1321, 2113, 2131, 2311, 3121]
'''

'''
= 메모 =
문자열을 숫자 리스트로 만들고, 리스트를 순열로 다 뽑은 다음에 소수가 몇개인지 새면 될듯.
011과 11 이부분 예외처리 하면 될듯.

= 레퍼런스 =
문자열을 리스트로 쪼개기
https://bio-info.tistory.com/29

소수 판별
https://seongonion.tistory.com/43



'''