# # 지역변수, 전역변수 개념
gun = 10

# def checkpoint(soldiers):
#     gun = gun - soldiers    # 함수 밖에서 정의된 변수이므로 함수 안에서는 값이 초기화되지 않은 변수여서 오류가 발생하게 됨
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# # 위 오류를 없애는 방법1 ( 내부에 전역 변수와 같은 내용을 선언하여 사용 )
# def checkpoint(soldiers):
#     gun = 10
#     gun = gun - soldiers    # 함수 밖에서 정의된 변수이므로 함수 안에서는 값이 초기화되지 않은 변수여서 오류가 발생하게 됨
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# # 위 오류를 없애는 방법2 ( 전역 변수를 함수 안에서 쓸 수 있게 선언하여 사용 )
# def checkpoint(soldiers):
#     global gun  # 전역 변수를 함수 안에서 쓸 수 있게 만들겠다는 선언
#     gun = gun - soldiers    
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# 위 오류를 없애는 방법3 ( 입력값으로 전역변수를 함수에 전달해서 사용 )
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
