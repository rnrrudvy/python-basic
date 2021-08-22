for i in range(1,51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : ")


# 정답
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")