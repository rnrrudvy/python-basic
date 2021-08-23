# 다중상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 일반 유닛 클래스인 Unit을 상속받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # 상속을 받는 클래스의 변수를 그대로 가져와서 사용하도록 설정
        self.damage = damage

    def attack(self, location): # 얘가 메소드임
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):  # 얘도 메소드라는 건 알아야겠지?^^
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽(공중 유닛, 수송기능 존재, 공격기능 없음)
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 레이스(공중 유닛, 공격기능 존재)
class FlyableAttackUnit(AttackUnit, Flyable):   # 두 개의 class를 상속받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) # 멤버변수 초기화
        Flyable.__init__(self, flying_speed)        # 멤버변수 초기화

# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
