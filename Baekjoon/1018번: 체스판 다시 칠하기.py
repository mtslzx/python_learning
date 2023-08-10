#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2023/08/10 13:47:38 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/380 파이썬 절대값 함수 abs() 사용

N, M = input().split()
Board = {'W': 0, 'B': 0}
RePaint = 0
for i in range(0, int(N)):  # N개 줄의 입력을 받도록 반복
    Line = list(input())
    Board['W'] += Line.count('W')
    Board['B'] += Line.count('B')
Half = 32
print(Board)
if Board['W'] + Board['B'] > 64:
    

if Board['W'] > Board['B']:
    RePaint += abs(Half - Board['B'])
else:
    RePaint += abs(Half - Board['W'])

print(int(RePaint))

# 문제 다시 읽고 천천히 풀어보자.