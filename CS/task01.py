'''
함수명 : diff
입력 (argument) : 두개의 정수
출력 (return) : 하나의 정수
기능 : 입력으로 들어온 두 정수의 차의 절댓값을 반환
사용예 : result = diff(-1, 5) print(result) #출력: 6
'''

# def diff(a, b):
#     return abs(a - b)
# print(diff(-1, 5))

diff = lambda a, b: abs(a - b)
result = diff(-1, 5)
print(result)

