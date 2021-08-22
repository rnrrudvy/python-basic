def std_weight(height, gender):
    if gender == "man":
        print("표준 체중 : {0} kg".format(round((height/100) * (height/100) * 22, 2)))
    else:
        print("표준 체중 : {0} kg".format(round((height/100) * (height/100) * 21, 2)))


std_weight(175, "man")
std_weight(170, "woman")


# 정답
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

