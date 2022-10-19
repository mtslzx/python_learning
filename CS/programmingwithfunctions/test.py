# 1줄 코딩
score = int(input("성적을 입력하시오: "));print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F')
number = int(input("정수를 입력하시오: "));print("2와 3으로 나누어 떨어집니다." if number % 2 == 0 and number % 3 == 0 else "2로 나누어 떨어집니다." if number % 2 == 0 else "3으로 나누어 떨어집니다." if number % 3 == 0 else "2와 3으로 나누어 떨어지지 않습니다.")