# import sys
# # sys.stdin = open('input_text.txt','r')
# read = sys.stdin.readline
# #############################################
# n = int(read())
# d = {i:set() for i in range(51)}
# for _ in range(n):
#     tmp = read().strip()
#     d[len(tmp)].add(tmp)
# for i in range(51):
#     arr = sorted(d[i])
#     for e in arr:
#         print(e)