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
    Floor = (Number % Height)  # 객실의 호실을 제외한 층수를 계산함.
    Room = (Number // Height) + 1  # 객실의 층수를 제외한 호실을 계산함. 1번방부터 시작하므로 +1
    print(f'{Floor}{str(Room).zfill(2)}')  # 0을 채워주도록 .zfill() 매소드 사용하여 출력.