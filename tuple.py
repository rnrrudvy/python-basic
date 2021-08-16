# list보다 빠르나 한 번 설정한 값을 변경할 수 없음, 따라서 고정된 값을 사용 시 좋음

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # tuple은 add 기능을 제공하지 않으므로 에러가 발생

name = "김종국"
age = 45
hobby = "운동"
print(name, age, hobby)

# 위 내용을 tuple로 선언
name, age, hobby = "김종국", 45, "운동" # 방법 1
(name, age, hobby) = ("김종국", 45, "운동") # 방법 2
print(name, age, hobby)
