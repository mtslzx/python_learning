# OX Quiz

loop = int(input())  # 테스트 케이스 입력
for i in range(loop):  # 테스트 케이스만큼 반복
    answer = 0  # 정답 개수
    case = input() # OX case <- OOXXOXXOOO
    li_case = case.split('X')  # X를 기준으로 나눔. X는 구분자 처리됨으로 O만 남게됨.
    for j in range(len(li_case)):  # O만남은 배열 길이 만큼 반복
        answer += (len(li_case[j]) * (len(li_case[j]) + 1)) // 2 # O의 개수만큼 N까지 합을 구함. OO -> 1+2=3, OOO -> 1+2+3=6 // 가우스공식
    print(answer)  # 정답 출력





# https://devpouch.tistory.com/72