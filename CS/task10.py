# from threading import Thread
from cs1robots import *
import random


class Robot(Robot):
    def pick_if(self):
        if (self.on_beeper()):
            self.pick_beeper()
    
    def pick_while(self):
        while (self.on_beeper()):
            self.pick_beeper()
            
    def turn_right(self):
        for i in range(3):
            self.turn_left()
            
    def turn_around(self):
        self.turn_left()
        self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def move_n_times_if(self, n):
        for i in range(n):
            self.move()
            self.pick_if()
            
    def move_n_times_while(self, n):
        for i in range(n):
            self.move()
            self.pick_while()
            
    def jump(self):
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()
        self.turn_right()
        self.move()
        self.turn_left()
    
    def up_stair(self):
        self.move()
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()
        
    def down_stair(self):
        self.move()
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()

    def zigzag(self):
        self.move_n_times(6)
        self.turn_right()
        self.move()
        self.turn_right()
        self.move_n_times(6)
        self.turn_left()
        self.move()
        self.turn_left()
        
    def zigzag_if(self):
        self.pick_if()
        self.move_n_times_if(6)
        self.pick_if()
        self.turn_right()
        self.pick_if()
        self.move()
        self.pick_if()
        self.turn_right()
        self.pick_if()
        self.move_n_times_if(6)
        self.turn_left()
        self.pick_if()
        self.move()
        self.pick_if()
        self.turn_left()
        self.pick_if()
        
    def zigzag_while(self):
        self.pick_while()
        self.move_n_times_while(6)
        self.pick_while()
        self.turn_right()
        self.pick_while()
        self.move()
        self.pick_while()
        self.turn_right()
        self.pick_while()
        self.move_n_times_while(6)
        self.pick_while()
        self.turn_left()
        self.pick_while()
        self.move()
        self.pick_while()
        self.turn_left()
        self.pick_while()
        
    def deploy(self):
        while (self.carries_beepers()):
            self.drop_beeper()
        
    # def pick_beeper(self):
    #     return super().pick_beeper()
    
    def front_clear_pick(self):
        while(self.front_is_clear()):
            self.move()
            self.pick_while()
    
    def move_whenLeftBlank_drop(self):  # Task 7
        while(self.front_is_clear()):
            self.move()
            if(self.left_is_clear()):
                self.drop_beeper()
    
    def smart_hurdle(self):  # Task 8
        while(not self.on_beeper()):  # Beeper에 도달할 경우 While 중단.
            if(self.on_beeper()):  # 종료조건... 이거 없애버리고 싶은데
                return 0
            counter = 0
            while(self.front_is_clear()):  # Hurdle을 넘기 위해 앞으로 이동하며 벽을 만날 때 까지 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
            self.turn_left()  # 벽을 만나면 왼쪽으로 회전.
            while(not self.right_is_clear()):  # 오른쪽에 벽이 있는동안 북쪽(위쪽)으로 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
                counter += 1
            self.turn_right()  # 오른쪽에 벽이 없으면 오른쪽으로 회전.
            self.move()  # 오른쪽으로 한 칸 이동.
            self.turn_right()  # 오른쪽으로 회전.
            for i in range(counter):  # 벽을 만날 때 까지 이동했던 칸 수만큼 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
            self.turn_left()  # 왼쪽으로 회전.
            
    def smart_zigzag(self):  # Task 9
        while(True):  # 함수가 종료될 때 까지 무한루프
            while(self.front_is_clear()):  # 전면에 벽이 나올때 까지 이동
                self.move()
            if(not self.right_is_clear()):  # 종료조건, 오른쪽에 벽이 없을경우 오른쪽으로 회전
                return 0
            self.turn_right()
            self.move()
            self.turn_right()
            while(self.front_is_clear()):  # 전면에 벽이 나올때 까지 이동
                self.move()
            if(not self.left_is_clear()):  # 종료조건, 왼쪽에 벽이 없을경우 왼쪽으로 회전
                return 0
            self.turn_left()
            self.move()
            self.turn_left()
            
    def addition(self):
        move_counter = 0  # 종료위치 초기화 설정값
        pos = 0  # 현재위치 초기화
        flag = True  # 종료위치 초기화 후 값 변환 추가 안함 플래그
        countup = False  # 다음 자리로 올려주는 수
        while(self.front_is_clear()): # 전면에 벽이 나올때 까지 이동, 1의 자리값 위치 초기화
            pos += 1
            if(flag and not self.on_beeper()):
                move_counter += 1  # 종료위치 확인
            else:
                flag = False  # 종료위치 플래그 종료    
            self.move()
        # 계산기 초기화
        while(move_counter - 1 != pos):  # 월드가 10칸 이므로 마지막 Beeper 위치까지 이동 후 종료.
            
            A = 0 # 위의 자리 계산값
            B = 0 # 밑의 자리 계산값
            
            while(self.on_beeper()):  # Beeper을 모두 수집할 때 까지 반복, 밑의 자리값 확인.
                self.pick_beeper()
                A += 1
            self.turn_left()
            self.move()
            while(self.on_beeper()):  # Beeper을 모두 수집할 때 까지 반복, 위의 자리값 확인.
                self.pick_beeper()
                B += 1
            self.turn_around()
            self.move()
            drop = (A + B + countup)
            if(A + B + countup > 10):
                countup = True
                drop = drop - 10
            else:
                drop = (A + B + countup)
                countup = False
            for i in range(drop):
                self.drop_beeper()
            self.turn_right()
            self.move()  # 다음자리로 이동됨
            pos -= 1  # 현재 위치 수정
            self.turn_around()
            
            
            
            
        
            
            


        


# Setup
load_world("/Users/hailhwan/Code/python_learning/CS/worlds/add3.wld")
hubo = Robot()
hubo.set_trace("blue")

# Task
hubo.addition()
