text = "Python is Amazing"

print(text.lower()) # 소문자로 변환
print(text.upper()) # 대문자로 변환
print(text[0].isupper()) # 해당문자가 대문자인지 아닌지 확인
print(len(text)) # 문자열 길이
print(text.replace("Python", "Java")) # Python이라는 문자를 Java로 변환

index = text.index("n") # 문자열에서 n이라는 문자의 인덱스를 찾음
print(index)
index = text.index("n", index + 1) # 앞에서 찾은 index+1 위치부터 n이라는 문자의 인덱스를 찾음
print(index)

print(text.find("Java")) # 원하는 값이 없을 경우 -1을 반환
# print(text.index("Java")) # 원하는 값이 없을 경우 에러를 발생시킴

print(text.count("n")) # n이라는 값이 몇 번 나오는지 출력