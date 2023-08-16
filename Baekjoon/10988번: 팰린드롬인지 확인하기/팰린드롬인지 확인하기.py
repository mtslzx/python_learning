#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10988                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10988                          #+#        #+#      #+#     #
#    Solved: 2023/08/16 22:49:22 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

testCase = input()  # 입력된 테스트 케이스를 변수에 받아준다.
if testCase == "0": exit  # 0이 입력될 경우 프로그램을 종료한다.
if len(testCase) == 1:  # 테스트 케이스의 자릿수가 한자리인 경우
    print("1")  # 한자리 문자열은 모두 팰린드롬이므로 맞다고 출력한다.
    exit
testCaseDeque = deque(testCase)  # 입력된 테스트 케이스를 덱으로 형변환을 해 문자열을 분리한다.
for _ in range(0, int(len(testCaseDeque) / 2)):  # 덱의 길이의 절반보다 작은 값까지 반복한다.
    if testCaseDeque.pop() != testCaseDeque.popleft():  # 양쪽 끝 값들을 하나씩 덱에서 제거하면서 비교한다.
        print("0")  # 양쪽 끝 값이 서로 다를 경우 팰린드롬이 아니라고 출력한다.
        break  # 반복문이 종료된다.
    if len(testCaseDeque) == 1 or len(testCaseDeque) == 0:  # 덱에 원소가 하나밖에 혹은 아무것도 남지 않았다면 (가운데를 제외한 혹은 모든 값들을 pop으로 꺼내서 확인했다면!)
        print("1")  # 양쪽 모든 값들이 일치한 것이므로 팰린드롬이 맞다고 출력한다.
