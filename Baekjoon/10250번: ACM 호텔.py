#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10250                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10250                          #+#        #+#      #+#     #
#    Solved: 2023/08/07 13:46:09 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://codechacha.com/ko/python-zero-fill/ 숫자 앞에 0으로 채우기 .zfill(num) - zero fill

for i in range(int(input())):  # 처음에 입력한 값 만큼 반복
    Height, Width, Number = map(int, input().split())  # 한 행에 여러 입력이 들어오므로 .split() 매소드를 사용하여 각 변수에 값을 담아줌
    Floor = (Number % Height) if (Number % Height) != 0 else Height  # 객실의 호실을 제외한 층수를 계산함.
    Room = (Number // Height) + 1 if (Number % Height) != 0 else (Number // Height)  # 객실의 층수를 제외한 호실을 계산함. 1번방부터 시작하므로 +1. 맨 윗층은 예외처리.
    print(f'{Floor}{str(Room).zfill(2)}')  # 0을 채워주도록 .zfill() 매소드 사용하여 출력.

# 반례 - 계산식에서 몫과 나머지를 계산하도록 만들었는데 이럴 경우 나누어 떨어지는 값은 0이 되어버려 6 * 12인 건물의 12번째 방은 003호가 되어버리는 문제가 발생한다.
# 정상적으로 출력된다면, 602호가 출력되어야 할 것이다.
# 오류: 6 12 12 -> 003 | 올바른 코드: 6 12 12 -> 602
