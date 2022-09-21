import threading
from functools import partial
from multiprocessing import Process 
from cs1robots import *

class Robot2(Robot):
    def pick_if(self):
        if (self.on_beeper()):
            self.pick_beeper()
    
    def pick_while(self):
            while (self.on_beeper()):
                self.pick_beeper()
            
    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def move_n_times_if(self, n):
        for i in range(n):
            self.pick_if()
            self.move()
            
    def move_n_times_while(self, n):
        for i in range(n):
            self.pick_while()
            self.move()
            
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
        
    def zigzag_while(self):  # 이 코드 최적화 필요함.  코드 개못생김
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
        
    # def pick_beeper(self):
    #     return super().pick_beeper()
        

            
        

load_world("/Users/hailhwan/Code/python_learning/CS/worlds/harvest2.wld")
hubo = Robot2(orientation='N')
hubo.set_trace("blue")

# for i in range(3):  # zigzag 3 times
#     hubo.zigzag_while()
# hubo.move_n_times_while(6)  # goto end of the world

# Thread(target = partial(hubo.pick_while)).start()
# for i in range(3): # zigzag
#     hubo.zigzag()
    
# p1.join(target = hubo.zigzag())
# p2.join(target = hubo.pick_while())

# if __name__ == '__main__':
#     p1 = Process(target=hubo.pick_while)
#     p1.start()
#     p2 = Process(target=hubo.zigzag())
#     p2.start()
#     p1.join()
#     p2.join()
if __name__ == '__main__':
# Create a new thread
    Thread1 = threading.Thread(target=hubo.pick_while)

    # Create another new thread
    Thread2 = threading.Thread(target=hubo.zigzag)

    # Start the thread
    Thread1.start()

    # Start the thread
    Thread2.start()

    # Wait for the threads to finish
    Thread1.join()
    Thread2.join()



'''
pick
move
pick
move
pick
move


return?

list?

move -> Temp = T
if Temp == T:
pick



줍는건 줍는거대로 계속 줍게하고 (while pick.)
움직이는건 움직이는거대로 계속 움직이게하고 (move. move. move.)
동시에 돌리고 싶은데...

방법은 MultiProcessing을 사용하는건데
이게 창 하나에 두 쓰레드를 돌리는게 안되는건지 뭔지 안되더라고..?
왜 그럴까...

일단 결론은 zigzag(), pick_while()을 동시에 돌리고 싶다~

지금 코드는 (pick, move, pick, move, pick, move ...) 이런식으로 돌아가는데
교수님도 이런식으로 푸시긴함...
근데 코드를 줄이고 싶은걸~~~~~



'''