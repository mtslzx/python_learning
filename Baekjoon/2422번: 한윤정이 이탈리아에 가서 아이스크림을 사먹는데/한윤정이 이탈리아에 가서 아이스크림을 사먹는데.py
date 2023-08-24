#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2422                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2422                           #+#        #+#      #+#     #
#    Solved: 2023/08/24 22:09:10 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://juhee-maeng.tistory.com/91 파이썬 itertools 순열, 조합

from itertools import combinations

N, M = input().split()



allCombi = list(combinations(range(1, N + 1), 3))  # 3가지 맛을 섞어먹는 모든 조합을 구한다.

# badTasteCombi = 

# for i in allCombi:
#     for j in range(0, M):  # 섞어먹으면 안되는 모든 경우의 수를 구할 것이므로, 조합을 구한다.