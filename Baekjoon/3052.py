# Last

li = []
dli = []
for i in range(10):
    li.append(int(input()) % 42)
    
for i in li:
    if i not in dli:
        dli.append(i)

print(len(dli))