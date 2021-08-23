# super
# 상속받은 멤버변수 초기화 시 부모클래스.__init__() 이 아닌 super().__init__ 으로 쓸 수 있다.
# 단, super().__init__()으로 생성 시 부모클래스.__init__()와는 달리 self를 빼주어야 한다.

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage, speed):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽(공중 유닛, 수송기능 존재, 공격기능 없음)
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# # 레이스(공중 유닛, 공격기능 존재)
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 으로 처리
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)      # 위 행과 동일한 역할을 한다. (단, super 사용시에는 self를 빼주어야 한다)
#         self.location = location

# ------------------------------------------------------------------------------------

# 다중상속시에는 super는 어떻게 동작하는가?

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):   # 두 개 이상의 상속을 받을 때 super를 사용하면 맨 처음 class 멤버변수가 초기화됨
    def __init__(self):
        super().__init__()          # 만약 2개를 다 초기화하고 싶다면 기존 방식인 부모클래스.__init__()을 각각 써주어야 함

dropship = FlyableUnit()