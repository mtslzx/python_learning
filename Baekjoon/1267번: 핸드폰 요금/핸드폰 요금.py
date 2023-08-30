#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1267                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1267                           #+#        #+#      #+#     #
#    Solved: 2023/08/30 22:28:02 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil

callCount = int(input())  # 이용한 통화의 개수
callTime = list(map(int, input().split()))  # 이용한 통화 시간
Y, M = 0, 0
output = ""

for time in callTime:  # 각 통화의 경우들을 다 확인해야 하므로 각 통화를 모두 종합한다.
    Y += ceil((time + 1) / 30) * 10
    M += ceil((time + 1) / 60) * 15

if Y == M: print(f"Y M {Y}")
if Y > M: print(f"M {M}")
if M > Y: print(f"Y {Y}")