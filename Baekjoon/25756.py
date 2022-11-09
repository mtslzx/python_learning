# Calculate Defense Ignore stat

N = int(input())
A = list(map(int, input().split()))
defStat = float(0)
for i in range(N):
    defStat = round(1.0 - (1.0 - round(defStat,6)) * (1.0 - round(A[i]/100,6)),6) # [1]
    # a = round(float("%g" %(defStat*100)),6)
    # if a == round(a):
    #     print(f"{a:.1f}")
    # else:
    #     print(a)
    # print(f"{round(defStat*100,6):.6f}")
        
# 20 20 20 20 20
# 1 - ( 1- 0.0 ) * (1 - 0.2) = 0.16
# 1 - ( 1- 0.16) * (1 - 0.2) = 0.256

# 1 1 1 1 1
# 1 - ( 1- 0.0 ) * (1 - 0.01) = 0.01 -> in python defStat = 0.01000000000000009 <- I think this make error 
# 1 - ( 1- 0.01) * (1 - 0.01) = 
# 0.99 * 0.99 = 0.9801

# Round 함수를 사용하면 0.01000000000000009 -> 0.01로 바뀌어서 정답처리가 됨

# [1]
# http://mwultong.blogspot.com/2007/04/python-percent-percentage.html
# 파이썬에서는 정수와 실수의 구분이 있기에, 가령 10 이런 정수가 있다면 10.0 이렇게 실수화해 주어야만 제대로 된 결과가 나옵니다.

'''
현재 방어율 수치 V (기본 0 퍼센트)
물약 수치 A(i)

1- ( 1 - 0 ) * ( 1- 1)


1 - ( 1 - V ) * ( 1 - A(i) )





-- 예제 입력 --
5
-- 20 20 20 20 20
예제 출력 --
20.0
36.0
48.8
59.04
67.232




'''