# dictionary
# dictionary 생성
# 빈 딕셔너리
#  d = {}
urls = {"google":"goole.com", 18:"student"}
print(urls)

print()
print()

# 딕셔너리에 요소 추가
print(urls)
urls["x"] = 2560
print(urls)

print()
print()

# 딕셔너리에 요소 수정
print(urls)
urls["x"] = 1920
print(urls)

print()
print()

# 딕셔너리에서 요소 제거
print(urls)
del urls["x"]
print(urls)

# pop() 메서드
print(urls.pop("google"))
print(urls)

# clear()
urls.clear()
print()

print()
print()

# 딕셔너리에서 요소 검색
urls = {"google":"google.com", 18:"student"}
print(urls)
print(urls[18])
print(urls.get("google"))
# 키 검색
print(18 in urls)
print("student" in urls)

print()

# 값 검색
print("google.com" in urls.values())

print()
print()

# 기타 딕셔너리 함수
print(len(urls))
# 딕서너리.keys()
print(urls.keys())
# 딕셔너리.values()
print(urls.values())
# 딕셔너리.items()
print(urls.items())