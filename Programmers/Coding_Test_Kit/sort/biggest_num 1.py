'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''

from itertools import permutations  # 순열을 구하기 위해 라이브러리 임포트

def solution(numbers):
    permu = list(permutations(numbers))
    temp_arr = list()
    temp = str()
    # temp = list(map(lambda x: str(x), permu))
    for i in range(len(permu)):
        temp = ''
        for j in range(len(permu[0])):
            temp.join(str(permu[i][j]))
        temp_arr.append(int(temp))
    for i in range(len(permu)):
        int(temp_arr[i])
    temp_arr.sort(reverse=True)
    answer = str(temp_arr[0])
    # list(map(lambda x: permutations(x), permu))
    return answer


numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
print(solution(numbers))




'''
== 주석 ==



== 메모 ==
#1
조합해서
대소비교하고
결과값 내기

#1.5
조합해서
정렬하고
제일 큰거 결과값 내기

#2
주어진수를
정렬해서
조합하기

#2 add ------
제일 큰 숫자부터 정렬시켜서 숫자 조합을 시킬거임!
배열에서 주어진 원소의 *맨 앞자리가 큰 순서대로* 정렬
ex) [6, 10, 2] -> [6, 2, 10]
ex) [3, 30, 34, 5, 9] -> [9, 5, *34, 3, 30*]
그러려면 배열의 맨 앞자리만 따게 만들어야함.
그리고 맨 앞자리가 같은 경우 다음자리를 비교하게 만들어야하는데,
병합정렬인가 퀵정렬이 이 순서를 유지시킨다고 했었는데 그걸 찾아봐야할듯
암튼 그렇게 만들어서 정렬된 숫자를 차례대로 pop? 해서 문자열에 더함.
return.

비교하는것만 잘 만들면 될듯.




    int_arr = list()
    float_arr = list()
    count_arr = list()
    for i in range(len(numbers)):
        temp = numbers[i]
        if (temp % 10) < 10:
            int_arr.append(temp)
        else:
            count = 0
            while(temp < 10):
                temp % 10
                count += 1
            float_arr.append(temp)
            count_arr.append(count)
    int_arr.sort(reverse=True)
    float_arr.sort(reverse=True)
    for i in range(len(float_arr)):
        float_arr[i] = 
    

아하..
지금 만들다 막혔는데, 지금 짜고 있는 코드가 너무 비효율적인것 같다고 느껴져서...
홀ㄹㄹ리 쉣

이게 내가 생각한게 10보다 큰 수를 소숫점으로 만들면 맨 앞자리가 큰 순으로 정렬이 됨.
근데 이 소숫점으로 만든 친구를 다시 원상태로 복구시켜줘야하는데
순서가 정렬되면 만약 3.0이 정렬되었는데 얘한테 10을 곱해야하는지 1000을 곱해야하는지 모르잖아.
튜플인가 그... 키랑 밸류있는 친구를 어떻게 하면 될것 같기도 한데 그건 잘 몰라서 나중에 해보는 걸로..
@TODO: Key랑 Value가 있는 자료형으로 해결해보기.
그 친구가 정렬될때 Key 역시 같이 딸려간다면 Key를 확인해서 곱셈 연산을 해주면 되는데...
!!! https://leedakyeong.tistory.com/entry/python-튜플-정렬하기두-번째-원소로-정렬하기-tuple-sorting-in-python !!!
발견했다!
아 딕셔너리네
https://blockdmask.tistory.com/566
딕셔너리를 정렬해주면 될듯?




'''