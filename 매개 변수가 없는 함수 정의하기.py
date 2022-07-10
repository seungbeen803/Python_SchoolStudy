import random

# 함수 사용 -- 의미 파악이 쉬워지고 수정이 쉽다.
def rolling_dice(): # 인수, 인자가 없음
    n = random.randint(1,6)
    print("6면 주사위 굴린 결과 : ", n)
rolling_dice()
rolling_dice()