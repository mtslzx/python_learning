from math import *

for i in range(41): #0,1,2,3,4,5,6.....,40
    # degree = # 0->0, 1->9, 2->18 ... 40->360
    # rad = #degree to radian
    # sine = sin(rad)
    # y = ax + b
    # num = #0->40, 0, 1->80, 0, -1->0, 0
    # int_num = #40, 0->40, 80, 0->80
    # print("#"*int_num)
    degree = i*9
    rad = radians(degree)
    sine = sin(rad)
    num = 40 * sine + 40
    int_num = int(num)
    print("#"*int_num)
    
    # print("하일환 바보~")
    # degrees = i*9
    # rad = radians(degrees)
    # # print("#"*int(40+ceil((sin(rad) * 40))))
    # print(40+((sin(rad) * 40)))
    
    
    
    
#make Edmund Gunter
