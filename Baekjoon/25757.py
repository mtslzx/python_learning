# Minigame with imms
from math import floor

N = input().split()
for i in range(int(N[0])):
    N.append(input())
if N[1] == 'Y':
    G = 1
elif N[1] == 'F':
    G = 2
elif N[1] == 'O':
    G = 3
N.remove(N[0])
N.remove(N[0])
N = list(set(N))
print(floor(len(N)/G))