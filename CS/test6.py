from cs1graphics import *
from cs1graphicsHelper import *
from time import sleep
import random
from PIL import ImageColor


# Break Out
canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')
# 초기 변수 세팅 
Velocity = -4  # 이 변수를 조정해서 공의 속도와 초기 방향을 조정
Margin = 20 # 그만좀 튀어나가 ㅠㅠ
leftWall, rightWall, topWall, bottomWall = 0 + Margin, 400 - Margin, 0 + Margin, 600 - Margin  # 캔버스 사이즈와 공의 CenterPt에 맞추어 조정



# Player Setting ====
player = Rectangle(130, 28) # Center pt = 68, 14  # 히트박스 수정
player.setBorderWidth(0)  # No border
player.move(200,450)  # Pos reset

# Ball Setting ====
ball = Circle(10)  # Center pt = 5, 5  # 히트박스가 안맞는 문제로 10을 7로 변경
b_Xpos, b_Ypos = 200, 400  # For ball pos reset
b_Xvel, b_Yvel = Velocity, Velocity  # For ball velocity reset
ball.move(-b_Xpos, -b_Ypos)  # Pos reset start to left up side
ball.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
ball.setBorderWidth(0)  # No border


# Ball Trail (Particle) =============================
# Particle Maker - From Star Generator
class Particle:
    '''
    파티클을 여러개 만들기 위해 클래스로 만들었음
    '''
    def __init__(self, x, y, life = 5, size = 0.3, deadSize = 0.8, color = "#FFFFFF"):
        '''
        x, y: 파티클이 생성될 좌표 x, y 오프셋 조정 가능함
        life: 파티클의 생명 (생명이 0이 되면 파티클이 사라짐) (.destroy로 감소)
        size: 파티클의 최초 생성 크기
        deadSize: 파티클이 사라지는 크기 (1이면 사라지지 않음) (작아지는 속도 조절)
        color: 파티클의 색상 hex color
        '''
        self.layer = Layer()
        self.life, self.size, self.deadSize = life, size, deadSize
        self.c = Circle(10);self.c_ = Circle(10)
        self.c.stretch(4, 1);self.c_.stretch(1, 4)
        self.c.setFillColor(ImageColor.getcolor(color,"RGB"));self.c_.setFillColor(ImageColor.getcolor(color,"RGB"))
        self.c.setBorderWidth(0);self.c_.setBorderWidth(0)
        self.layer.add(self.c);self.layer.add(self.c_)
        self.layer.scale(self.size)
        self.layer.moveTo(x,y)
        canvas.add(self.layer)
    def destroy(self):
        '''
        destroy(self) 호출시 마다 파티클의 생명이 1씩 감소, 0보다 작다면 제거 후 True 반환
        '''
        if not self.life <= 0:
            self.layer.scale(self.deadSize)  # 작아지는 값 변경 가능
            self.life -= 1
        else:
            canvas.remove(self.layer)
            del self
            return True

particles1 = {}
particles2 = {}
particles3 = {}

# Plife = 5
# def Particle(x, y, life, size):
#     if Plife <= 0:
#         particleLife, particleSize = life, size
#         Particle = Layer()
#         particle = Circle(10);particle_ = Circle(10)
#         particle.stretch(4, 1);particle_.stretch(1, 4)
#         particle.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"));particle_.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
#         particle.setBorderWidth(0);particle_.setBorderWidth(0)
#         Particle.add(particle);Particle.add(particle_)
#         Particle.scale(particleSize)
#         Particle.moveTo(x,y)
#         canvas.add(Particle)
        
# def ParticleRemove(particle):
#     Plife -= 1
    
#         for i in sorted(range(1, particleLife + 1), reverse=True):
#             Star.scale((particleSize / i))
#         canvas.remove(Star)
# Brick Setting ====
# Old Code
# brick = Rectangle(60, 20) # Center pt = 30, 10
# brick.setFillColor('blue')
# brick.move(200, 100)  # Pos reset
# print(brick.getReferencePoint())


# Brick Generator =================
# 초기 변수 세팅
BrickX = 60  # Brick X 크기
BrickY = 25  # Brick Y 크기
SpaceX = 60  # Brick 간의 X축 간격
SpaceY = 30  # Brick 간의 Y축 간격

