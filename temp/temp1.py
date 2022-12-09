text = 'Hello World!'
# text = 'Hello World! To my friends! This is a test!'  

# If text is longer then 20 characters (that on below code)
# It Doesen't work.

print(f'{text}')       # Hello World!
print(f'{text:#<20}')  # Hello World!########
print(f'{text:_>20}')  # ________Hello World!
print(f'{text:.^20}')  # ....Hello World!....
print(f'{text:^^20}')  # ^^^^Hello World!^^^^
print(f'{text: >20}')  #         Hello World!
