# #에러처리하기 계산기 만들기 try와 except 활용하기--강제종료/에러 발생을 줄임으로서 프로그램의 완성도 높임
# try:
#     print('나누기 전용 계산기 입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
#     # nums.append(int(nums[0] / nums[1]))
#     print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
# except BigNumberError:
#     print('에러! 잘못된 값을 input했습니다.')
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print('알 수 없는 오류가 발생하였습니다!')



#에러 발생시키기- 한 자리 숫자 나누기 전용 계산기
# try:
#     print('한 자리 숫자 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#     num2 = int(input('escribir numeri segundo : '))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print('에러!')


# #사용자 정의 예외처리-ValueError나 ZeroDivisionError는 파이썬에서 제공하고 있는 것이고 직접 새로 에러의 유형을 정의해서 사용하기
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg #이거 안하고 그냥 pass 써도되는데 그러면 msg를 쓸수가없음-입력값을 다시 알게 해준다던지 식의 에러 상황에
#         # 대한 묘사가 부족해짐
# try:
#     print('한 자리 숫자 전용 계산기입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#     num2 = int(input('escribir numeri segundo : '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except BigNumberError as err:
#     print('에러!')
#     print(err)
# #ㄴ BigNumberError로 정의해서 해도 통함
# # Finally-예외 처리 중 정상이건 오류건 무조건 실행되는 구문
# finally:
#     print('계산기를 이용해 주셔서 감사합니다.')






#Quiz 예외처리 구문짜기
# 1보다 작거나 숫자가 아닌 입력값이 들어오면 ValueError처리-'잘못된 값을 입력하셨습니다.'
# 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정-치킨소진시 사용자정의에러[SoldOutError]를 발생시키고 프로그램 종료메시지
# ㄴ'재고가 소진되어 더 이상 주문을 받지 않습니다.'

# class SoldoutError(Exception):
#     def __init__(self,messege):
#         self.messege = messege
#     def __str__(self):
#         return self.messege
# try:
#     chicken = 10
#     waiting = 1
#     while(True):
#         print('[남은 치킨 : {0}]'.format(chicken))
#         order = int(input('치킨 몇 마리 주문하시겠습니까?'))
#         if order >= chicken:
#             print('재료가 부족합니다.')
#         if chicken <= 0:
#             print('재료가 부족합니다.')
#         if chicken <= 0:
#             raise SoldoutError('재고가 소진되어 더 이상 주문을 받지 않습니다.')
#         # if order == int:
#         #     raise ValueError
#         if order <= 0:
#             raise ValueError
#         else:
#             print('대기번호 {0} 손님 {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
#             waiting += 1
#             chicken -= order

# except SoldoutError as err:
#     print(err)
# except ValueError:
#     print('잘못된 값을 입력하셨습니다.')

# finally:
#     print('콩콩치킨을 이용해 주셔서 감사합니다.')















#200914-똑같은 python workplace 에 있기 떄문에 mycom.py에 정의됭 있는 모듈을 사용할 수있음
# import mycom
# mycom.price(3) #3명이서 영화보러 갔을 때 가격
# mycom.price_morning(4)
# mycom.price_soldier(1)

# import mycom as mc #너무 길땐 줄여서 이렇게 할 수 있음
# mc.price(4)
# mc.price_morning(1) ; mc.price_soldier(7)

# from mycom import* #이걸 해주면 mycom. 이런걸 안쓰고 그냥 여기서 *은 모든 것을 갖고 온 것이므로
# price(4) ; price_soldier(10)
# from mycom import price_morning #이렇게 하나만 해도 된다
# price_morning(1)
# from mycom import price_soldier as ps#이렇게 빼온 것도 별칭 설정 할 수 있다
# ps(1) 



# import travel.thailand#이렇게 폴더-파일 형식으로 침투한 모듈 불러오기 (클래스는 이렇게 간접적으로만 import할 수 있음 직접적으로 import하면 오류뜸)
# #혹은 이렇게: from travel.thailand import ThailandPackage
# trip_to = travel.thailand.ThailandPackage() #변수에 폴더-파일(모듈)-그 안의 클래스까지 저장한다
# trip_to.detail()#클래스에 저장되어있는 함수를 쓸 수 있게되었다

# from travel import vietnam
# trip__to = vietnam.VietnamPackage()
# trip__to.detail()

# #그런데, 랜덤모듈--#from random import*처럼
# #from travel import* 을 해도, 클래스 등은 참조가 안됨,, 그래서 __init__을 쓰는데,(가서 한번 확인하셈)-그렇게 __all__을 써주고 리스트에 입력을 해놓으면 import*로 한꺼번에 클래스 모듈 불러오기가 가능해짐
# from travel import*
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random)) #이렇게 하면 random이라는 모듈이 어디에 저장되어있는지 알 수 있음 - 위치가 같은 폴더 혹은 파이썬 이하 파일이 모여있는 곳에 있어야 모듈이 상호 작용하기 떄문에 모듈의 위치를 아는 것은 매우 중요함
# print(inspect.getfile(thailand))


# #pip로 package 설치하기--계속 새로운 package가 개발되고 있으므로 다른 사람이 만든 패키지를 받아 사용할 수도 있는것임
# #??????????


# #내장함수
# # language = input('무슨 언어를 좋아하세요?')
# # print('%d는 아주 좋은 언어입니다!'%(language))
# import random #외장함수
# print(dir()) #dir 내장함수 --현재 뭘 쓸 수 있는지 알려주는
# import pickle
# print(dir) #pickle이 추가된 것을 알 수있음
# print(dir(random)) #이렇게 하면 random 안에서 뭘 쓸 수 있는지 나옴

# lst = [1,2,3]
# print(dir(lst)) #이러면 lst에서 쓸 수 있는 메소드들이나옴
# name = '공성식'
# print(dir(name)) #이것 말고도, 구글에서 builtin functions in python 과 같이 검색하면 정보가 나옴 각 사용 예제와 기능 등도 알려주므로 참고할 것







# #외장함수- 직접 import 를 해야하는 것 --구글에서 list of python modules 검색하면 나옴
# import glob #경로 내의 폴더/파일을 조회 (윈도우에서의 dir)
# print(glob.glob('*.py')) #확장자가 .py인 모든 파일에 대해 알려주는 것



# import os #운영체제에서 제공하는 기본 기능/정보 라이선스 정보 등
# print(os.getcwd()) #현재 디렉토리를 표시해달라

# folder = 'simple_dir'
# if os.path.exists(folder): #simple.dir이라는 폴더가 있으면, 
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder)
#     print(folder, '폴더를 삭제하였씁니다,')
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, '폴더를 생성하였습니다.')  #왼쪽 pythonworkplace를 보면 simple_dir이 실제로 생성된 것을 알 수 있고,(원랜 없었음) 또한번하면 삭제되고 하는 시스템임


# print(os.listdir())



import time #시간 관련 함수를 제공
print(time.localtime())

import datetime
print('오늘 날짜는 : ', datetime.date.today(), '입니다')
today = datetime.date.today()
td = datetime.timedelta(days=100)#오늘로부터 100일 뒤를 알려주는 것
print('우리가 만난지 100일은', today+td)

import byme
byme.sign()