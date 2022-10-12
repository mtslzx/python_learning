for i in range(10):
    global Wow 
    if(not (Wow in 'global')):
        Wow = 3
    Wow = Wow + 3

print(Wow)