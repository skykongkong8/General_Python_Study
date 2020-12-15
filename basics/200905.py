#표준 입출력
print('python','java',sep=',')
print('python','java')
print('python','java','javascropt',sep='vs')
print('Python', 'Java',end='?')
print('무엇이 재밌을까요')
# print('python','java',file=sys.stdout)#표준출력으로 처리
# print('python','java', file=sys.stderr)#표준 에러로 처리 -겉보기엔 차이가 없지만 나중에쓰임

scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4),sep=',') #줄 정렬하기

#은행 대기 순번표
for number in range(1,21):
    print('대기번호 :'+str(number).zfill(4)) #빈공간0으로 채우기

answer = input('아무 값이나 입력하세요 :')
print('입력하신 값은'+answer+'입니다')
print(type(answer)) #input으로 값을 받으면 숫자값 input을 해도 문자열(str)으로 저장이 된다는 것을 확인.

wine_character = input('어떤 와인을 찾으시나요?')
if wine charprint('')

#다양한 출력 포멧
# 빈자리는 빈 공간으로 두고 오른쪽 정렬을 하괴 총 10자리 공간을 확보하기
print('{0: >10}'.format(500)) #>10 10칸 확보하고 오른쪾 정렬하라는 명령
#양수일 때는 +로 표시, 음수일 떈 -로 표시
print('{0: >+10}'.format(-500))
#왼쪽 정렬하고 지정된빈칸에 _을 채움
print('{0:_<10}'.format(500))
#큰 수가 들어왔을 때 세 자리 마다 콤마
print('{0:,}'.format(5165135135135153135))


print('{0:^<+30}'.format(3251351351351))
#소수점 출력
print('{0:f}'.format(5/3))

#소수점 특정 자리수까지만 표시
print('{0:.2f}'.format(5/3))#소수점 둘째자리에서 반올림해달라는 의미로 해석

from random import*
X=randint(1,4)
print(X)