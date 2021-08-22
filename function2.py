# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# # 기본값 사용법
# def profile(name, age=17, main_lang="파이썬"):  # 입력에 age, main_lang 값을 입력하지 않으면 기본값으로 지정한 내용이 출력됨
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


# # 키워드 호출 사용법
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# # 이처럼 함수의 값 입력 순서대로 쓰지 않아도 입력인자의 값을 지정하여 입력값으로 넣어서 사용할 수도 있다.
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


# 가변인자 사용법
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    # end=" " 를 사용하면 print문이 자동으로 개행을 하지 않음(즉, 한 줄에 다음 print문의 내용도 같이 출력되도록 할 수 있음)
    for lang in language:
        print(lang, end=" ")
    print() # 함수가 끝나면 다음줄로 넘어갈 수 있게 개행용으로 추가한 것

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")