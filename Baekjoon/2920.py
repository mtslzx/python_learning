# Music code

I = input().split()
if I == sorted(I):print("ascending")
elif I == sorted(I,reverse=True):print("descending")
else: print("mixed")