brickCoordinates = [  # Brick의 좌표를 저장할 리스트 -> 갯수 정하면 자동으로 생성되게 만들 수 있을듯
[200 - SpaceX * 2,100 + SpaceY * 0], [200 - SpaceX * 1,100 + SpaceY * 0], [200,100 + SpaceY * 0], [200 + SpaceX * 1,100 + SpaceY * 0], [200 + SpaceX * 2,100 + SpaceY * 0],
[200 - SpaceX * 2,100 + SpaceY * 1], [200 - SpaceX * 1,100 + SpaceY * 1], [200,100 + SpaceY * 1], [200 + SpaceX * 1,100 + SpaceY * 1], [200 + SpaceX * 2,100 + SpaceY * 1],
[200 - SpaceX * 2,100 + SpaceY * 2], [200 - SpaceX * 1,100 + SpaceY * 2], [200,100 + SpaceY * 2], [200 + SpaceX * 1,100 + SpaceY * 2], [200 + SpaceX * 2,100 + SpaceY * 2]
]

'''
Brick Coordinate
(Center)
[            |-20-|       |-20-|         |-20-|         |-20-|                 
    |(100,100)  |  (150,100)  |  (200, 100)  |  (250, 100)  |  (300, 100)
 10 |        |-20-|       |-20-|         |-20-|         |-20-|
    |(100,120)  |  (150,120)  |  (200, 120)  |  (250, 120)  |  (300, 120)
 10 |        |-20-|       |-20-|         |-20-|         |-20-|
    |(100,140)  |  (150,140)  |  (200, 140)  |  (250, 140)  |  (300, 140)
]
벽돌 틈 사이즈는 20
벽돌 가로 사이즈는 60 세로 사이즈는 20
가운데로부터 각각 +-30, +-10이 테두리
조정 가능함
'''

# Brick Generator =================
# Brick Painter - From Gradient Generator
palete = (  # You can add more colors. Just add color hex text.
    "#070707", 
    "#12061a", 
    "#150521", 
    "#170529", 
    "#180438",
    "#170340",
    "#160248",
    "#150050", 
    "#1a0154",
    "#1e0157",
    "#23015b",
    "#28015f",
    "#2c0162",
    "#310166",
    "#36006a",
    "#3f0071"
    )

bricks = {}  # Thx to StackOverflow
for idx, pos in enumerate(brickCoordinates):  # Clone Brick With Addressed Coordinates
    bricks["brick{0}".format(idx)] = Rectangle(BrickX - 10, BrickY - 5) # Center pt = 30, 10  # 히트박스 보정을 위해 좌표보다 작게 보임
    bricks["brick{0}".format(idx)].setFillColor(ImageColor.getcolor(palete[idx],"RGB"))  # Set Color
    bricks["brick{0}".format(idx)].move(pos[0], pos[1])  # Pos reset
    canvas.add(bricks["brick{0}".format(idx)])  # Make Variable in loop. Thx to StackOverflow
    # https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
    # print(f"[DEBUG] {brick.getReferencePoint()})
# print(f"[DEBUG] {bricks}"")

for i in bricks:
    print(f"[DEBUG] {i} : {bricks[i].getReferencePoint()}")
    
# 벽돌 좌표를 리스트 써서 저장해놓고, 공이 벽돌에 닿으면 리스트에서 빼내서 삭제하는 방식으로 구현
# 벽돌을 여러개 만들고 한번에 관리가 가능할까?
# 벽돌은 무조건 100x20 사이즈로 만들고, 위치만 조정해서 여러개 만들어서 관리하는 방식으로 구현

# Add to canvas
canvas.add(ball)
# canvas.add(brick)  # Add brick to canvas
canvas.add(player)  # Add player to canvas

# TRAIN
# Main Train -> Player
Trains = Layer()
MTrain = Layer()

train_main = Rectangle(60, 26)
train_main.setBorderWidth(0)  # No border
train_main.setFillColor(ImageColor.getcolor("#190A09","RGB"))
train_main.move(0,1)
train_mainUpper = Rectangle(50, 10)
train_mainUpper.setBorderWidth(0)  # No border
train_mainUpper.setFillColor(ImageColor.getcolor("#190A09","RGB"))
train_mainUpper.move(0, -10)
train_mainWindow = Rectangle(25,7)
train_mainWindow.setBorderWidth(0)  # No border
train_mainWindow.setFillColor(ImageColor.getcolor("#FDA22B","RGB"))
train_mainWindow.move(-16, -3)
train_mainWindow_ = train_mainWindow.clone()
train_mainWindow_.move(29, 0)
MTrain.add(train_main);MTrain.add(train_mainUpper);MTrain.add(train_mainWindow);MTrain.add(train_mainWindow_)
MTrain.move(130, 436)
Trains.add(MTrain)

