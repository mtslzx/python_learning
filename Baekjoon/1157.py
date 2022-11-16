# Learning Words

li = list(map(lambda x: x.upper(), list(input())))
cnt = {}
for x in li:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
        
# 아직 못품
        
max_cnt = max(cnt.values())
print(f"{max(cnt, key=cnt.get)}" if list(cnt.values()).count(max_cnt) == 1 else "?")  # (Copilot)



# https://jsikim1.tistory.com/218