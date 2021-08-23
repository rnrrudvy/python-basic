# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는 것
# 이를 다른 사람에게 공유하여 재사용이 가능함

import pickle

# profile_file = open("profile.pickle", "wb")  # pickle은 encoding 따로 안해도 됨, wb는 쓰기(w), 바이너리(b) 모드임
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()