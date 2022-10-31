# Nu gu in ga?
# Caution

li = list()
for i in range(28):
    li.append(int(input()))
li.sort()
li += [0,0]
i = 1
for a in range(30):
    if li[a] != i:
        print(i)
        i += 1
    i += 1

'''
val 1 2 4 5 6 7 9 10
idx 1 2 3 4 5 6 7 8
'''


'''
30번이 제출하지 않을 경우!

'''