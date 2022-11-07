# Self number

def d(n: int) -> int:
    return n + sum(map(int, str(n)))  # Damm, Copilot, you're so smart!
li = list(range(1, 10001))
for i in range(1, 10001):
    if d(i) in li:
        li.remove(d(i))
    # else:
        # print(i)
print(*li)


# You need to why this code is working.