# 메인 기차와 한량만 추가
Train = Layer()
train_cabin = Rectangle(70, 25);train_cabin_ = Rectangle(70, 25);train_cabin__ = Rectangle(70, 25)
train_cabin.setFillColor(ImageColor.getcolor("#410D42","RGB")) #410D42  # Set Cabin Color
train_cabin_.setFillColor(ImageColor.getcolor("#190946","RGB")) #190946  # Set Cabin Color
train_cabin__.setFillColor(ImageColor.getcolor("#190A09","RGB")) #090A09  # Set Cabin Color
train_cabin_.stretch(1, 0.90);train_cabin__.stretch(1, 0.9) # Make Depth
train_cabin_.move(0,1);train_cabin__.move(0,3)  # Make Depth
train_window = Rectangle(17, 7)
train_window.setFillColor(ImageColor.getcolor("#FDA22B","RGB"))  # Set Window Color
train_window.move(-20,-3)
train_window_ = train_window.clone()
train_window_.move(20,0)
train_window__ = train_window_.clone()
train_window__.move(20,0)
train_connectingRod = Rectangle(5, 5)
train_connectingRod.setFillColor(ImageColor.getcolor("#190A09","RGB"))  # Set Connecting Rod Color
train_connectingRod.move(-38, 8)
# No Border
train_cabin.setBorderWidth(0);train_cabin_.setBorderWidth(0);train_cabin__.setBorderWidth(0)
train_window.setBorderWidth(0);train_window_.setBorderWidth(0);train_window__.setBorderWidth(0)
train_connectingRod.setBorderWidth(0)
# Add to Train Layer
Train.add(train_cabin);Train.add(train_cabin_);Train.add(train_cabin__)
Train.add(train_window);Train.add(train_window_);Train.add(train_window__)
Train.add(train_connectingRod)
Train.move(200, 436)  # move For make N trains
Trains.add(Train) # Add to Trains Layer

# Train이 옆에서 나오는 모션 연출
Trains.moveTo(0,0)
canvas.add(Trains)
Trains.adjustReference(168, 436)
Trains.moveTo(468,450)
for i in range(100):
    Trains.move(-1,0)
    sleep(0.01)
# /TRAIN

# Messages
txt_click = Text("Click Train to Start", 20)
txt_click.moveTo(200, 500)
canvas.add(txt_click)

Trains.wait()  # Wait for Clicking Player



# drawReferencePoints(canvas)
# drawGrid(canvas, 100)
# markClicks(canvas)

# Reset Variables
Score = 0
Life = 3
RandomMin = 1  # 일반화된 회전각도를 없애기 위해 랜덤값을 더해줌
RandomMax = 2  # 일반화된 회전각도를 없애기 위해 랜덤값을 더해줌 -> 대신 벽에 닿을때 마진을 늘려야함
Velocity_Accel = 1  # 재미를 위해 공의 속도를 점점 빠르게 만들어주는 변수 -> 에러가 너무 나서 못쓰겠음
Xcnt = 5 # 에러 수정용
Ycnt = 5 # 에러 수정용
Pcnt = 5 # 에러 수정용
Bcnt = 5 # 에러 수정용
X = 0 # TEST
Y = 1 # TEST
p1 = p2 = p3 = 0 # Particle test
cnt1 = cnt2 = cnt3 = 0 # Particle test
win = False

txt_life = Text("Life : " + str(Life), 15)
txt_life.moveTo(200, 520)
canvas.add(txt_life)
canvas.setAutoRefresh(True)  # Auto Refresh 함수를 찾긴 했는데 정확히 뭐하는건지는 모르겠음.

