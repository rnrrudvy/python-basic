# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 빈 자리는 x로 채우고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:x>10}".format(500))

# 양수일 때는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마 찍기
print("{0:,}".format(100000000))

# 3자리마다 콤마 찍고, +- 부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리마다 콤마 찍고, +- 부호도 붙이고 자릿수도 확보하며 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(100000000))

# 소숫점 출력
print("{0:f}".format(5/3))

# 소숫점을 특정 자릿수까지만 표시
print("{0:.2f}".format(5/3))    # 소숫점 3째 자리에서 반올림