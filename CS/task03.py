'''
함수명 : deci_to_any
입력 (argument) : 양의 정수 하나와 2~16 사이의 정수 하나
출력 (return) : 문자열 하나
기능 : 첫째 인수의 값을 둘째 인수의 진법으로 표현한 문자열을 반환
사용예 :
result = deci_to_any(140, 8) print(result) #출력: 214 
result = deci_to_any(61, 16) print(result) #출력: 3D
'''

def getHexChar(dec_number):  # 16진법 A,B,C,D,E,F 붙여주기
    if dec_number < 10:
        return str(dec_number)
    if dec_number == 10:
        return "A"
    if dec_number == 11:
        return "B"
    if dec_number == 12:
        return "C"
    if dec_number == 13:
        return "D"
    if dec_number == 14:
        return "E"
    if dec_number == 15:
        return "F"

def deci_to_any(number, divider):
    if(number // divider == 0):
        return getHexChar(number % divider)
    else:
        return "" + str(deci_to_any(number // divider, divider)) + getHexChar(number % divider)

result = deci_to_any(140, 8)  # Case 1  Oct -> OK
result = deci_to_any(61, 16)  # Case 2  Hex -> OK
result = deci_to_any(516, 10)  # Case 3  Dec -> OK
result = deci_to_any(27, 2)  # Case 4 Bin -> OK
result = deci_to_any(10, 12)  # Case 5 12? -> OK
result = deci_to_any(8, 7)  # Case 6 7? -> OK
result = deci_to_any(42, 15)  # Case 7 15? -> OK
print(result)


'''
= Memo =
(재귀) 스택을 사용하자! ⭐️
https://techblog-history-younghunjo1.tistory.com/399

전역변수가 다중으로 선언되는걸 막기 위한 if 문
https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists

파이썬 재귀함수 return None  (다른 곳의 문제였음)
https://munang.tistory.com/entry/개념-정리-Python-None-리턴하는-경우-재귀함수-None-리턴

8진수로 만드는건 이제 잘 되는데 16진수를 만드는게 안됨..
이 부분은 16진수로 만드는 부분을 구현하지 않았기 때문이니..
한번 만들어보겠음.

61을 16으로 나누었을때
몫 3과 나머지 13가 나옴
3을 16으로 나누면 나머지 3이 나오니

3, 13 이렇게 나올것이며
예상 답변인 3D는 3그리고 13를 16진수로 만든 값일거임.
13은 실제로 16진수 [... 9, A(10), B(11), C(12), D(13), E(14), F(15), 10 ...] 에서 D를 담당하므로
divider가 16일 경우에 이렇게 만들어 주는게 필요할듯...
아니 근데 입력에서 2~16의 정수 하나라고 해서 15진수나 14진수도 구현하고 싶은데...
일단 16부터 만들어 보자.


16진수 영어 만드는법
https://stackoverflow.com/questions/48893881/turning-decimals-into-hexadecimals-without-the-hex-function

그냥
if dec_digit < 10:
        return dec_digit
    if dec_digit == 10:
        return "A"
    if dec_digit == 11:
        return "B"
    if dec_digit == 12:
        return "C"
    if dec_digit == 13:
        return "D"
    if dec_digit == 14:
        return "E"
    if dec_digit == 15:
        return "F"
요렇게 생각했었는데
스택 아저씨들은
def getHexChar(dec_digit):
    return '{:x}'.format(range(16)[dec_digit])

이렇게 하거나

def getHexChar(dec_digit):
    return str((tuple(range(10)) + ('a', 'b', 'c', 'd', 'e', 'f'))[dec_digit])

요렇게 하네

'''


'''
= 코드 백업 =
def deci_to_any(number, divider):
    if(number // divider == 0):
        return str(number % divider)
    else:
        return "" +  str(number % divider) + str(deci_to_any(number // divider, divider))

result = deci_to_any(140, 8)  # Expected Result : 214
print(result)  # Result : 412

아 재귀함수의 return 순서를 바꾸면 되는거였네 ㅋㅋㅋ



def deci_to_any(number, divider):
    if(number // divider == 0):
        return str(number % divider)
    else:
        return "" +  str(number % divider) + str(deci_to_any(number // divider, divider))

result = deci_to_any(140, 8)  # Expected Result : 214
print(result)  # Result : 214

16진수가 출력이 안됨 ㅋㅋ

'''