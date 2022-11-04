'''
2를 뒤집으면 5로, 5를 뒤집으면 2로, 1과 8을 뒤집으면 각각 1과 8로 보인다. 
나머지 숫자들은 뒤집었을 때의 상태를 숫자로 나타낼 수 없다. 
임스가 뒤집고자 하는 방향(상하좌우 중 하나)과 배열의 크기 N이 주어지고, 
0이 아닌 숫자(1~9)로 이루어진 N x N배열이 주어졌을 때, 
주어진 방향으로 뒤집어진 배열의 모습을 출력하시오.
첫 번째 줄에는 임스가 뒤집고자 하는 방향 W와, 배열의 크기 N이 주어진다. 
W는 L, R, U, D 중 하나이다. (2<N<=20)
입력의 두 번째 줄부터 N개의 줄에 0이 아닌 숫자가 구성된 배열이 공백으로 구분되어 주어진다.
Input   -> Output
D 3     -> 
1 2 3   ->  ? 8 ?
4 5 6   ->  ? 2 ?
7 8 9   ->  1 5 ?
'''

def vertical(n):  # 세로로 반전시켰을 때 같은 숫자 반환.
    if n == '8': return '8'
    elif n == '1': return '1'
    elif n == '2': return '5'
    elif n == '5': return '2'
    else: return '?'
    
def horizontal(n):  # 가로로 반전시켰을 때 같은 숫자 반환
    if n == '8': return '8'
    elif n == '1': return '1'
    else: return '?'    
    
def mirror(direction, arr):  # 방향에 따라 반전 및 변환 한 값 출력
    if direction == 'L' or direction == 'R':
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(vertical(arr[i][-(j+1)]), end=' ')
            print()
    else:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(vertical(arr[-(i+1)][j]), end=' ')
            print()
        
            
# if __name__ == '__main__':
direction, N = input().split()  # 방향과 배열의 크기 입력 (문자열로 입력받아서 문자열 나어서 두 변수에 할당)
N = int(N)  # N은 정수로 변환
arr = []  # 배열을 담을 리스트 생성
[arr.append(input().split()) for i in range(N)] #input().split() is a list "1 2 3" -> ['1', '2', '3']
mirror(direction,arr)
    





'''
# D 3
1 2 3
4 5 6
7 8 9
->  ARR = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

R
3 2 1
6 5 4
9 8 7




= 메모 =
(2<N<=20) 이므로 브루트포스 가능할듯
뒤집어 졌을때를 가정하고 배열의 숫자를 바꾸고,
출력할때 방향에 따른 출력하기.

2를 뒤집으면 5로, 5를 뒤집으면 2로, 1과 8을 뒤집으면 각각 1과 8로 보인다. -> 처리할 필요 없음
나머지 숫자들은 뒤집었을 때의 상태를 숫자로 나타낼 수 없다. 

1과 8은 전방향에서 뒤집어도 뒤집어진 상태가 그대로이다.
2와 5는 상하 방향에서 서로 바뀐다. 이외의 경우에는 ? 처리
이외의 숫자 나머지는 전부 ? 처리

def mirror:
    if direction == 'D' or direction == 'U':
        for array
            2 -> 5, 5 -> 2, 1 -> 1, 8 -> 8, 나머지 -> ?

    else:
        for array
            1 -> 1, 8 -> 8, 나머지 -> ?
def output:






'''