'''
ex)
[1, 1, 2, 3, 3] -> [1, 2, 3]
[4, 5, 5, 4, 6] -> [4, 5, 6]

'''



input = [1, 1, 2, 3, 3]

def solution(input):
    for i in input:
        arr = (filter(lambda x : x == i, input))
    print(arr)
    
solution(input)