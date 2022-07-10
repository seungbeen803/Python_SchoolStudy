# 매개 변수가 없는 함수
# 임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다
import random

# 처음 시작
n = random.randint(1, 6) # 1에서 6까지의 정수 중에서 하나를 뽑음
print("결과 : ", n)
n = random.randint(1, 6) # 1에서 6까지의 정수 중에서 하나를 뽑음
print("결과 : ", n)
n = random.randint(1, 6) # 1에서 6까지의 정수 중에서 하나를 뽑음
print("결과 : ", n)

print()

# 코드 수정
n = random.randint(1, 6)
print("6면 주사위 굴린 결과 : ", n)
n = random.randint(1, 6)
print("6면 주사위 굴린 결과 : ", n)
n = random.randint(1, 6)
print("6면 주사위 굴린 결과 : ", n)

