# 함수
def 장보다(상품, 장소):
    print(장소,'에 간다.')
    print(상품,"을 산다.")

장보다('우유', '편의점')

# 절댓값
print(10, "의 절댓값 : ", abs(10))
print(-10, "의 절댓값 : ", abs(-10))

# 연산
numbers = [ 1, 5, -2, 0, 6 ]
print(numbers, "중 가장 큰 값은 ", max(numbers))
print(numbers, "중 가장 작은 값은 ", min(numbers))
print(numbers, "의 합계는 ", sum(numbers))
print("2의 10승은 ", pow(2, 10))

# name = input("이름 : ")
# age = input("나이: ")
# print(name + "님! 나이는 " + str(age) + "세군요!")
# say = "{0}님의 나이는 {1}이군요".format(name, age)
# print(say)


list = [ 'q', 'e', 's', 'j']
list.sort()
print(list)
list.sort(reverse=True)
print(list)
# enumerate
for index, value in enumerate(list):
    print("인덱스", index, "위치의 값", value)
