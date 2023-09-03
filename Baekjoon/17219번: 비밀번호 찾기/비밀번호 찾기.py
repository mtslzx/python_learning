#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17219                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17219                          #+#        #+#      #+#     #
#    Solved: 2023/09/03 22:09:45 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, M = map(int, input().split())
passwords = dict()

# 간단하게 입력 방법에 따른 시간을 비교해보고자 한다.

# input() 사용 코드 - 80% 부터 점점 느려졌다. 49344KB 15184ms
for _ in range(N):  # 저장된 사이트 주소의 수 만큼 반복한다.
    site, password = input().split()
    passwords[site] = password  # 비밀번호가 담긴 딕셔너리에 사이트 주소를 키로, 비밀번호를 벨류로 저장한다.
for _ in range(M):  # 찾고자 하는 사이트 주소의 수 만큼 반복한다.
    print(passwords[input()])

# sys.stdin 사용 코드 -> 굉장히 빠르다...! 49176KB 224ms, 의외로 메모리도 덜 썼다..?
# for _ in range(N):  # 저장된 사이트 주소의 수 만큼 반복한다.
#     site, password = sys.stdin.readline().rstrip().split()
#     passwords[site] = password  # 비밀번호가 담긴 딕셔너리에 사이트 주소를 키로, 비밀번호를 벨류로 저장한다.
# for _ in range(M):  # 찾고자 하는 사이트 주소의 수 만큼 반복한다.
#     print(passwords[sys.stdin.readline().rstrip()])

# open(0) 사용 코드
# for _ in range(N):  # 왜 오류가 나는지 모르겠다. 사실 open(0) 조차 잘 이해가 안되긴 함... 
#     site, password = open(0).readline().rstrip().split() -> OSError: [Errno 9] Bad file descriptor