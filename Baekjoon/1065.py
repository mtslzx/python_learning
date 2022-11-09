# Han number

def han(num):
    if num < 10: return True  # 1자리 수는 무조건 한수
    split_num = list(map(int, list(str(num))))
    D = split_num[0] - split_num[1]  # 첫번째 수와 두번째 수의 차이 즉, 공차
    for i in range(len(split_num)):  # 숫자의 길이만큼 반복 (1 , 2 , 3, 4) -> 4번
        if not split_num[i] == split_num[0] - (D * i):  # 공차수열인지 판별 a(n) = a(1) - (n-1) * D 이므로 하나하나 비교
            return False  # 공차수열이 아니라면 False 리턴
    return True  # 공차수열이 맞으므로 True 리턴

I, cnt = int(input()), -1  # 왜 cnt를 -1로 해야 예제를 맞출 수 있는지 모르겠음...
for i in range(I + 1):
    if han(i): cnt += 1
print(cnt)
    

'''

첫째항 - 공차 * (n-1) = n항
이 공식이 적용되는지 판별하면 될듯


135
-> 1 3 5
5 - 3- 1 = 1

110
-> 1 1 0
0 - 1 - 1 = -2

247
-> 2 4 7
7 - 4 - 2 = 1

음 예를 들어 247이 있겠네요 첫항이 2 이고 공차가 3인 등차수열이니까요.
-> 258아님??




'''