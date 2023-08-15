#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1032                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1032                           #+#        #+#      #+#     #
#    Solved: 2023/08/15 22:59:14 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/573 파이썬 리스트를 문자열로 출력하기

fileName = list()  # 파일명을 저장할 리스트를 생성합니다.
for i in range(0, int(input())):  # N개의 줄 만큼 반복합니다.
    fileName.append(list(input()))  # 파일명이 담긴 리스트에 파일명을 리스트 형식으로 이중 리스트로 저장합니다.
searchPattern = fileName[0]  # 검색 패턴을 추출하기 위해서 맨 처음 파일명을 가져옵니다.
for i in range(0, len(fileName[0])):  # 파일명은 모두 일정하므로 맨 처음 파일명의 길이만큼 반복합니다.
    for j in range(0, len(fileName) - 1):  # 파일명은 여러개 입력되므로 첫번째 파일명과 두번째 파일명을 참조하되, 없는 파일명을 참조해서 인덱스 에러가 나지 않도록 값을 조정해주었습니다.
        if fileName[j][i] != fileName[j + 1][i]: searchPattern[i] = "?"  # 여러 파일명중 하나라도 다른점이 발견된다면 검색패턴은 ?로 지정됩니다.
print(''.join(searchPattern))  # 리스트로 저장된 검색패턴을 문자열로 출력합니다.
