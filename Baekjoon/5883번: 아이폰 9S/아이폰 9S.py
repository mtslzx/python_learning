#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5883                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5883                           #+#        #+#      #+#     #
#    Solved: 2023/08/17 22:34:08 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# https://latte-is-horse.tistory.com/200 리스트에서 특정 값을 모두 제거할때 시간을 효율적으로 쓰는 방법.

queue = list()  # 대기열 리스트 생성한다.
for i in range(0, int(input())):  # 대기열 인원만큼 반복한다.
    queue.append(int(input()))  # 대기열 순서대로 리스트에 저장한다.
options = set(queue)  # 모든 용량의 가짓수를 추출해낸다.
topConsecutiveNumber = 0  # 가장 많이 연속된 구간은 몇명인지 담는 값이다.
for option in options:  # 모든 용량의 가짓수만큼 반복한다.
    testQueue = [i for i in queue if i != option]  # 대기열에서 특정 용량을 뺀 대기열을 새로운 리스트에 저장한다. list comprehension을 이용한 기술인데.. 익힐 필요가 있겠다.
    consecutiveNumber = 1  # 연속된 구간을 구하기 위한 값으로, 연속된 값이 나올때마다 +1이 될 것이다.
    for i in range(0, len(testQueue) - 1):  # 가장 많이 연속된 구간을 순회하며 찾기 위해 특정 용량이 제거된 대기열만큼 반복한다. 이후 리스트 비교에서 인덱스 오류가 나지 않도록 수정해주었다.
        if testQueue[i] == testQueue[i+1]: consecutiveNumber += 1  # 만약 n번째 값과 n+1번째 값이 같다면 연속되므로 연속 카운트에 +1을 해준다.
        if topConsecutiveNumber < consecutiveNumber:  # 지금까지 누적된 연속 카운트 보다 최고 카운트 값이 작다면
            topConsecutiveNumber = consecutiveNumber  # 최고 카운트 값을 현재 누적된 값으로 갱신한다.
        if testQueue[i] != testQueue[i+1]:  # 만약 n번째 값과 n+1번째 값이 다를경우 (값이 연속되지 않을 경우)
            consecutiveNumber = 1  # 다음 용량은 새로운 값이므로 누적 카운트를 1으로 초기화시킨다.
print(topConsecutiveNumber)  # 모든 작업이 완료되면, 최고 누적값을 출력한다.