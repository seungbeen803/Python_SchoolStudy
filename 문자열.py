# 문자열
greeting = 'Hello'
to = "world!"
print(greeting)
print(type(greeting))

say_hello = greeting + ", " + to
print(say_hello) # 'Hello, world!'

print("Hello"*5)

print("\"Hello\"\n" + to)

multiline = """Happy
Programming"""
print(multiline)

# 문자열 인덱싱과 슬라이싱
# 문자열 인덱싱
s = "Life is too short."
print(s[3])
print(s[11])
print(s[-1])
print(s[-7])
print(s[-18])

# 문자열 슬라이싱
s = "Life is too short, You need Python."
print(s[3:7])
print(s[-10:-7])
print(s[3:-10])
print(s[-10:30])
print(s[3:2]) # 구할 수 없음
print(s[30])
print(s[-7:])
print(s[:4])
print(s[:-17])
print(s[:])

# 3. 문자열 함수
h = "  Happy Programming! "

print(len(h))

print(h.count("p"))

print(h.upper())

print(h.lower())

print(h.strip()) # 양쪽 공백 모두 없애기

print(h.replace("Happy", "Funny"))

print(h.find("ap"))

print(h.rfind("a"))

print(h.find("zoo")) # 찾지 못하면 -1


print("a" in h)

print("amp" in h)

x = "01::23::ab::&&"
print(x.split("::"))

y = x.split("::")
print(y)

print(", ".join(y))