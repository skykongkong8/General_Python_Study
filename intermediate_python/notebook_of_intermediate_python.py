#모듈에 관한 실습 노트

import area
"""같은 폴더 내에 있는 모듈(다른 파이썬 파일) 불러오기"""
# print(area.circle(2)) #함수를 쓸 때는 파일.함수이름 과같이 '.'을 써주어야 합니다
# print(area.sqaure(4))

#하나만 필요하다면:
from area import circle
"""area라는 모듈에서 circle 함수만 가져오기"""
from area import circle, sqaure
"""n개씩 가져오기"""

import area as ar
from area import circle as donggurami
"""이름 바꿔주기"""
# *방식 다가져오는건 지양합시다---

#CF)
A=[[0 for i in range(3)] for i in range(2)]
"""반복문으로 리스트 채우는 법"""
# print(A)

"""Class도 as from import 등 사용해서 자유롭게 이용하면 된다"""


# print(dir()) #네임스페이스를 출력하는 함수 dir()
a=[1,2,3]
b=a
c=a[:]
a[0]=4
# c=a[:]
print(a,b,c)