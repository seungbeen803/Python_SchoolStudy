def sum(*numbers):
    sum_value = 0 # 초기값 설정
    for number in numbers:
        sum_value += number
    return sum_value

result = sum(1, 3)
print("1 + 3 =", result)
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))

print()

def min(*numbers):
    min_value = numbers[0] # 초기값 설정
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value
result = min(1, 3)
print("min(1, 3 =", result)
print("min(0, 3, -11) =", min(0, 3, -11))