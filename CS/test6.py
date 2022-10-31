
from cs1graphics import *
from cs1graphicsHelper import *
from time import sleep


# Break Out
canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')
# 초기 변수 세팅 
Velocity = -4  # 이 변수를 조정해서 공의 속도와 초기 방향을 조정
leftWall, rightWall, topWall, bottomWall = 5, 395, 5, 595  # 캔버스 사이즈와 공의 CenterPt에 맞추어 조정



# Player Setting ====
player = Rectangle(100, 20) # Center pt = 50, 10
player.move(200,450)  # Pos reset

# Ball Setting ====
ball = Circle(10)  # Center pt = 5, 5
b_Xpos, b_Ypos = 200, 400  # For ball pos reset
b_Xvel, b_Yvel = Velocity, Velocity  # For ball velocity reset
ball.move(-b_Xpos, -b_Ypos)  # Pos reset start to left up side
ball.setFillColor('red')


# Brick Setting ====
brick = Rectangle(100, 20) # Also Center pt = 50, 10
brick.setFillColor('blue')
brick.move(200, 100)  # Pos reset
    
    
# Add to canvas
canvas.add(ball)
canvas.add(brick)  # Add brick to canvas
canvas.add(player)  # Add player to canvas

player.wait()  # Wait for Clicking Player


# 벽돌 좌표를 스택 큐 써서 저장해놓고, 공이 벽돌에 닿으면 스택 큐에서 빼내서 삭제하는 방식으로 구현
# 벽돌을 여러개 만들고 한번에 관리가 가능할까?

    
    
    
    
score = 0

while True:  # Forever
    # Player Move ===
    player.moveTo(canvas.getMouseCoordinates().getX(), 450)  # 마우스 좌표에 따라 플레이어 이동
    print(f"Mouse:{canvas.getMouseCoordinates()} b_Xpos:{b_Xpos} b_Ypos:{b_Ypos}")
    
    # Ball Move ===
    # X-axis
    b_Xpos += b_Xvel
    if b_Xpos <= leftWall or b_Xpos >= rightWall:  # 만약 공이 벽에 닿았을 경우
        b_Xvel = -b_Xvel  # 공의 가속도 반전
    # Hit brick
    if b_Xpos == brick.getReferencePoint().getX() and b_Ypos == brick.getReferencePoint().getY():  # 만약 공이 벽돌에 닿았을 경우
    
    # Y-axis
    b_Ypos += b_Yvel
    if b_Ypos <= topWall or b_Ypos >= bottomWall:  # 만약 공이 벽에 닿았을 경우
        b_Yvel = -b_Yvel # 공의 가속도 반전
    ball.moveTo(b_Xpos, b_Ypos)  # 공의 움직임 반영
    
    # Win Game ===
    if score > 100:  # 100점 넘을시 종료
        break
    # Velocity += 0.1  # 공의 속도 증가
    sleep(0.05)
    

drawReferencePoints(canvas)
drawGrid(canvas, 100)
markClicks(canvas)


# mover = 