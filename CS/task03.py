'''
함수명 : deci_to_any
입력 (argument) : 양의 정수 하나와 2~16 사이의 정수 하나
출력 (return) : 문자열 하나
기능 : 첫째 인수의 값을 둘째 인수의 진법으로 표현한 문자열을 반환
사용예 :
result = deci_to_any(140, 8) print(result) #출력: 214 
result = deci_to_any(61, 16) print(result) #출력: 3D
'''


def deci_to_any(number, divider):
    if(number // divider == 0):
        return str(number % divider)
    else:
        return "" +  str(number % divider) + str(deci_to_any(number // divider, divider))

result = deci_to_any(140, 8)
print(result)


'''
= Memo =
(재귀) 스택을 사용하자! ⭐️
https://techblog-history-younghunjo1.tistory.com/399

전역변수가 다중으로 선언되는걸 막기 위한 if 문
https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists

파이썬 재귀함수 return None  (다른 곳의 문제였음)
https://munang.tistory.com/entry/개념-정리-Python-None-리턴하는-경우-재귀함수-None-리턴

'''