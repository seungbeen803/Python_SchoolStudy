# 리스트 관련 내장 함수
list = ['d', 'c', 'a', 'b']
# len()
print("리스트의 길이 :", len(list))

print()

# reverse() -> 거꾸로
list.reverse()
print("리스트 항목 순서 뒤집기", list)

print()

# sort() -> 오름차순
list.sort()
print("리스트 항목 정렬하기", list)

print()

# sort(reverse=True)
list.sort(reverse=True)
print("리스트 항목 역정렬하기", list)

print()

# enumerate()
for index, value in enumerate(list):
    print("인덱스", index, "위치의 값은", value)