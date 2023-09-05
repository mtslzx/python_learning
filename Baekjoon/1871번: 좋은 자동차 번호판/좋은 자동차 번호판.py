#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1871                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1871                           #+#        #+#      #+#     #
#    Solved: 2023/09/05 22:31:23 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/380 파이썬 절댓값 함수 abs()

for _ in range(int(input())):
  w, n = input().split('-')
  print('nice' if abs(sum([(ord(a) - 65) * 26 ** (2 - i) for i, a in enumerate(list(w))]) - int(n)) <= 100 else 'not nice')

# 아래와 같이 줄이기도 가능하다... 원리는 같으나 더 줄이는 방법을 몰라서 졌다... ㅋㅋ
# for i in[*open(0)][1:]:a,b=i.split("-");print('not '*(abs(sum((ord(x)-65)*(26**i)for i,x in enumerate(a[::-1]))-int(b))>100)+'nice')
# for i in[*open(0)][1:]:a,b=i.split("-") <- 이 부분은 원리를 한번 파악해보고 싶다.