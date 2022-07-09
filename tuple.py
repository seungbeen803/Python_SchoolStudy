# tuple

# tuple 생성
# 빈 튜플
# t = []


xy = (2560, 1440)
print(xy)
color = 129, 247, 216
print(color)
print(xy + color)
print(xy * 3)

print()
print()

# 패킹과 언패킹
# 패킹
color = 219, 247, 216
print(color)

# 언패킹
red, green, blue = color
print(red)
print(green)
print(blue)

print()
print()

# 튜플 활용
x = 2560
print(x)
y = 1440
print(y)

# 직관적인 교환(swap)
x, y = y, x
print(x, y)

print()
print()

a = (123, "abc", True, 123, 123)
print(a)
# index() 메서드
print(a.index(True))

# count() 메서드
print(a.count(123))