def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("▲")
p("A", "▲")
p("A", "B", "C")

print()

# 고정된 인자를 받고 그 이후 개수는 가변 인자로 받아 출력
def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)
p(",", 3, "▲", "@")
p("_", 2, "&", "#", "$")