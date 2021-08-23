# 오버로딩
# 부모 클래스에서 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의해서 사용하는 것

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
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
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 으로 처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")    # 상속을 받았기 때문에 부모 클래스(Unit)의 move 메소드를 사용할 수 있음
# battlecruiser.fly(battlecruiser.name, "9시")    # 상속을 받았기 때문에 부모 클래스(Flyable)의 fly 메소드를 사용할 수 있음
battlecruiser.move("9시")   # 공중 유닛 클래스에서는 move를 쓰면 [지상 유닛 이동]이라고 출력됨
                            # 그래서 FlyableAttackUnit class에서 move 메소드를 재정의하여 사용
                            # 부모 클래스에 있는 move를 그대로 쓰는 것이 아니라 FlyableAttackUnit class에서 재정의한 것을 사용

