# 표준입출력

# # 값 사이 사이에 sep에 지정한 값이 추가된다.
# print("Python", "Java", sep=",")
# print("Python", "Java", "C++", sep="-")

# # end는 문장의 끝부분 처리를 담당한다.(원래 print의 마지막은 개행인데 ?로 바꾼 것)
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# # 로깅 처리를 할 때 이런식으로 표준 출력과 에러를 구분할 수 있다.
# import sys
# print("Python", "Java", file=sys.stdout)    # 표준 출력
# print("Python", "Java", file=sys.stderr)    # 표준 에러

# # ljust, rjust
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():   # .items()를 사용하면 딕셔너리의 key, value를 각각 반환해준다.
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")      # .ljust(number) - 왼쪽에 number만큼의 공간을 확보한다.
#                                                                # .rjust(number) - 오른쪽에 number만큼의 공간을 확보한다.

# # zfill
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))    # .zfill(number) - number만큼의 공간을 확보하되 빈 공간은 0으로 채운다.

# input
answer = input("아무 값이나 입력하세요 : ") # input은 입력값을 str으로 변환하여 반환한다.
# print(type(answer))
print("입력하신 값은 " + answer + "입니다.")