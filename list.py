# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 타고 있는 칸 번호는?
print(subway.index("조세호"))

# 하하가 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈이 유재석과 조세호 사이에 탐
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 뒤에서부터 한 명씩 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 역순 정렬
num_list.reverse()
print(num_list)

# # 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형을 함께 수용
mix_list = ["조세호", 20, True]
print(mix_list)

# 확장
num_list.extend(mix_list)
print(num_list)