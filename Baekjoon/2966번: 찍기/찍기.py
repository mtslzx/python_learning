#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2966                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2966                           #+#        #+#      #+#     #
#    Solved: 2023/08/19 22:53:10 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# def Adrian(idx, ans):
#     if idx % 2 == 0:
#         if ans == 'B':
#             adrian += 1
#     elif idx % 3 == 0:
#         if ans == 'C':
#             adrian += 1
#     else:
#         if ans == 'A':
#             adrian += 1
# 
# def Bruno(idx, ans):
#     if idx % 2 == 0:
#         if idx % 4 == 0:
#             if ans == 'C':
#                 bruno += 1
#         elif ans == 'B':
#              bruno += 1
#     elif idx % 3 == 0:
#         if ans == 'B':
#             bruno += 1
#     else:
#         if ans == 'B':
#             bruno += 1
# 
# def Goran(idx, ans):
#     if idx % 2 == 0:
#         if ans == 'B':
#             goran += 1
#     elif idx % 3 == 0:
#         if ans == 'C':
#             goran += 1
#     else:
#         if ans == 'A':
#             goran += 1

# 위의 코드는... 굉장히 원시적으로 작성되었는데요... 하하.. 파이썬에는 덱이 있고 rotate라는 기능이 있다는 사실을 중간에 떠올려버렸습니다~

from collections import deque

N = int(input())
answer = list(input())
adrian, bruno, goran = 0, 0, 0
Adrian, Bruno, Goran = deque(['A', 'B', 'C']), deque(['B', 'A', 'B', 'C']), deque(['C', 'C', 'A', 'A', 'B', 'B'])
for idx, ans in enumerate(answer, start=1):
    if ans == Adrian[0]: adrian += 1
    if ans == Bruno[0]: bruno += 1
    if ans == Goran[0]: goran += 1
    Adrian.rotate(-1)
    Bruno.rotate(-1)
    Goran.rotate(-1)

max_answer = max(adrian, bruno, goran)
print(max_answer)
if adrian == max_answer: print("Adrian")
if bruno == max_answer: print("Bruno")
if goran == max_answer: print("Goran")





