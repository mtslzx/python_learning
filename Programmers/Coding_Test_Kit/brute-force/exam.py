'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1
수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
입출력 예 #2
모든 사람이 2문제씩을 맞췄습니다.
'''

def solution(answers):
    # 사용할 변수 초기화
    answer = []  # return에 사용할 리스트
    stu1, stu2, stu3 = 0, 0, 0  # 학생별 정답 카운터
    stu1_answers = 1  # 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    stu2_answers = 1  # 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    stu3_answers = [3, 1, 2, 4, 5]  # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    stu3_pos = 0  # stu3_answers의 인덱스값
    for i in range(0, len(answers)):  # Answers의 길이(최대 1만)동안 반복하기
        # 학생 1의 답안 코드
        if stu1_answers == 6:  # 학생 1의 문제 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로
            stu1_answers = 1  # 6 -> 1로 다시 돌려줌
        if answers[i] == stu1_answers:  # 학생 1의 답안과 문제 답안이 일치할 경우
            stu1 += 1  # 학생 1의 정답 개수 추가
        stu1_answers += 1  # 학생 1의 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
        
        # 학생 2의 답안 코드
        if (((i + 1) % 2) == 1):  # 학생 2의 답안은 홀수번째때 2가 출력되어야 하므로 2로 나눈 나머지가 1일 경우에
            if answers[i] == 2:  # 학생 2의 답안(2)과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
        else:  # 짝수번인 경우에
            if stu2_answers == 6:  # 학생 2의 문제 답안이 짝수번째때 1, 3, 4, 5, 1 ...을 반복해야 하므로
                stu2_answers = 1  # 6 -> 1로 다시 돌려줌
            elif stu2_answers == 2:  # 학생 2는 짝수번째때 2를 답하지 않으므로
                stu2_answers = 3  # 2 -> 3으로 넘겨줌
            if answers[i] == stu2_answers:  # 학생 2의 답안과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
            stu2_answers += 1  # 학생 2의 답안이 짝수번째때 1, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
                
        # 학생 3의 답안 코드
        if stu3_pos == 5:  # 학생 3의 인덱스 값이 범위를 초과되지 않도록
            stu3_pos = 0  # 5 -> 0로 다시 돌려줌
        if answers[i] == stu3_answers[stu3_pos]:  # 홀수번째와 짝수번째때
                stu3 += 1  # 학생 3의 정답 개수 추가
        if (((i + 1) % 2) != 1):  # 학생 3의 답안이 짝수번째때 다음 숫자로 넘어가므로
            stu3_pos += 1  # 학생 3 답안 배열의 인덱스값을 +1 해줌
        
    # 정답 개수 비교
    winner = max(stu1, stu2, stu3)  # 가장 많이 맞춘 답안 개수 추출
    if (stu1 == winner):  # 가장 많이 맞춘 답안 개수와 같다면
        answer.append(1)  # 추가
    if (stu2 == winner):
        answer.append(2)
    if (stu3 == winner):
        answer.append(3)
    return answer




answers = [1, 2, 3, 4, 5]  # Case1
answers = [1, 3, 2, 4, 2]  # Case2
answers = [3, 3, 2, 1, 5]  # Case3
# answers = [5, 5, 4, 2, 3]  # Case4
# answers = [2, 3, 4, 5, 1]  # Case5
# answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
# answers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
answers = [1, 3, 5, 1, 2, 3, 1, 2, 1, 5, 6]

print(solution(answers))


'''
=메모=
#1
학생 1, 2, 3을 정해서, answer에 대해 for문을 돌리도록 만들기.
학생마다 for문이 돌아가야 하므로 시간복잡도는 높은편.
하지만, 시험은 최대 1만 문제이며, 3명을 모두 합한다 하여도 최대 3만번의 연산이다.

#perusdocode
define check_answer1



#2


'''


'''
def solution(answers):
    # 사용할 변수 초기화
    answer = []  # return에 사용할 리스트
    stu1, stu2, stu3 = 0, 0, 0  # 학생별 정답 카운터
    stu1_answers = 1  # 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    stu2_answers = 1  # 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    stu3_answers = [3, 1, 2, 4, 5]  # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    stu3_pos = 0  # stu3_answers의 인덱스값
    for i in range(0, len(answers)):  # Answers의 길이(최대 1만)동안 반복하기
        # 학생 1의 답안 코드
        if stu1_answers == 6:  # 학생 1의 문제 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로
            stu1_answers = 1  # 6 -> 1로 다시 돌려줌
        if answers[i] == stu1_answers:  # 학생 1의 답안과 문제 답안이 일치할 경우
            stu1 += 1  # 학생 1의 정답 개수 추가
        stu1_answers += 1  # 학생 1의 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
        
        # 학생 2의 답안 코드
        if (((i + 1) % 2) == 1):  # 학생 2의 답안은 홀수번째때 2가 출력되어야 하므로 2로 나눈 나머지가 1일 경우에
            if answers[i] == 2:  # 학생 2의 답안(2)과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
        else:  # 짝수번인 경우에
            if stu2_answers == 6:  # 학생 2의 문제 답안이 짝수번째때 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로
                stu2_answers = 1  # 6 -> 1로 다시 돌려줌
            if answers[i] == stu2_answers:  # 학생 2의 답안과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
            stu2_answers += 1  # 학생 2의 답안이 짝수번째때 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
                
        # 학생 3의 답안 코드
        if stu3_pos == 5:  # 학생 3의 인덱스 값이 범위를 초과되지 않도록
            stu3_pos = 1  # 5 -> 0로 다시 돌려줌
        if answers[i] == stu3_answers[stu3_pos]:  # 홀수번째와 짝수번째때
                stu3 += 1  # 학생 3의 정답 개수 추가
        if (((i + 1) % 2) == 0):  # 학생 3의 답안이 짝수번째때 다음 숫자로 넘어가므로
            stu3_pos += 1  # 학생 3 답안 배열의 인덱스값을 +1 해줌
        
    # 정답 개수 비교
    winner = max(stu1, stu2, stu3)  # 가장 많이 맞춘 답안 개수 추출
    if (stu1 == winner):  # 가장 많이 맞춘 답안 개수와 같다면
        answer.append(1)  # 추가
    if (stu2 == winner):
        answer.append(2)
    if (stu3 == winner):
        answer.append(3)
    return answer
    
    
