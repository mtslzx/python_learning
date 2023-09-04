#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25329                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25329                          #+#        #+#      #+#     #
#    Solved: 2023/09/04 22:08:56 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/566 파이썬 딕셔너리 정렬하기 - sorted() 함수의 key 매개변수를 이용하는데 더 알아볼 필요가 있음

import sys
from math import ceil

callRecords = dict()

for _ in range(int(input())):  # 테스트 케이스의 수 만큼 반복한다.
    time, name = sys.stdin.readline().rstrip().split()  # 입력된 시간과 학생의 이름을 분리하여 변수에 입력한다.
    hour, minute = map(int, time.split(":"))  # : 로 구분된 시간값을 시간, 분으로 분리해 변수에 입력한다.
    try: callRecords[name] += (hour * 60) + minute  # 전화 내역이 있을경우 추가로 전화 사용량을 누적시킨다.
    except: callRecords[name] = (hour * 60) + minute  # 특정 이름의 전화 내역이 없을경우 새로 전화 사용량을 기록한다.
[print(f"{i[0]} {10 if i[1] < 100 else 10 + ceil((i[1] - 100) / 50) * 3}") for i in sorted(dict(sorted(callRecords.items())).items(), key = lambda x:x[1], reverse=True)]  # 리스트 컴프리핸션을 사용한 for 문, 먼저 시간과 이름이 적힌 딕셔너리를 학생 이름순으로 정렬한 뒤, 시간을 내림차순으로 정렬한다, 그 다음 for문에 의해 하나씩 i로 꺼내어 print문을 수행하는데 f-string 포맷으로 이름을 먼저 출력하고 전화요금을 if문을 통해 기본요금과 추가요금을 계산해서 출력한다.
