# list 생성
 # 빈 리스트
# l = []

# list(문자열)
print(list('HAPPY'))

# list(튜플)
print(list((1125, 2436)))

# list(딕셔너리)
print(list({"menu":"pizza", "price":10000}))

# list(셋)
print(list({"사과", "배"}))

# list(range())
print(list(range(3)))

print()
print()

# list에 요소 추가
nums = list(range(3))
print(nums + [10, 11]) # 출력 때만 추가
print(nums)
nums += [10, 11] # nums 리스트의 요소로 추가 됨
print(nums)

# append() 메서드
nums.append(20)
print(nums)
nums.append([30, 31])
print(nums)

# insert() 메서드
nums.insert(2, 40)
print(nums)

# extend() 메서드
nums.extend([50, 51])
print(nums)

print()
print()

# list에 요소 수정
print(nums[7])
nums[7] = 60
print(nums)

print()
print()

# list에서 요소 제거
print(nums)
# del 리스트[인덱스]
del nums[2]

# pop() 메서드
nums.pop()
print(nums)
nums.pop(5)
print(nums)

# remove() 메서드
nums.remove(10)
print(nums)

# clear()
nums.clear()
print(nums)

print()
print()

# list에서 요소 검색
nums = list(range(3))
nums += [100, 10]
print(nums)
print(nums[3])
print(3 in nums)
print(10 in nums)

# index() 메서드
print(nums.index(10))

print()
print()

# 기타 list 관련 함수
nums = [1, 2, 4, 5, 6, 33, 6, 8]
print(len(nums))
print(nums.count(6))
print(nums)
nums.sort()
print(nums)
print()
print(nums)
nums.reverse()
print(nums)