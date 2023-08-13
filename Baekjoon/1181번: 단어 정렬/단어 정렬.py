#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2023/08/13 22:18:52 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://blockdmask.tistory.com/450

words = dict()

for _ in range(0, int(input())):  # 단어의 개수 입력받기
    word = input()
    words[word] = len(word)  # 딕셔너리에 단어를 키로, 단어의 길이를 벨류로 입력시킨다.
for length in sorted(set(words.values())):  # 단어의 길이들을 set() 자료형으로 중복을 없애고 정렬시킵니다.
    sameLengthWords = list()  # for문 맨 처음에 같은 길이의 단어를 선언해 매 for문 반복마다 초기화합니다.
    for item in words.items():  # words 딕셔너리에 저장된 아이템들을 모두 가지고 와서 하나하나 확인합니다. (최적화가 필요해보임)
        if length == item[1]:  # item[1]은 딕셔너리의 벨류이며, 단어의 길이를 담고 있습니다. 현재 출력하고자 하는 단어의 길이와 일치한 경우
            sameLengthWords.append(item[0])  # item[0]은 딕셔너리의 키 값이며, 단어를 담고 있습니다. 이를 같은 길이의 단어들 리스트에 포함합니다.
    for word in sorted(sameLengthWords):  # 같은 길이의 단어들을 정렬해 사전순으로 출력합니다.
        print(word)  # 단어 출력과 변수 초기화단을 .pop()을 사용하게 만들어도 좋을듯 합니다.