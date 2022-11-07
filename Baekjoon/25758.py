# Gnome Combination

N = input()
inputList = input().split()
outputList = []
for idx, val in enumerate(inputList):
    key = list(val)
    inputList[idx] = None  # key가 나온 자리를 예외처리하기 위함
    for i in range(int(N)):  # 0 ~ N  # 배열의 idx 위치와 무관하게 무조건 맨 처음부터 시작함
        compare = inputList[i]
        if compare == None:  # 미리 제외해둔 key값을 만날경우 건너뛰기
            pass
        else:  # key 값이 아닐경우
            compare = list(compare)  # 앞에 쓰지 않는 이유는 None의 경우에 list()를 쓰면 에러가 발생하기 때문
            # 어쨌거나 우린 "2"세대 유전자의 "표현형"만 구하면 되므로, 역순정렬을 통해 맨 얖 표현형만 확인한다.
            outputList.append(sorted(key[0] + compare[1], reverse=True)[0])  # 출력리스트에 조합 저장  # 첫번째 유전자의 첫번째 문자와 두번째 유전자의 두번째 문자를 합침, 그리고 표현형만 확인하기 위해, 영어를 역순으로 했을 때 만 앞의 글자만 출력
    inputList[idx] = val  # 다시 key 자리에 넣어줌
result = sorted(list(set(outputList)))  # 중복 제거
print(len(result))  # 알파벳 개수 출력
# [print(i, end=' ') for i in result]  # 공백 출력
print(*result)  # 공백 출력


# 단어 별로 문자열 분리
# https://codechacha.com/ko/python-convert-string-to-char-list/

# 정렬알고리즘?
# -> 브루트포스.. 아마 O(20만 ^ 20만) 일것 같은데, 뭔가 시간초과날것같음
# -> 시간초과남 ㅋㅋ ;; , 계산기 넣어봤는데 10만! 이 10의 10승(100억) 이상 나오는거 보니깐 답도 없음
# 보통 1억 연산을 1초로 치는데 12억 까지일 거거든
# 다른 방법 생각해보자.

# 리스트 컴프리헨션 -> 리스트 안에서 포문 2개 쓰는법도 알려줌
# https://m.blog.naver.com/qbxlvnf11/221434003885

# print(*list)  # 리스트를 공백으로 구분하여 출력
# https://www.daleseo.com/python-lists-print/





# Code Archive
# 시간초과
# N = input()
# inputList = input().split()
# outputList = []
# for idx, val in enumerate(inputList):
#     key = list(val)
#     inputList[idx] = None  # key가 나온 자리를 예외처리하기 위함
#     for i in range(int(N)):  # 0 ~ N  # 배열의 idx 위치와 무관하게 무조건 맨 처음부터 시작함
#         compare = inputList[i]
#         if compare == None:  # 미리 제외해둔 key값을 만날경우 건너뛰기
#             pass
#         else:  # key 값이 아닐경우
#             compare = list(compare)  # 앞에 쓰지 않는 이유는 None의 경우에 list()를 쓰면 에러가 발생하기 때문
#             # 어쨌거나 우린 "2"세대 유전자의 "표현형"만 구하면 되므로, 역순정렬을 통해 맨 얖 표현형만 확인한다.
#             outputList.append(sorted(key[0] + compare[1], reverse=True)[0])  # 출력리스트에 조합 저장  # 첫번째 유전자의 첫번째 문자와 두번째 유전자의 두번째 문자를 합침, 그리고 표현형만 확인하기 위해, 영어를 역순으로 했을 때 만 앞의 글자만 출력
#     inputList[idx] = val  # 다시 key 자리에 넣어줌
# result = sorted(list(set(outputList)))  # 중복 제거
# print(len(result))  # 알파벳 개수 출력
# [print(i) for i in result]  # 공백 출력