# Sangsu ( Copilot )
# 734 893 -> 437
I = input().split()


def sangsu(x):
    return int(x[::-1])

print(max(sangsu(I[0]), sangsu(I[1])))



# String[::-1] -> reverse string
# String[::N] -> ?

# String.split() -> split string by space
# String.split(' ') -> split string by space