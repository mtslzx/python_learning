#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2023/08/06 13:52:32 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/410 리스트 카운트
# https://jsikim1.tistory.com/214 리스트 중복 제거
# https://www.freecodecamp.org/korean/news/python-dictionary-methods/ 딕셔너리 fromkeys 메소드
# https://blockdmask.tistory.com/566 딕셔너리에서 value를 기반으로 정렬하기

lst = list(input().upper())  # .upper() 메소드를 사용하여 소문자를 대문자로 만들었다.
cnt = dict.fromkeys(set(lst), 0)  # 단어의 개수를 샐 딕셔너리 생성. set 함수와 fromkeys 메소드를 사용하여 문자열에 존재하는 모든 단어의 카운트가 0인채로 초기화된 딕셔너리가 생성된다.

for i in set(lst):  # set 함수로 문자열의 중복된 알파벳 제거. 문자열에 존재하는 알파벳을 하나씩만 남김.
    for j in lst:  # 문자열을 전부 분리해서 하나씩 j로 전달
        if i == j:  # 문자열에 존재하는 알파벳을 찾았다면
            cnt[i] += 1  # 알파벳 카운트 업

result = sorted(cnt.items(), key=lambda x: x[1], reverse=True)  # 조금더 이해할 필요 있음. 딕셔너리에서 value를 기반으로 정렬한건데, sorted 함수의 key와 lambda를 아직 잘 모르겠음.

if len(result) == 1:  # 문자열 길이가 1인 경우 아래의 대소 비교 코드로 인해 오류가 나는걸 방지
    print(result[0][0])
else:
    if result[0][1] == result[1][1]:  # 정렬된 딕셔너리에서 첫번째 벨류값과 두번쩨 벨류값이 일치한다면(가장 많이 사용된 알파벳이 여러 개 존재한다면) '?' 출력
        print('?')
    else:
        print(result[0][0])  # 모든 예외상황이 없다면 정상적으로 결과 출력
 