# bool
a = True
b = False
print(type(a))

print()

# 비트 연산자
# bin()함수를 이용하여 이진수(0b)로 표현
print(bin(0b1010))
# & -> 둘다 1이어야 1 나머지 0
print(0b1010 & 0b0110)
print(bin(0b1010 & 0b0110))

# | -> 둘 중 하나만 1이어도 1 둘 다 0일 때 0
print(0b1010 | 0b0110)
print(bin((0b1010 | 0b0110)))

# ^ -> 같으면 0, 다르면 1
print(0b1010 ^ 0b0110)
print(bin((0b1010 ^ 0b0110)))

# ~ -> 0이면 1, 1이면 0 서로 반대
print(~0b1010)
print(bin((~0b1010)))

# <<
print(0b1010 << 2)
print(bin((0b1010 << 2)))

# >>
print(0b1010 >> 2)
print(bin((0b1010 >> 2)))
