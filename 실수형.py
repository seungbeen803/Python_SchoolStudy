# 실수형
# type(변수명) -> 메서드
age = 18
print(type(age)) # <class 'int'>

pi = 3.14
print(type(pi)) # <class 'float'>

age /= 2
print(type(age)) # <class 'float'>

x = 10 + 3.14
print(type(x)) # <class 'float'>

# 그 밖의 숫자 표현
# 가. 여러 가지 진수
print(0b1100111000) # 824
print(type(0b1100111000)) # <class 'int'>

print(0o130) # 88

print(0xD7A) # 3450

# 나. 지수 표현
print(10e3) # 1000.0
print(type(10e3)) # <class 'float'>

print(1.23456E2) # 123.456
print(type(1.23456E2)) # <class 'float'>

print(1.23456e22) # 1.23456e+22
print(type(1.23456e22)) # <class 'float'>

# 다. 복소수
print(8 + 24j) # (8 + 24j)

c = 1.2 + 3.4j
print(type(1.2 + 3.4j)) # <class 'complex'>

print(c.real) # 1.2 -> 실수
print(c.imag) # 3.4 -> 허수

print(c.conjugate()) # (1.2-3.4j) -> 켤레복소수

d = 1j
print(d.conjugate())
print(d * d.conjugate()) # (1+0j)