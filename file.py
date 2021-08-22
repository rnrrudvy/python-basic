# 파일입출력

# # file을 쓰기모드로 열어서 내용을 입력 후 닫기, 추가로 중복된 실행이 돼도 파일에는 계속 덮어쓰기 됨(내용이 +되어 기록되지 않음)
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()  # file을 열었으면 닫아주어야 함, 근데 안 닫아도 뭐가 문젠지는 모르겠음 잘됨


# # file을 추가모드로 열어서 내용을 입력 후 닫기, 기존파일에 내용이 추가됨(덮어쓰기x)
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close() 

# # file을 읽기모드로 열어서 내용 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# # file을 읽기모드로 열어서 내용 읽어오기(한 줄씩)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# # file이 총 몇줄인지 모를때 읽어오는 방법1
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# file이 총 몇줄인지 모를때 읽어오는 방법2
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()