while True:  # Do Forever
    # Score Set ===
    txt_click.setMessage("Score: " + str(Score))  # 점수 표시로 변환
    txt_life.setMessage("Life: " + str(Life))  # 생명 표시
    # Player Move ===
    PlayerX = canvas.getMouseCoordinates().getX()  # 마우스 X좌표 저장
    PlayerY = 450  # Player Y좌표 고정
    player.moveTo(PlayerX, PlayerY)  # 마우스 좌표에 따라 플레이어 이동
    Trains.moveTo(PlayerX, PlayerY)  # Move Sprite
    # print(f"[DEBUG] Mouse:{canvas.getMouseCoordinates()} b_Xpos:{b_Xpos} b_Ypos:{b_Ypos} b_Xvel:{b_Xvel} b_Yvel:{b_Yvel} vel:{Velocity}")
    
    # Ball Particles  ====
    # Particle 1
    # Particle(b_Xpos,b_Ypos,5, 1)
    if p1 == cnt1:
        particles1["particles{0}".format(p1)] = Particle(b_Xpos,b_Ypos,10, 0.24, 0.9)
        cnt1 += 1  # 파티클 중복 생성 방지
    # if particles["particles{0}".format(i)].life <= 0:  # 파티클 생명이 0일 경우
    #     p += 1  # 다음 파티클로 넘어가기
    if particles1["particles{0}".format(p1)].destroy() == True:  # 파티클 생명 감소 및 삭제
        p1 += 1  # 다음 파티클로 넘어가기
    # Particle 2
    if p2 == cnt2:
        particles2["particles{0}".format(p2)] = Particle(b_Xpos+1,b_Ypos-1,15, 0.2, 0.94)
        cnt2 += 1  # 파티클 중복 생성 방지
    if particles2["particles{0}".format(p2)].destroy() == True:  # 파티클 생명 감소 및 삭제
        p2 += 1  # 다음 파티클로 넘어가기
    # # Particle 3 (Performance Issue)
    # if p3 == cnt3:
    #     particles3["particles{0}".format(p3)] = Particle(b_Xpos-3,b_Ypos+4,7, 0.1, 0.4)
    #     cnt3 += 1  # 파티클 중복 생성 방지
    # if particles3["particles{0}".format(p3)].destroy() == True:  # 파티클 생명 감소 및 삭제
    #     p3 += 1  # 다음 파티클로 넘어가기
        
    # Ball Move ===
    ball.moveTo(b_Xpos, b_Ypos)  # 공의 움직임 반영
        
    # X-axis
    b_Xpos += b_Xvel # X축 속도에 가속값을 더해줌
    if (b_Xpos <= leftWall or b_Xpos >= rightWall) and Xcnt == 0:  # 만약 공이 벽에 닿았을 경우
        Xcnt = 5  # 에러 수정용
        b_Xvel = -b_Xvel  # 공의 가속도 반전
        Velocity += Velocity_Accel  # 공의 속도 증가
    # Y-axis
    b_Ypos += b_Yvel  # Y축 속도에 가속값을 더해줌
    if (b_Ypos <= topWall) and Ycnt == 0:  # 만약 공이 벽에 닿았을 경우
        Ycnt = 5  # 에러 수정용
        b_Yvel = -b_Yvel # 공의 가속도 반전
        Velocity += Velocity_Accel  # 공의 속도 증가
    if (b_Ypos >= bottomWall) and Ycnt == 0:
        Ycnt = 5
        Life -= 1
        b_Xpos = b_Ypos =  250
        if Life <= 0:
            break
        
    # Trying to Catch Exception
    if b_Ypos >= bottomWall + Margin or b_Ypos <= topWall - Margin or b_Xpos >= rightWall + Margin or b_Xpos <= leftWall - Margin:
        print(f"[DEBUG] Exception Occured")
        ball.moveTo(250, 250)
        b_Xvel, b_Yvel = 0, 0
        Velocity = 1
        quit()
        
    
    
    # Hit brick
    for idx, pos in enumerate(brickCoordinates):  # Special Thanks to Github Copilot
        if Bcnt == 0:
            if (pos[0] - (BrickX / 2) <= b_Xpos <= pos[0] + (BrickX / 2)):
                if (pos[1] - (BrickY / 2) <= b_Ypos <= pos[1] + (BrickY / 2)):
                    Bcnt = 5
                    for i in bricks:
                            print(f"[DEBUG] {i} : {bricks[i].getReferencePoint()}")
                    print(f"[DEBUG] Hit Brick idx:{idx} pos:{pos} :{brickCoordinates} len{len(brickCoordinates)}")
                    b_Yvel = -(b_Yvel)# 가속도 반전
                    # bricks["brick{0}".format(idx)].setBorderWidth(0)  # Canvas에서 벽돌 제거 <- 여기 뭔가 문제가 있음
                    # bricks["brick{0}".format(idx)].setFillColor('transparent')  # Canvas에서 벽돌 제거
                    # try:
                    #     canvas.remove(bricks["brick{0}".format(idx)])  # Canvas에서 벽돌 제거
                    # except:
                    #     for i in bricks:
                    #         print(f"[DEBUG] {i} : {bricks[i].getReferencePoint()}")
                    brickCoordinates[idx] = (-1,-1) # 벽돌의 좌표로 공이 닿았는지 확인하므로 닿은 이후에는 제거
                    canvas.remove(bricks["brick{0}".format(idx)]) # 벽돌의 좌표로 공이 닿았는지 확인하므로 닿은 이후에는 제거
                    print(f"[DEBUG] :{brickCoordinates} len: {len(brickCoordinates)}")
                    Velocity += Velocity_Accel  # 공의 속도 증가
                    Score += 1  # 점수 추가
                    print(f"Score:{Score}")  # 점수 출력
                    break  # 반복문 탈출
            elif (pos[1] - (BrickY / 2) <= b_Ypos <= pos[1] + (BrickY / 2)):  # 공이 벽돌에 닿았을 경우 (좌표리스트 전부 확인) -> (최적화 필요)
                if (pos[0] - (BrickX / 2) <= b_Xpos <= pos[0] + (BrickX / 2)):
                    Bcnt = 5
                    for i in bricks:
                            print(f"[DEBUG] {i} : {bricks[i].getReferencePoint()}")
                    print(f"[DEBUG] Hit Brick idx:{idx} pos:{pos} :{brickCoordinates} len{len(brickCoordinates)}")
                    b_Xvel = -(b_Xvel)# 가속도 반전
                    # bricks["brick{0}".format(idx)].setBorderWidth(0)  # Canvas에서 벽돌 제거 <- 여기 뭔가 문제가 있음
                    # bricks["brick{0}".format(idx)].setFillColor('transparent')  # Canvas에서 벽돌 제거
                    # try:
                    #     canvas.remove(bricks["brick{0}".format(idx)])  # Canvas에서 벽돌 제거
                    # except:
                    #     for i in bricks:
                    #         print(f"[DEBUG] {i} : {bricks[i].getReferencePoint()}")
                    brickCoordinates[idx] = (-1,-1) # 벽돌의 좌표로 공이 닿았는지 확인하므로 닿은 이후에는 제거
                    canvas.remove(bricks["brick{0}".format(idx)]) # 벽돌의 좌표로 공이 닿았는지 확인하므로 닿은 이후에는 제거
                    print(f"[DEBUG] :{brickCoordinates} len: {len(brickCoordinates)}")
                    Velocity += Velocity_Accel  # 공의 속도 증가
                    Score += 1  # 점수 추가
                    print(f"Score:{Score}")  # 점수 출력
                    break  # 반복문 탈출
    # if b_Xpos == brick.getReferencePoint().getX() and b_Ypos == brick.getReferencePoint().getY():  # 만약 공이 벽돌에 닿았을 경우
    
    # Hit player (fixed value)
    if (PlayerX - 68 <= b_Xpos <= PlayerX + 68) and (PlayerY - 14 <= b_Ypos <= PlayerY + 14) and Pcnt == 0:
        if PlayerX < 200:  # Player가 왼쪽에 있을 경우
            b_Xvel = -b_Xvel  # 가속도 반전
        b_Yvel = -b_Yvel  # 가속도 반전
        Velocity += Velocity_Accel  # 공의 속도 증가
        print("[DEBUG] Hit player")
    
    # 에러 수정용
    Xcnt = 0 if Xcnt == 0 else Xcnt - 1
    Ycnt = 0 if Ycnt == 0 else Ycnt - 1
    Pcnt = 0 if Pcnt == 0 else Pcnt - 1
    Bcnt = 0 if Bcnt == 0 else Bcnt - 1
    # Win Game ===
    if Score >= 15:  # 100점 넘을시 종료
        win = True
        break
    # Velocity += 0.1  # 공의 속도 증가
    sleep(0.001)
    
if win == True:
    txt_life.setMessage("You Win!")
else:
    txt_life.setMessage("Game Over!")




'''
@TODO: 벽돌 부딫히는 부분 입사 반사각으로 변경
-> https://ai-creator.tistory.com/534
대각선으로 완만하게 나갈때 벽 판정에서 오류가 발생함
-> 수정 완료 (속도 높이면 다시 나갈수도..)
@TODO: 배경 별 반짝이게 만들기
@TODO: 


'''


'''
for idx,pos in enumerate(brickCoordinates):  
    brick = Rectangle(60, 20) # Center pt = 30, 10
    brick.setFillColor('blue')
    print(f"Brick {idx} : {pos} ")
    brick.move(pos[idx][0], pos[idx][1])  # Pos reset
    print(brick.getReferencePoint())

pos[idx][0]을 찾으면
int형변환 관련 에러가 나고
pos[idx]를 찾으면
인덱스 에러가 났음

C스타일로 코드를 짜다보니 이렇게 되는건지 잘 몰랐었는데
그냥 pos[0] pos[1] 이렇게 하면 됨
enumerate를 쓰면 pos에 brickCoordinates의 2차원 리스트중 1차원 원소가 들어가는듯

'''