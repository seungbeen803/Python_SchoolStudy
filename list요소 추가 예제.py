from turtle import color


colors = ["red", "green", "blue"]
print(colors)
print(type(colors))

print()

# append() 메서드
print(colors)
colors.append("blue")
print(colors)

print()

# insert() 메서드
print(colors)
colors.insert(1, "black")
print(colors)

print()

# extend() 메서드
print(colors)
colors.extend(["blue", "yellow", "white"])
print(colors)