#Pass :  건물을 만든다고 하자(스타 연장
# class Unit:
#     def __init__(self, name, hp, damage): #함수처럼 init이라는 함수를 정의 __init__은 생성자: 자동으로 호출되는 부분
#         self.name = name #멤버변수
#         self.hp = hp #멤버변수
#         self.damage = damage #멤버변수

#         print('{0}유닛이 생성 되었습니다'.format(self.name))
#         print('체력 {0}','공격력 {1}'.format(self.hp,self.damage))
#저번 내용 unit을 상속함

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass #아무것도 안하고 일단 init 함수에서 별도로 정의안하고 넘어간다는 뜻. 
# #서플라이 디폿- 1건물-8유닛 생성 (파이런같은것)

# supply_depot = BuildingUnit('서플라이 디폿', 500, '7')

# # pass는 다른 곳에서도 쓸 수 있음
# def game_start():
#     print('[알림] 새로운 게임을 시작합니다.')
# def game_over():
#     pass
# game_start()
# game_over() #출력해보면 보이는 바와 같이 거의 해시태그한 급으로 그냥 넘어가는 것을 볼 수 있음


#Super
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0) 이렇게 쓸 수도 있지만 super을 활용할 수도 있음
#         super().__init__(name, hp, 0)#똑같은 거지만, super을 쓸때는 괄호()를 써주고 self를 쓰지 않음. 이 점 주의할 것 
#         #문제는 다중 상속을 할 때 일어남--아래 #내용 참조
#         self. location = location

# supply_depot = BuildingUnit('서플라이 디폿', 500, '7')

# def game_start():
#     print('[알림] 새로운 게임을 시작합니다.')
# def game_over():
#     pass
# game_start()
# game_over()

#super의 다중 상속시 문제점
# class Unit:
#     def __init__(self):
#         print('Unit 생성자')
# class Flyable:
#     def __init__(self):
#         print('Flyable 생성자')
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()

# dropship = FlyableUnit() #보는 바와 같이 super을 써버리면 순서 상 맨 마지막 상속만 챙겨줌.... 그래서 다중상속을 할 때는 따로
# # Unit.__init__(self) 일일히 넣어줄 것.




#실제 프로그래밍 해보기!!

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0}유닛이 생성 되었습니다'.format(self.name))
    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격하려 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린',40,1,5)
    def steampack(self):
        if self.hp >= 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. [HP 10 감소]'.format(self.name))
        else:
            print('{0} : 체력이 10 이하이므로 스팀팩을 사용할 수 없습니다.'.format(self.name))
class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, '탱크',150,1,35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage *=2
            self.seize_mode = True
        else:
            print('{0} : 시즈모드를 해제합니다.'.format(self.name))
            self.damage *=0.5
            self.seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(self.name, location, self.flying_speed))
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed=0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,'레이스', 80, 20, 5)
        self.clocked = False
    def clocking(self):
        if self.clocked == True:
            print('{0} : 클로킹 모드를 해제합니다'.format(self.name))
            self.clocked = False
        else:
            print('{0} : 클로킹 모드를 실행합니다'.format(self.name))
            self.clocked = True

gamer = 'skykongkong8'
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')
def game_over():
    print('{0} : GG'.format(gamer))
    print('{0} 님이 게임에서 퇴장하셨습니다.'.format(gamer))

#실제 게임 진행
from random import* #나중에 난수 쓰게됨
game_start()

#유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리-리스트 작성+append처리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move('1시')

Tank.seize_developed = True
print('[알림] 탱크 시즈모드가 개발되었습니다.')

#공격모드 준비-기능 가동
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.steampack() #isinstance-객체가 특정 class의 소속인 것인지 확인해서 처리하는 기능
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack('1시')

#피해 입기
for unit in attack_units:
    unit.damaged(randint(10,100)) #5~20사이의 피해

game_over()


#QUIZ
#매물:
# 강남 아파트 매매 10억 2010
# 마포 오피스텔 전세 5억 2007
# 송파 빌라 월세 500/50 2000

class House:
    def __init__(self, location, house_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print('{0} {1} {2} {3}'.format(self.location, self.house_type, self.price, self.completion_year))
# Apartment = House('강남', '매매', '10억', 2010)
# Office_Tel = House('마포', '전세', '5억', 2007)
# Villa = House('송파','월세', '500/50', 2000)
# Apartment.show_detail()
# Office_Tel.show_detail()
# Villa.show_detail()

house = []
Apartment = House('강남', '매매', '10억', 2010)
Office_Tel = House('마포', '전세', '5억', 2007)
Villa = House('송파','월세', '500/50', 2000)
house.append(Apartment)
house.append(Office_Tel)
house.append(Villa)

print('총 {0}대의 매물이 있습니다'.format(len(house)))
for houses in house:
    houses.show_detail()