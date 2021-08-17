# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for 반복문
# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1,6): # range(시작번호, 끝번호) - 범위의 숫자를 가져옴(시작번호 ~ 끝번호-1까지)
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while 반복문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer,index))
#     index += 1
    
# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


# 한 줄 for문
# 출석번호가 1,2,3,4 였는데 앞에 100을 더해서 부르기로 함(101, 102, 103, 104)
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am grrot"]
students = [len(i) for i in students] # len(x) - x의 길이(갯수)를 반환
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am grrot"]
students = [i.upper() for i in students] # x.upper() - x를 대문자로 변환하여 반환
print(students)