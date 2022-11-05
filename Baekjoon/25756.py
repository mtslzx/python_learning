# Calculate Defense Ignore stat

N = int(input())
A = list(map(int, input().split()))
defStat = float(0)
for i in range(N):
    defStat = 1 - (1 - defStat) * (1 - A[i]/100)
    a = float("%g" %(defStat*100))
    if a == round(a):
        print(f"{a:.1f}")
    else:
        print(a)