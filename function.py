# 함수 선언
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 함수 선언(입력값과 반환값이 있는 함수)
def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):   # 출금
    if balance >= money: # 잔액이 출금할 금액보다 작은지 확인
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):   # 저녁에 출금, 수수료
    commission = 100
    return commission, balance - money - commission # 2개의 값 반환

# 함수 호출
open_account()

# 입금 / 함수 호출(입력값에 따른 반환값이 출력됨)
balance = 0
balance = deposit(balance, 1000)

# 출금 / 함수 호출(입력값에 따른 반환값이 출력됨)
balance = withdraw(balance, 500)

# 저녁에 출금 / 함수 호출(입력값에 따른 반환값이 출력됨, 반환값이 2개)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))