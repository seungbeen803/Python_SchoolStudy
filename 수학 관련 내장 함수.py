# 수학 관련 내장 함수
# 절댓값 : abs()
print(10, "의 절댓값 : ", abs(10))
print(-10, "의 절댓값 : ", abs(-10))

print()

# 진수 변환 : bin(), oct(), hex()
# 10진수 -> 2진수
print(128, "의 2진수 : ", bin(128))
print(128, "의 2진수 : ", bin(128))
print()
# 10진수 -> 8진수
print(7, "의 8진수 : ", oct(7))
print(8, "의 8진수 : ", oct(8))
print()
# 10진수 -> 16진수
print(15, "의 16진수 : ", hex(15))
print(16, "의 16진수 : ", hex(16))

print()
print()

# 연산 : max(), min(), sum(), pow()
numbers = [1, 5, -2, 0, 6]
# max()
print(numbers, "중 가장 큰 값은 ", max(numbers))

print()
# min()
print(numbers, "중 가장 작은 값은 ", min(numbers))

print()
# sum()
print(numbers, "합계는 ", sum(numbers))

print()
# pow()
print("2의 10승은", pow(2, 10))

print()
print()

# 반올림 : round()
pi = 3.14152
print(pi, "의 소수점 1자리 반올림은 ", round(pi))
print(pi, "의 소수점 1자리 반올림은 ", round(pi, 0))
print(pi, "의 소수점 2자리 반올림은 ", round(pi, 1))
print(pi, "의 소수점 3자리 반올림은 ", round(pi, 2))
print(pi, "의 소수점 4자리 반올림은 ", round(pi, 3))