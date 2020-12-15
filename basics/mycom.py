def add(a,b):
    return a+b
def sub(a,b):
    return a-b

PI = 3.14159262457788
class Circle:
    def com1(self, r):
        return PI*(r**2)
    def com2(self, r):
        return 2*PI*r
def com3(a,b):
    return 2*a*b

#티켓 가격 모듈
def price(people):
    print('%d명 가격은 %d원 입니다.'%(people, people * 10000))
def price_morning(people):
    print('조조할인 %d명 가격은 %d원 입니다.'%(people, people * 6000))
def price_soldier(people):
    print('%d명 가격은 %d원 입니다.'%(people, people * 4000))


