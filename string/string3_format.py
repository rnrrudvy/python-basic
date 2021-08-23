# 문자 포맷팅

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s와 친구입니다." % "뽀로로")
print("사과는 영어로 %cpple" % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

# 방법 3
print("나는 {age}살이고, {color}색을 좋아해요.".format(age=20, color="살"))
 
# 방법 4 ( python 3.6 이상부터 가능 )
age=20
color="파랑"
print(f"나는 {age}살이고, {color}색을 좋아해요.")