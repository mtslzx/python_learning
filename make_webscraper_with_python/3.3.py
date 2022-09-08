# elif와 and를 설명하기 위해서 다음과 같이 만든것 같은데...

age = int(input("Age: "))

if age < 18:
    print("You can't drink.")
elif age > 18 and age < 35:
    print("You drink beer.")
else:
    print("You can drink.")

# 놀랍게도 이렇게 할 필요는 없고 다음과 같이 elif 문을 써줘도 
# 똑같이 작동한다.

age = int(input("Age: "))

if age < 18:
    print("You can't drink.")
elif age < 35:
    print("You drink beer.")
else:
    print("You can drink.")

# 물론 맨 위의 코드같은 경우 18살 부분에서 else로 빠지겠지만.
# 위의 코드는 18살 역시 drink beer를 출력한다.