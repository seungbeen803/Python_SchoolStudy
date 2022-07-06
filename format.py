# format 함수
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))

print("name: {name}, number: {num}".format(name="Jordan", num = 23))

# 정수를 표현하는 여러 가지 방법
# 정수를 넣는다
print("{:d}".format(515))

# 최소 5칸을 차지하고 정수를 넣는다
print("{:5d}".format(515))

# 양수면 +를 표시한다
print("{:+5d}".format(515))

# +를 맨 앞에 표시한다
print("{:=+5d}".format(515))

# 빈칸은 0으로 채운다
print("{:05d}".format(515))

# 양수면 0앞에 +를 표시한다
print("{:+05d}".format(515))

# 실수를 표현하는 여러 가지 방법
# 실수를 넣는다
print("{:f}".format(11.17))

# 최소 12칸을 차지하고 실수를 넣는다
print("{:12f}".format(11.17))

# 소수점 1자리까지 반올림해서 나타낸다
print("{:12.1f}".format(11.17))


# 문자열 format을 사용하여 양수 11.17을 '+ 11.2로 출력해보자'
print("{:=+6.1f}".format(11.17))