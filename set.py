# set
game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
# set(문자열)
print(set('Funny'))

# set(리스트)
print(set([2048, "Tetris", "Cube"]))

# set(튜플)
print(set((2560, 1440)))

# set(딕셔너리)
print(set({18:"student", "school":"mirim"}))

# set(range())
print(set(range(3)))

print()
print()

# set에 추가
# add() 메서드
print(game)
game.add("Fifa")
print(game)
print()
# update() 메서드
print(game)
game.update(("NBA", "MLB"))
print(game)

print()
print()

# set에서 제거
print(game)
game.remove("LOL")
print(game)

print()
print()

# set 연산
s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
# 교집합
s3 & s4
print(s3.intersection(s4))

# 합집합
s3 | s4
print(s3.union(s4))

# 차집합
s3 - s4
print(s3.difference(s4))

# 대칭 차집합
s3  ^ s4
print(s3.symmetric_difference(s4))

print()
print()

# 문자열, 리스트, 튜플과 함께 쓸 수 있는 함수 -> reversed()
print(list(reversed(["Happy", "Birthday"])))

print()

# 문자열, 리스트, 튜플, 딕셔너리, 튜플과 함께 쓸 수 있는 함수 -> enumerate()
for i, value in enumerate(("funny", "Python")):
    print(i, value)