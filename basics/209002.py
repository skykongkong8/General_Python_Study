#if

nahyun = 'smart'

if nahyun == 'smart':
    print('Indeed she is')
elif nahyun =='dumb':
    print('pitty')
else:
    print('actually I dont care')

# temp = int(input('hows the temperature?'))
# if 30<= temp:
#     print('너무 더워요 나가지 마세요')
# elif 10<= temp and temp < 30:
#     print('weather is fine')
# elif 0<= temp and temp<10:
#     print('take your clothes')
# else:
#     print('too cold to go outside')


#for
# print('waiting : 1')
# print('waiting : 2')
# print('waiting : 3')

for waiting_no in range(1,6):
    print('waitingnumeri : {0}'.format(waiting_no))

starbucks = ['승헌', '민창', '건우']
for customer in starbucks:
    print("{0}, coffee is ready". format(customer))
#reviewing
redwine = ['cabrnet souvignon', 'merlot', 'pino noir',]
for hereitisnotimportant in redwine:
    print('I wanna drink {0}, please'. format(hereitisnotimportant))
for whitewine in range(29,42):
    print('chardonnay', 'souvignon blanc', 'pino grizgio {0} bottles would be fine'.format(whitewine))

# #while
# customer = 'thor'
# index = 5
# while index >= 1:
#     print('{0}, your coffee is ready. {1} times left'.format(customer, index))
#     index -= 1
#     if index ==0:
#         print('your coffee has discarded')

# # client = 'ironman'
# # while True:
# #         print('{0}, your coffee is ready. call{1} index'))

# client = 'hella'
# person = 'unknown'

# while person != client :
#     print("{0}, coffee is ready".format(client))
#     person = input("Como te llamas?")


#continue와 break
absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    if student in no_book:
        print('DETENTION for {0}'.format(student))
        break
    print("{0}, read page 394 for me.".format(student))


#1 2 3 4 를 101 102 1030 등으로 만들고싶음
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

estudiantes = ['iron man', 'thor', 'i am groot']
estudiantes = [len(i) for i in estudiantes]
print(estudiantes)

friends = ['a','b','crocodile']
friends = [k.upper() for k in friends]
print(friends)



from random import* #난수를 써야하니 random을 꺼내옴
cnt = 0 #처음 시작숫자는 0으로 정의
for i in range(1,51): #i를 format에 쓸 수 있도록 정의한 것. 이때 range에 들어가는 것을 for함수를 써야함 그래야 그 기준으로\
    #쭉 나열된다.
    time = randrange(5, 51)#time을 format에 쓸 수 있도록 정의한 것. randrange이므로 for로 자동나열 시킬수없는 경우
    if 5 <=time <=15: #조건 첫번쨰-if문장에는 두번씩 쓰는 것을 기억할것
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time)) #format을 활용한 풀이
        cnt += 1 #그럴 때마다 cnt의 수 증가함을 표시
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print('총 탑승 승객 : {0} 분'.format(cnt)) 
