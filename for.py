# for
# 기본적인 for문
# range() 함수
for x in range(3, 9,  2):
    print(x)

print()

# 문자열
for ch in "LOVE":
    print(ch)

print()

# 리스트
for item in ["힙합", "발라드"]:
    print(item + "을/를 즐겨 듣는다.")

print()

# 튜플
for item in (2560, 1440):
    print(item)

print()

# 딕셔너리
pl = {"C":1942, "Java":1995, "Python":1991}
for key in pl:
    print(key, ":", pl[key])

print()

# 세트
for item in {"HTML", "CSS3", "JavaScript"}:
    print(item + "를 할 수 있다.")

print()
print()

# 중첩 반복문
for i in range(1, 9+1):
    print("2 x {} = {}".format(i, i*2))

print()

for i in range(1, 9+1):
    print("2 x {} = {}".format(i, i*2))
for i in range(1, 9+1):
    print("3 x {} = {}".format(i, i*3))
for i in range(1, 9+1):
    print("4 x {} = {}".format(i, i*4))
for i in range(1, 9+1):
    print("5 x {} = {}".format(i, i*5))

print()
print()

for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} x {} = {}".format(dan, i, dan*i))
    print("----------------")

print()
print()

table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+ " ")
    print()

print()
print()

# break문
for i in range(1, 9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i, 2*i))

print()
print()

# countinue 문
for i in range(1, 9+1):
    if i % 2 == 0:
        continue
    print("2 x {} = {}".format(i, 2*i))

print()
print()

# 리스트 컴프리헨션
array = []
for i in range(1, 10, 2):
    array.append(i*i)
    print(array)
print()
print(array)

print()
array = [i*i for i in range(1, 10, 2)]
print(array)

print()
array = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array)