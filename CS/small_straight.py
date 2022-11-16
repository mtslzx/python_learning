## Small Straight

li = sorted(list(input()))
li = list(map(lambda x: int(x), li))


arr = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
cnt = 0

for i in range(len(arr)):
    for idx, val in enumerate(arr[i]):
        if li[idx] in arr[i]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 4:
            print("Small Straight")
            break
        
    



## 스스 경우의 수가 뭐있지
# 1, 2, 3, 4 / 2, 3, 4, 5 / 3, 4, 5, 6
# 얘네가 들어가면 되는거자나 
# 저렇게 만들라고?기래? 그럼 그것도 되게 만들면 되지

