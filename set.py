# set(집합) - 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "나PD"}
python = set(["유재석", "조세호"])

# 교집합 찾기( 서로 다른 집합에 있는 항목 중 중복되는 값 찾기 )
print(java & python)
print(java.intersection(python))

# 합집합 찾기 ( 서로 다른 집합에 있는 항목 중 1개 이상 있는 값 찾기 )
print(java | python)
print(java.union(python))

# 차집합 찾기 ( 서로 다른 집합에 있는 항목 중 1개 항목은 포함하지만 다른 항목은 포함하지 않는 값 찾기 )
print(java - python) # java는 할 수 있으나 python은 할 줄 모르는 사람
print(java.difference(python))

# python 할 줄 아는 사람이 늘어났을 때
python.add("김태호")
print(python)

# java를 까먹었을 때
java.remove("김태호")
print(java)