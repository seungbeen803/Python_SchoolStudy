# while
x = 3
# 무한반복
# while x < 6:
#     print(x)

while x < 6:
    print(x)
    x += 1

print()

echo = input()
while echo != "exit":
    print(echo)
    echo = input()

print()
print()

echo = input()
while True:
    if echo == "exit":
        break
    print(echo)
    echo = input()