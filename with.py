# 파일 사용을 좀 더 편하게 할 수 있음

import pickle

# with open("profile.pickle", "rb") as profile_file:  # file을 열어서 as <변수>에 저장해주고 이용하면 되며 파일 닫기도 안해도 됨
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())