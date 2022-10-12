'''
함수명 : is_triangle
입력 (argument) : 세개의 양의 실수
출력 (return) : True / False
기능 : 세변의 길이가 삼각형을 이루면 True, 그렇지 않으면 False를 반환 (삼각형의 모든 변의 길이는 다른 두 변의 길이의 합보다 작다)
사용예 :
result = is_triangle(2.3, 4.3, 5.6) print(result) #출력: True
result = is_triangle(1.3, 4.3, 5.6) print(result) #출력: False
'''

is_triangle = lambda a, b, c: a+b > c and b+c > c and c+a > a
print(is_triangle(2.3, 4.3, 5.6))

'''
= References =
https://ko.wikihow.com/주어진-세-변의-길이로-삼각형-성립이-가능한지-알아보는-방법

= Memo =

( False )
13
43
56

13 + 43 + 56 = 112
13 + 43 = 56
43 + 56 = 99
13 + 56 = 69


( True )
23
43
56

23 + 43 + 56 = 122
23 + 43 = 66
43 + 65 = 99
23 + 56 = 79



'''