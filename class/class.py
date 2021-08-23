# # 마린

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# # 탱크가 추가된다면?
# # 다시 두 번째 탱크 관련 변수를 선언해야함.
# # 이런 반복을 없애기 위해 필요한 게 class

# # class 생성
# class Unit:
#     def __init__(self, name, hp, damage):   # __init__ 은 생성자라고 함
#         self.name = name    # self.name, self.hp 등을 멤버변수라고 함. 클래스 내에서 정의된 변수
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # class 사용
# marine1 = Unit("마린", 40, 5)   # class로 만들어지는 것들을 객체라고 함
# marine2 = Unit("마린", 40, 5)   # 여기서 marine1, marine2, tank는 Unit class의 인스턴스라고 함
# tank = Unit("탱크", 150, 35)    # 객체가 생성될 때는 기본적으로 init 함수에 정의된 갯수만큼의 입력이 필요(단, self는 제외)

# # 레이스
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # class 외부에서 멤버변수를 호출하여 사용가능함

# # 마인드 컨트롤
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # clocking 이라는 멤버변수는 class에 없지만 외부에서 객체에 변수를 추가하여 사용할 수 있다.
#                         # 단, 확장한 변수는 해당 객체에서만 사용가능하며 다른 객체에서는 사용할 수 없음.

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# ------------------------------------------------------------------------------

class Unit:
    def __init__(self, name, hp, damage):   # __init__ 은 생성자라고 함
        self.name = name    # self.name, self.hp 등을 멤버변수라고 함. 클래스 내에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):   # self는 자기자신을 의미, class 내에서 메소드 앞에는 항상 self를 적어준다고 생각하면 됨
        self.name = name
        self.hp = hp
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
