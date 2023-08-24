#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1764                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1764                           #+#        #+#      #+#     #
#    Solved: 2023/08/24 22:33:04 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = input().split()
notHeard, notSeen = [], []
for _ in range(0, int(N)):
    notHeard.append(input())
for _ in range(0, int(M)):
    notSeen.append(input())
if N > M: notHeardSeen = [name for name in notSeen if name in notHeard]
else: notHeardSeen = [name for name in notHeard if name in notSeen]
notHeardSeen.sort()
print(len(notHeardSeen))
[print(name) for name in notHeardSeen]