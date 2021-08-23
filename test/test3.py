from random import *

sum = 0
for i in range(1,51):
    time = randrange(5,50)
    print("{0}번째 손님 (소요시간 : {1}분".format(i, time))
    if 5 <= time <= 15:
        sum += 1

print("총 탑승 승객 : {0} 분".format(sum))

# 정답
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15: # 매칭 성공한 경우
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))