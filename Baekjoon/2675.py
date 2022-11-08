# Repeat String

T = int(input())
for i in range(T):
    I = input().split()
    string = list(I[1])
    for j in string:
        print(j*int(I[0]), end='')
    print()