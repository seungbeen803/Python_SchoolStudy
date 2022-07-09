# 기본 if문
x = int(input("수 입력 : "))
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

print()

password = input("암호 입력 : ")
if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다.")

print()

x = int(input("수 입력 : "))
if x % 4 == 0:
    print("4의 배수")
elif x % 3 == 0:
    print("3의 배수")
elif x % 2 == 0:
    print("2의 배수")

print()

x = int(input("나이 입력 : "))
if 10 <= x < 20:
    print("10대")
elif 30 <= x < 40:
    print("30대")
else:
    print("10, 30대가 아님")

print()

# 중첩 제어문
# 논리 연산자를 이용한 여러 조건의 제어문
x = int(input("정수 입력 : "))
if x > 10 and x % 2 == 0:
    print("10 초과 짝수")

print()

# 중첩 제어문
x = int(input("정수 입력 : "))
if x > 10:
    if x % 2 == 0:
        print("10 초과 짝수")
    else:
        print("10 초과 홀수")
else:
    print("10 이하")
 

