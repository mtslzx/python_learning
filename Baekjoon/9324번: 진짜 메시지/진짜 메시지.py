#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9324                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9324                           #+#        #+#      #+#     #
#    Solved: 2023/08/31 22:09:10 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://studymake.tistory.com/208 for~else문

for i in range(int(input())):
    message = list(input())  # 문자열을 리스트로 만들기.
    messageCount = dict()
    for word in set(message): messageCount[word] = 0  # 문자열에 존재하는 문자들만 뽑아서 딕셔너리를 만들고 0으로 초기화
    for idx, word in enumerate(message):
        messageCount[word] += 1  # 같은 문자가 3번째 마다 있는지 확인하기 위해 문자열에 존재하는 문자 카운트 업
        if messageCount[word] == 3:  # 같은 문자가 3번째 출현했을 경우.
            try:
                if message[idx + 1] != word: # 그 다음번째 문자가 변형되어 나와야 하는 중복 문자가 맞는지 확인한다.
                    print("FAKE")  # 다른 중복문자가 나왔으므로 이 문자열은 가짜 메시지이다.
                    break  # 테스트 케이스 종료
            except:
                print("FAKE")
                break
            messageCount[word] = -1  # 중복 문자가 맞다면, 그 문자는 다시 처음부터 카운트를 시작한다. (+ 추가로 다음 문자(중복문자)도 확인하며 카운트가 올라 갈 것이므로, -1로 해주었다.)
    else: 
        print("OK")  # break 없이 확인되었으므로 올바른 메시지이다.


# for i in range(int(input())):
#     message = list(input())  # 문자열을 리스트로 만들기.
#     # wordCount, messageCount = dict(), dict()
#     # for j in message:
#     #     pass
#     # availableWords = set(message)  # 문자열에서 존재하는 문자만 뽑아내기. (최적화)
#     # for word in availableWords:
#     #     if message.count(word) >= 3:  # 문자열에 존재하는 문자들의 개수가 3개 이상인 문자만 뽑아내기. (최적화)
#     #         wordCount[word] = (message.count(word) - message.count(word) % 3) // 3  # 각 문자가 몇번 더 추가되어야 하는지 저장
#     #     messageCount[word] = message.count(word)

#     # for idx, word in enumerate(message):

#     # for word in availableWords: messageCount[word] = 0
#     messageCount = dict()
#     for word in set(message): messageCount[word] = 0  # 문자열에 존재하는 문자들만 뽑아서 딕셔너리를 만들고 0으로 초기화
#     for idx, word in enumerate(message):
#         # print(f'w = {word} idx = {idx}')
#         messageCount[word] += 1  # 같은 문자가 3번째 마다 있는지 확인하기 위해 문자열에 존재하는 문자 카운트 업
#         if messageCount[word] == 3:  # 같은 문자가 3번째 출현했을 경우.
#             try:
#                 if message[idx + 1] != word: # 그 다음번째 문자가 변형되어 나와야 하는 중복 문자가 맞는지 확인한다.
#                     print("FAKE")  # 다른 중복문자가 나왔으므로 이 문자열은 가짜 메시지이다.
#                     break  # 테스트 케이스 종료
#             except:
#                 print("FAKE")
#                 break
#             messageCount[word] = -1  # 중복 문자가 맞다면, 그 문자는 다시 처음부터 카운트를 시작한다. (+ 추가로 다음 문자(중복문자)도 확인하며 카운트가 올라 갈 것이므로, -1로 해주었다.)
#     else: 
#         print("OK")  # break 없이 확인되었으므로 올바른 메시지이다.
        

# print(f'wordCount = {wordCount}, messageCount = {messageCount}')

###
# (N - N%3) // 3
###

    # for j in range(65, 90 + 1):
    #     pass
    #     # wordCount.
    #     message.count(chr(j))