# 평균은 넘겠지

N = input()
for i in range(int(N)):
    count = 0
    stu = input().split()
    stu.remove(stu[0])
    stu = list(map(int, stu))
    avg = sum(stu)/len(stu)
    for j in range(len(stu)):
        if stu[j] > avg:
            count += 1
    print(f"{(count/len(stu))*100:.3f}%")
