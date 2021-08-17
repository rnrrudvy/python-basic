# 반복문에서 사용되는 continue, break

absent = [2,5] # 결석자 번호
no_book = [7] # 책 없는 사람 번호
for student in range(1,11):
    if student in absent:
        continue # 아래 문장을 실행시키지 않고 다음 반복루프로 이동하는 것
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복루프 자체를 벗어남(종료함)
    print("{0}, 책을 읽어봐".format(student))

