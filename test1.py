# 내 풀이
site = "http://naver.com"

temp = site[7:]
temp = temp[0:-4]

print(temp[0:3] + str(len(temp))+ str(temp.count('e')) + "!")


# 정답
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[0:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다".format(url,password))
