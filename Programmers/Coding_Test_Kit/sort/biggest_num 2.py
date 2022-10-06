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

import math
from re import T

def solution(numbers):
    int_arr = list()
    float_arr = dict()
    count_arr = list()
    for i in range(len(numbers)):
        temp = numbers[i]
        if temp < 10:
            int_arr.append(temp)
        else:
            count = 0
            while(temp > 10):
                temp /= 10
                count += 1
            float_arr[i] = temp  # [*1]
            count_arr.append(count)
    # int_arr.sort(reverse=True)
    item_float_arr = list(float_arr.items())  # items 매소드는 리스트 객체를 반환하므로, 리스트 함수로 리스트로 만들어줘야함
    sorted_float_arr = sorted(list(item_float_arr), key = lambda x:x[1], reverse=True)  # value를 key로 정해 key값에 따라 정렬. (딕셔너리의 key가 아니다.)
    # decrypt_arr = sorted_float_arr.keys()  # float이 정렬된 값에 맞추어 key 값 역시 정렬되었으므로 복원때 필요한 배열을 할당 [*2]
    decrypt_arr = list(filter(lambda x: x[0], sorted_float_arr))  # float이 정렬된 값에 맞추어 key 값 역시 정렬되었으므로 복원때 필요한 배열을 할당 [*2]
    arr = sorted(int_arr + sorted_float_arr, reverse=True)  # arr 리스트로 두 리스트 합치기 및 내림차순 정렬
    for i in range(len(arr)):  # 소수점으로 변환된 값 복원하기, 합쳐진 리스트 길이만큼 반복.
        num = 1  # float, count 배열 길이를 맞춰주기 위한 변수
        if type(arr[i]) == type(float):  # int를 제외한 float형일 경우 순서대로일 것이므로, float_arr의 순서(key를 사용해서 곱해주기 위해)를 활용
            arr[i] = arr[i] * (10 * count_arr[decrypt_arr[num]])  # 배열의 길이가 float형만 있는것은 아니므로 float만큼의 배열을 액세스 할 수 있도록 하는 새로운 변수
            
    print(arr)
    answer = ''
    return answer


# numbers = [6, 10, 2]
numbers = [3, 30 , 34, 5, 9]
print(solution(numbers))




'''
== 주석 ==
[*1]
딕셔너리 자료형으로 순서가 정렬되어도 

[*2]
decrypt_arr example
index [0, 1, 2, 3, 4, ...]
value [5, 3, 1, 2, 8, ...]



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