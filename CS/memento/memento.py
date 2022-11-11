from cs1graphics import *
from time import sleep #to use sleep()
from random import shuffle, randrange #to use shuffle()

paper = Canvas(640,580,'white','Memento')

path = "/Users/hailhwan/Code/python_learning/CS/memento/images/"
names = ("pororo.jpg","poby.jpg","loopy.jpg","harry.jpg","eddy.jpg","crong.jpg")

cards = []
num_pads = []
correct_list = []

tries = 1

def list_randomizer(lst):
    result = []
    while len(lst) > 0:
        index = randrange(0,len(lst))
        result.append(lst.pop(index))
    return result

def initialize():    
    for i in range(6):
        for k in range(4):
            img = Image(path+names[i])
            temp_tuple = (img,names[i])
            cards.append(temp_tuple)
            shuffle(cards)
            
    #you should shuffle the cards
    #try help(shuffle)
    
    for i in range(24):  # 1, 2, 3.. 숫자 커버 생성
        card = Layer()
        rect = Rectangle(90,120,Point(0,0))
        text = Text(str(i),18,Point(0,0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

def print_cards():
    paper.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range( len(num_pads) ):
        if i in correct_list:    # rewrite the condition for visualization.
            cards[i][0].moveTo(i_w + w, i_h+h)
            paper.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            paper.add(num_pads[i])
            
        w += 100
        if w % 600 == 0:
            w = 0
            h += 130
            
def welcome():
    randlst = list_randomizer(list(range(24)))
    for i in range(12):
        correct_list.append(randlst[i])
        correct_list.append(randlst[i+12])
        print_cards()
        # sleep(0.1)
        correct_list.remove(randlst[i])
        correct_list.remove(randlst[i+12])
    correct_list.clear()
            

isValid = lambda a, b: (a != b) and (a not in correct_list) and (b not in correct_list) and (a < 24) and (b < 24)
    # check if any of two numbers exists in the current correct list or are same number.
    # return boolean value according to the result.
    # is_triangle = lambda a, b, c: a+b > c and b+c > c and c+a > a

def check(num1,num2):
    # at first, visualize the screen including the two cards(num1-th card and num2-th card).
    # if two numbers of two cards are same, put two numbers into the correct list.
    # if not, re-visualize the original screen.
    # return boolean value according to the result.
    correct_list.append(num1); correct_list.append(num2)  # 일시적으로 두 카드를 눈에 보이게 하고, 두 카드의 그림이 같으면 correct_list에 추가
    print_cards()  # 일시적으로 두 카드를 눈에 보이게 함
    sleep(0.2)  # .2초간 확인 텀
    if cards[num1][1] == cards[num2][1]: return True # 같다면 True 반환
    else: correct_list.remove(num1); correct_list.remove(num2) # 같지 않으면 다시 원래대로
    sleep(0.8)  # .8초간 확인 텀
    print_cards(); return False  # 초기화 후 False 반환
        
initialize()
welcome()
print_cards()
print ("### Welcome to the Python Memento game!!! ###")
while len(correct_list) < 24: # rewrite the condition for termination
    print (str(tries) + "th try. You got "+str(len(correct_list)//2)+" pairs.")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    if not isValid(num1,num2):
        continue
    tries += 1
    if check(num1,num2):
        print ("Correct!")
    else:
        print ("Wrong!")
print ("### Congratulations! You got all pairs in "+str(tries)+" tries! ###")

    