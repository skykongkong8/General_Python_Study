#pickle-누군가한테 보내줘서 그사람이 받아서 쓰는것..?
# import pickle
# profile_file = open('profile.pickle','wb') #wb는 write(쓰기) binary 형식이라는 뜻
# profile = {'이름':'박명수', '나이':30, '취미':['골프','코딩']}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장
# profile_file.close()



# profile_file = open('profile.pickle','rb') #rb는 read(일기) binary라는 뜻
# profile = pickle.load(profile_file) #위에서 열어준 후 저장되어있는 피클을 load함 그래서 profile이라는 변수에 저장한것임
# print(profile)
# profile_file.close()

#with 쓰기- 열고닫기가 필요없음
# import pickle
# with open('profile.pickle','rb') as profile_file:
#     print(pickle.load(profile_file))

# with open('study.txt','w', encoding='utf8') as study_file: #한글로 쓸거니까 encodubg='utf8'이라는데 뭔소린지 모르겠음
#     study_file.write('파이썬은 너무 어려운 것 같아요')

with open('study.txt','r', encoding='utf8') as study_file: 
    print(study_file.read()) #매번 close해줄 필요가 없음

# QUIZ 보고서쓰기
#보고서 양식:
# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약 :
# 조건: 파일명은 '1주차.txt', '2주차.txt'... 와 같습니다.

# for i in range(1,51):
#     with open('{0}주차.txt'.format(i),'w', encoding='utf8') as report_form: #혹은 str(i)+'주차.txt' 이렇게 해도 된다
#         report_form.write('- {0}주차 주간보고 -'.format(i)+'\n부서:'+'\n이름:'+'\n업무 요약:')







#클래스 - 어렵지만 꼭 필요한 내용
#스타크래프트 예시: terran-marine:공격 유닛, 총을 쏜다
name = 'marine'
hp = 40
damage = 5 #공격력
print('{0} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}','공격력 {1}'.format(hp,damage))

tank_name = 'tank'
tank_hp = 150
tank_damage = 35
print('{0} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}','공격력 {1}'.format(tank_hp,tank_damage))

#공격
def attack(name, location, damage):
    print('{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(name,location,damage))

attack(name, '1시', damage)
attack(tank_name,'1시',tank_damage)

#탱크를 추가하는 방법..? 이렇게하면 시간이 너무많이든다

# tank2_name = 'tank'
# tank2_hp = 150
# tank2_damage = 35
# print('{0} 유닛이 생성되었습니다.'.format(tank2_name))
# print('체력 {0}','공격력 {1}'.format(tank2_hp,tank2_damage))
# 붕어빵처럼 찍어내는 방법? class

class Unit:
    def __init__(self, name, hp, damage): #함수처럼 init이라는 함수를 정의 __init__은 생성자: 자동으로 호출되는 부분
        self.name = name #멤버변수
        self.hp = hp #멤버변수
        self.damage = damage #멤버변수

        print('{0}유닛이 생성 되었습니다'.format(self.name))
        print('체력 {0}','공격력 {1}'.format(self.hp,self.damage))

# marine1 = Unit('마린',40,5) #이렇게 클래스로부터 생성되는 애들이 '객체'=unit 클래스의 'instance' 라고 함
# marine2 = Unit('마린',40,5)
# tank = Unit('탱크',150,35)

# #멤버변수
# wraith1 = Unit('레이스',80,5)
# print('유닛 이름 : {0}', '공격력 : {1}'.format(wraith1.name, wraith1.damage)) #이렇게 정의하지 않았어도 self로 다 대체될수있음

# #
# wraith2 = Unit('레이스',80,5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print('{0}는 현재 클로킹 상태입니다'.format(wraith2.name))

class NormalUnit:
    def __init__(self, name, hp, speed): #함수처럼 init이라는 함수를 정의 __init__은 생성자: 자동으로 호출되는 부분
        self.name = name #멤버변수
        self.hp = hp #멤버변수
        self.speed = speed
    def move(self, location):
        print('지상 유닛 이동')
        print('{0} : {1} 방향으로 이동합니다. [속도 :{2}]'.format(name, location, self.speed))



#메소드
class AttackUnit(NormalUnit):#괄호안에 다른 class이름을 넣으면 상속됨
    def __init__(self, name, hp, speed, damage): #함수처럼 init이라는 함수를 정의 __init__은 생성자: 자동으로 호출되는 부분
        NormalUnit.__init__(self,name,hp,speed)
        self.damage = damage #멤버변수

    def attack(self, location): #self는 class를 따기 위한 것일 뿐 따로 집어줄 필요 없음
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력: {2}]'.format(self.name,location,self.damage))
        #location은 안쓴 이유가 귀속되지 않은 값이기 때문에
    def damaged(self, damage):
        print('{0} : {1}이 현재채력입니다 데미지를 입었습니다.'.format(self.name, self.hp))
        self.hp -= damage
        if self.hp <= 0:
            print('{0} : 파괴되었습니다'.format(self.name))

firebat1 = AttackUnit('파이어뱃', 50,10, 16)
firebat1.attack('5시') #위에서 def한 attack 함수는 location만 있으면 됌 self 는 unit을 받기 위한 조건을 뿐임
firebat1.damaged(25)
firebat1.damaged(30)

#다중상속 그냥 Unit 과 AttackUnit 모두 name과 hp는 공유함--그냥 다 상속해서 할수 있다!
#근데 부모 클래스를 두 개 이상 받는것--참조같은 느낌으로 다양하게 사용할 수 있음을 시사


class Flyable:
    def __init__(self, flyingspeed):
        self.flyingspeed = flyingspeed
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. 속도: [{2}]'.format(name, location, self.flyingspeed))

class Flyableattack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingspeed):
        AttackUnit.__init__(self, name, hp,0, damage) #지상 스피드는 0으로 처리
        Flyable.__init__(self, flyingspeed)
    def move(self,location):
        print('공중 유닛 이동')
        self.fly(self.name, location)

# valkyre = Flyableattack('발키리',200,6,5)
# valkyre.fly(valkyre.name, '3시')

#오버로딩 메소드
vulture = AttackUnit('벌쳐', 80, 10, 20)

battlecrusier = Flyableattack('배틀크루저',500, 25, 3)

vulture.move('11시')
battlecrusier.move('9시')