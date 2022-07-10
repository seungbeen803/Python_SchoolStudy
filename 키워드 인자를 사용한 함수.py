# 위치 인자를 사용하여 함수 호출
def fn(a, b, c, d, e):
    print(a, b, c, d, e)
fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)

print()
print()

# 키워드 인자를 사용하여 함수 호출
def fn(a, b, c, d, e):
    print(a, b, c, d, e)
fn(1, 2, 3, 4, 5)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, e=5, d=4)

print()

# 키워드 인자는 반드시 위치 인자 다음에 나와야하기 때문에 에러 발생
# fn(d=4, e=5, 1, 2, 3)

# 가변 인수 = 위치 인자

def fn(a, b, c, *d):
    print(a, b, c, d)
# fn(c=3, b=2, a=1, 4, 5) # 키워드 인자는 위치 인자보다 앞에 나올 수 없음
# fn(1, 2, c=3, 4, 5) # 키워드 인자는 맨 뒤에 나와야 함
# fn(4, 5, a=1, b=2, c=3) # a, b에 이미 값이 있는데 중복해서 넣었기 때문