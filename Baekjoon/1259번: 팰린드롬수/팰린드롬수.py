#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1259                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1259                           #+#        #+#      #+#     #
#    Solved: 2023/08/14 22:08:13 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://woogyun.tistory.com/519 파이썬에서의 Do While문 만들기. (파이썬에는 do가 없다.)
# https://velog.io/@sjwngjs/javascriptpython-%EC%9D%B4%EC%A4%91-for%EB%AC%B8-%ED%83%88%EC%B6%9C
# https://yeomss.tistory.com/290 파이썬 deque. popleft, rotate

from collections import deque

while True:  # 조건이 만족될 때 (0이 입력될때) 까지 반복문을 계속한다.
    testCase = input()  # 입력된 테스트 케이스를 변수에 받아준다.
    if testCase == "0": break  # 0이 입력될 경우 프로그램을 종료한다.
    if len(testCase) == 1:  # 테스트 케이스의 자릿수가 한자리인 경우
        print("yes")  # 한자리 수는 모두 팰린드롬수이므로 맞다고 출력한다.
        continue  # 다시 입력을 받기 위해 반복문 처음으로 돌아간다.
    # 아래 조건문은 팰린드롬수가 짝수인 경우가 있으므로 폐기한다.
    # if (int(testCase) % 2) == 0:  # 입력된 테스트 케이스의 값이 짝수인 경우
    #     print("no")  # 팰린드롭수는 짝수인 경우가 없으므로 아니라고 출력한다.
    #     continue  # 반복문의 처음으로 돌아간다.
    testCaseDeque = deque(testCase)  # 입력된 테스트 케이스를 덱으로 형변환을 해 문자열을 분리한다.
    # centerIdx = int(len(testCaseDeque) / 2) + 1
    for _ in range(0, int(len(testCaseDeque) / 2)):  # 덱의 길이의 절반보다 작은 값까지 반복한다.
        if testCaseDeque.pop() != testCaseDeque.popleft():  # 양쪽 끝 값들을 하나씩 덱에서 제거하면서 비교한다.
            print("no")  # 양쪽 끝 값이 서로 다를 경우 팰린드롬수가 아니라고 출력한다.
            break  # 반복문이 종료된다.
        if len(testCaseDeque) == 1 or len(testCaseDeque) == 0:  # 덱에 원소가 하나밖에 혹은 아무것도 남지 않았다면 (가운데를 제외한 혹은 모든 값들을 pop으로 꺼내서 확인했다면!)
            print("yes")  # 양쪽 모든 값들이 일치한 것이므로 팰린드롬수가 맞다고 출력한다.
