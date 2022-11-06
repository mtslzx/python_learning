# Gnome Combination

from itertools import combinations

N = input()
inputList = input().split()
outputList = []
for idx, val in enumerate(inputList):
    key = list(val)
    inputList[idx] = None  # key가 나온 자리를 예외처리하기 위함
    for i in range(N):  # 0 ~ N  # 배열의 idx 위치와 무관하게 무조건 맨 처음부터 시작함
        compare = inputList[i]
        if compare == None:  # 미리 제외해둔 key값을 만날경우 건너뛰기
            pass
        else:
            compare = list(compare)  # 앞에 쓰지 않는 이유는 None의 경우에 list()를 쓰면 에러가 발생하기 때문
            outputList.append(key[0] + compare[1])
    inputList[idx] = val  # 다시 key 자리에 넣어줌
    
print(inputList)



# 단어 별로 문자열 분리
# https://codechacha.com/ko/python-convert-string-to-char-list/

# 정렬알고리즘?
# -> 브루트포스.. 아마 O(20만 ^ 20만) 일것 같은데, 뭔가 시간초과날것같음