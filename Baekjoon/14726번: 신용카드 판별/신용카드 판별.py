#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14726                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14726                          #+#        #+#      #+#     #
#    Solved: 2023/08/23 22:31:16 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

for _ in range(0, int(input())):
    creditCardNumber = list(map(int, input()))
    for idx, num in enumerate(creditCardNumber, start=0):
        if idx % 2 == 0:  # 맨 우측 수부터 세어 홀수 번째 수는 그대로 두고, 짝수 번째 수를 2배로 만든다. # 맨 우측 수부터 세어나가므로, 맨 왼쪽 수는 짝수로 취급되어야 한다. 그래서 인덱스 그대로 진행하면 된다.
            if num * 2 >= 10:  # 2배로 만든 짝수 번째 수가 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.
                creditCardNumber[idx] = sum(list(map(int, str(num * 2))))
            else: creditCardNumber[idx] = num * 2
    if sum(creditCardNumber) % 10 == 0: print('T')
    else: print('F')