#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1966                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1966                           #+#        #+#      #+#     #
#    Solved: 2023/08/22 22:19:16 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://mjmjmj98.tistory.com/83 map() 함수 - 공백 없이 입력 받기

from collections import deque

for _ in range(0, int(input())):  # 테스트 케이스의 수 만큼 반복한다.
    docNum, findNum = map(int, input().split())  # 문서의 개수, 몇번째 놓인 문서인지 # 공백을 기준으로 구분된 데이터의 개수가 2개일 경우
    printQueue = deque(map(int, input().split()))  # 큐에 담긴 문서들의 중요도 # 공백을 기준으로 구분된 정수 데이터 입력받기
    printedNum = 1  # 몇 번째로 인쇄된 것인지 확인하는 변수이다.
    while True:  # 찾고자 하는 문서가 출력될 때 까지 반복한다.
        if printQueue[0] == max(printQueue):  # 가장 앞에 있는 문서의 중요도와 큐에 담긴 문서들 중 가장 높은 문서의 중요도와 일치하다면
            if findNum == 0:  # TODO: 찾고자 하는 문서가 출력이 되는 상황
                print(printedNum)
                break
            printQueue.popleft()  # 가장 앞의 문서는 출력된 것이다.
            printedNum += 1  # 출력되었으므로 카운트 업
        else:  # 가장 앞에 있는 문서의 중요도가 가장 높은 중요도가 아닐 경우
            if findNum == 0:  # 찾고자 하는 문서가 가장 높은 중요도가 아닐 경우
                findNum = len(printQueue)  # 제일 마지막 인덱스로 옮겨진다.
            printQueue.rotate(-1)  # 맨 앞의 문서를 맨 뒤로 보내는 동시에 다른 문서들을 앞으로 보낸다.
        findNum -= 1  # 출력이 되든, 맨 뒤로 가든 찾고자 하는 문서는 한 칸 앞으로 왔으므로 인덱스 -1, # 여기서 30번째 줄의 len() 값을 인덱스 값으로 보정해주는 효과도 얻는다.