테스트 1 〉	실패 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	실패 (0.03ms, 10.1MB)
테스트 7 〉	통과 (1.59ms, 10.3MB)
테스트 8 〉	통과 (0.55ms, 10.3MB)
테스트 9 〉	통과 (3.14ms, 10.5MB)
테스트 10 〉	실패 (1.39ms, 10.3MB)
테스트 11 〉	실패 (3.08ms, 10.3MB)
테스트 12 〉	실패 (2.76ms, 10.4MB)
테스트 13 〉	실패 (0.16ms, 10.4MB)
테스트 14 〉	통과 (3.34ms, 10.3MB)
'''


'''
def solution(answers):
    # 사용할 변수 초기화
    answer = []  # return에 사용할 리스트
    stu1, stu2, stu3 = 0, 0, 0  # 학생별 정답 카운터
    stu1_answers = 1  # 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    stu2_answers = 1  # 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    stu3_answers = [3, 1, 2, 4, 5]  # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    stu3_pos = 0  # stu3_answers의 인덱스값
    for i in range(0, len(answers)):  # Answers의 길이(최대 1만)동안 반복하기
        # 학생 1의 답안 코드
        if stu1_answers == 6:  # 학생 1의 문제 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로
            stu1_answers = 1  # 6 -> 1로 다시 돌려줌
        if answers[i] == stu1_answers:  # 학생 1의 답안과 문제 답안이 일치할 경우
            stu1 += 1  # 학생 1의 정답 개수 추가
        stu1_answers += 1  # 학생 1의 답안이 1, 2, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
        
        # 학생 2의 답안 코드
        if (((i + 1) % 2) == 1):  # 학생 2의 답안은 홀수번째때 2가 출력되어야 하므로 2로 나눈 나머지가 1일 경우에
            if answers[i] == 2:  # 학생 2의 답안(2)과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
        else:  # 짝수번인 경우에
            if stu2_answers == 6:  # 학생 2의 문제 답안이 짝수번째때 1, 3, 4, 5, 1 ...을 반복해야 하므로
                stu2_answers = 1  # 6 -> 1로 다시 돌려줌
            elif stu2_answers == 2:  # 학생 2는 짝수번째때 2를 답하지 않으므로
                stu2_answers = 3  # 2 -> 3으로 넘겨줌
            if answers[i] == stu2_answers:  # 학생 2의 답안과 문제 답안이 일치할 경우
                stu2 += 1  # 학생 2의 정답 개수 추가
            stu2_answers += 1  # 학생 2의 답안이 짝수번째때 1, 3, 4, 5, 1 ...을 반복해야 하므로 1 추가
                
        # 학생 3의 답안 코드
        if stu3_pos == 5:  # 학생 3의 인덱스 값이 범위를 초과되지 않도록
            stu3_pos = 1  # 5 -> 0로 다시 돌려줌
        if answers[i] == stu3_answers[stu3_pos]:  # 홀수번째와 짝수번째때
                stu3 += 1  # 학생 3의 정답 개수 추가
        if (((i + 1) % 2) == 0):  # 학생 3의 답안이 짝수번째때 다음 숫자로 넘어가므로
            stu3_pos += 1  # 학생 3 답안 배열의 인덱스값을 +1 해줌
        
    # 정답 개수 비교
    winner = max(stu1, stu2, stu3)  # 가장 많이 맞춘 답안 개수 추출
    if (stu1 == winner):  # 가장 많이 맞춘 답안 개수와 같다면
        answer.append(1)  # 추가
    if (stu2 == winner):
        answer.append(2)
    if (stu3 == winner):
        answer.append(3)
    return answer
    
테스트 1 〉	실패 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	실패 (0.03ms, 10.2MB)
테스트 7 〉	실패 (1.63ms, 10MB)
테스트 8 〉	실패 (0.55ms, 10.4MB)
테스트 9 〉	통과 (2.99ms, 10.4MB)
테스트 10 〉	통과 (1.40ms, 10.3MB)
테스트 11 〉	실패 (3.38ms, 10.2MB)
테스트 12 〉	실패 (2.80ms, 10.1MB)
테스트 13 〉	실패 (0.18ms, 10.1MB)
테스트 14 〉	통과 (3.28ms, 10.3MB)
'''