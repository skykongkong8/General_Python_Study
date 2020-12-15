#함수
def open_account(): #함수정의하기
    print('새로운 계좌가 생성되었습니다')
open_account()

def deposit(balance, money):
    print('입금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >=money:
        print('출금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance-money))
        return balance- money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다.'.format(balance))
def withdraw_night(balance, money):
    comission = 100
    return comission, balance-money-comission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(balance)
comission, balance = withdraw_night(balance, 500)
print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(comission, balance))


#함수의 기본값
# def profile(name, age, main_lang):
#     print('name: {0}\tage:{1}\tmain_lang:{2}'\
#         .format(name,age,main_lang))
# profile('유재석',20, 'python')
# 이랬던 함수를

def profile(name, age=17, main_lang='python'):
    print('name: {0}\tage:{1}\tmain_lang:{2}'\
        .format(name,age,main_lang))
profile('유재석')
profile('김태호')
#이와 같이 동일한 기본값으로 출력가능(같은 속성을 띨 때)
# +키워드값은 순서가 바뀌어도 된다:

def profile(이름, 나이, 언어):
    print('name: {0}\tage:{1}\tmain_lang:{2}'\
        .format(이름,나이,언어))
profile(나이 = 15, 이름 = '공성식', 언어 = '스페인어')

#가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print('name: {0}\tage : {1}\t'.format(name, age), end=' ')
    print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', '20', 'python','java', 'C','C+','C#')
profile('공성식', 23, 'python','','','','')

def lang(nombre, anos, *language):
    print('nombre: {0}, anos: {1},'.format(nombre,anos), end=' ')
    for langs in language:
        print(langs, end=' ')
    print()

lang('공성식',23,'coreano','ingles','espanol')
lang('한국인',5465465,'corano')

#지역변수와 전역변수(specific/everywhere)

gun = 10
def checkpoint(soldiers):
    # gun = gun - soldiers #요기 있는 gun이 지역변수-이 함수내에서밖에 못쓴다 윗줄의 gun과 다름 그래서 밑 print에 반영이 안됌
    global gun #그래서 요렇게 global을 쓰면 전역변수화시킴 그러나 보통은 이렇게 안하고___밑에 내용 확인
    gun = gun - soldiers
    print('lef gun [in function] : {0}'.format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun- soldiers
    print('[함수 내]남은 총 : {0}'.format(gun))
    return gun #이렇게 return 을 쓰면 내부에서 계산된  gun을 밖으로 유츌시킬수 있음

print('전체 총 : {0}'.format(gun))
# checkpoint(2)
gun = checkpoint_return(gun,2) #이렇게 유출 된 gun을 받을 수 있음 
print('남은 총 : {0}'.format(gun))


# #QUIZ
# 키와 성별을 넣으면 표준 체중을 구하는 프로그램-소수점 둘째자리에서 반올림할 것. height*height*22

def std_weight(gender, height):
    if gender == 'M':
        return height*height*22
    else:
        return height*height*21
height = 155 #cm
gender = 'F'
weight = round(std_weight(gender,height/100),2)
print('성별이 {0}이고 키가 {1}이면 표준체중이 {2}입니다.'.format(gender,height,weight))










def std_weight(height, gender):
    if gender == 'male':
        return height*height*22
    else:
        return height*height*21
height = 177
gender = 'male'
weight = round(std_weight(height/100,gender),2)
print('the standard weight of {0}cm {1} is {2}kg'.format(height,gender,weight))






# #Hint풀이
# def std_weight(height, gender): #함수를 정의: 변수는 키와 성별
#     if gender == 'male': #성별이 남자이면
#         return height*height*22 #이렇게 곱한 값을 함숫값으로 내보냄
#     else:
#         return height*height*21 #성별이 남자가 아니면(여자이면) 이 값을 함숫값으로 내보냄

# height = 175 #함수에 넣을 값1: 키
# gender = 'male' # 함수에 넣을 값2 : 성별
# weight = round(std_weight(height/100, gender),2) #print하기 전 깔끔하게 시키기-함숫값 뽑아내기\
# # (아예 함수를 새로정의한다 싶을 정도로해야함) 그 뒤 정제
# print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height,gender,weight)) #최종 답안