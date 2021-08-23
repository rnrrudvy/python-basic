# 딕셔너리 {} - key:value

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# # 주의사항
# print(cabinet[5]) # 없는 값을 요청 시 에러가 발생
# print(cabinet.get(5)) # 없는 값을 요청 시 "None"을 반환하고 넘어감
# print(cabinet.get(5, "값이 없음")) # 없는 값을 요청 시 "값이 없음"을 반환하고 넘어감

# 새 손님 추가
cabinet["C-20"] = "조세호" # 이미 존재하는 key가 있는 경우 value가 업데이트 됨
print(cabinet)
cabinet[3] = "김종국"
print(cabinet)

# 손님 퇴장
del cabinet["C-20"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 딕셔너리 초기화
cabinet.clear()
print(cabinet)