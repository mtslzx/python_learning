#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2161                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2161                           #+#        #+#      #+#     #
#    Solved: 2023/08/29 22:06:52 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/573

from collections import deque

deck = deque(range(1, int(input()) + 1))
output = []
i = 1

while len(deck) > 1:
    if i % 2 != 0:
        output.append(deck.popleft())
    if i % 2 == 0:
        deck.append(deck.popleft())
    i += 1
output.append(deck[0])
print(' '.join(list(map(str, output))))