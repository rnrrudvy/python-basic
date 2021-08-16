# 문자열 표기
text1 = '나는 바보다'
text2 = "나는 천재다"
text3 = """
나는 바보이자,
나는 천재이다
"""
print(text1)
print(text2)
print(text3)

# 슬라이싱
number = "123456-1234567"

print(number[0:3]) # 인덱스가 0,1,2인 값만 가져옴
print(number[:3]) # 맨 앞부터 가져오는 경우 0은 생략가능
print(number[3:]) # 맨 뒤도 동일하게 생략가능

print(number[-7:]) # 뒤에서부터 계산할 때는 -를 사용