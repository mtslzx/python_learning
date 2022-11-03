
N = int(input())
M = input().split()
L = list(map(lambda x : int(x), M))
LL = float()
for i in range(N):
    LL = LL + (L[i]/max(L)*100)
print(LL/N)