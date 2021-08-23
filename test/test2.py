from random import *

user = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(user)
happy = sample(user,4)
chicken = happy[0]
coffee = happy[1:4]

print("-- 당첨자 발표 --")
print("치킨 당첨자: %d" % chicken)
print("커피 당첨자: %s" % coffee)
print("-- 축하합니다 --")

# 정답
from random import *
users = range(1,21) # 1~20까지의 숫자를 생성
# print(type(users)) # range 생성 시 타입이 range가 됨
users = list(users) # range 타입을 list로 변환
# print(type(users))

# print(users)
shuffle(users)
# print(users)

winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")

