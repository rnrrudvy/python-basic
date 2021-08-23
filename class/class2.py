# 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 일반 유닛 클래스인 Unit을 상속받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # 상속을 받는 클래스의 변수를 그대로 가져와서 사용하도록 설정, 멤버변수 초기화
        self.damage = damage

    def attack(self, location): # 얘가 메소드임
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):  # 얘도 메소드라는 건 알아야겠지?^^
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)