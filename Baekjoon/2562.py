# Find Max

li = list()
for i in range(9):
    li.append(int(input()))
print(f"{max(li)}\n{li.index(max(li)) + 1}")

# 다른 방법도 있을텐데
# Max만 고르는 함수가 있을텐데에에에... 여깄다
'''
# Archive
li = list()
for i in range(9):
    li.append(int(input()))
li.sort()
print(li[-1])

'''

