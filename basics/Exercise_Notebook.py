# # from random import*
# # a= randint(-10000000,10000000)
# # b= randint(-10000000,10000000)
# def solution(a,b):
#     A =abs(a)
#     B =abs(b)
#     C =max(A, B)
#     D =min(A, B)
#     if a == b:
#         return a
#     elif a*b<0 and (a+b)<0:
#         return -1*C*(C+1)/2 + D*(D+1)/2
#     elif a*b<0 and (a+b)>0:
#         return C*(C+1)/2 - D*(D+1)/2
#     elif a*b>0 and (a+b)<0:
#         return -1*C*(C+1)/2 + D*(D+1)/2 - D
#     else:#A>=B>=0 or A<=B<=0:
#         return C*(C+1)/2 - D*(D+1)/2 + D
# print(solution(a,b))



# # stri = '수박'
# string = stri*5000
# def solution(n):
#     return string[0:n]
# n=4
# print(solution(n))



# def solution(s):
#     return int(s)
# s=1234
# print(solution(s))
#다른풀이
# solution = int
# print(solution(1234))



# def solution(x, n):
#     if x>0:
#         return list(range(x, n*x+1, x))
#     elif x<0:
#         reverselist = list(range(n*x,x+1,-1*x))
#         return list(reversed(reverselist))
#     elif x==0:
#         zerolist=[]
#         for i in range(n):
#             zerolist.append(0)
#         return zerolist 
# x=0
# n=5
# print(solution(x, n))
# # reverselist = list(range(0, 5, 1))
# # print(reverselist.reverse())



#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# def solution(arr):
#     Sum = sum(arr)
#     return Sum/len(arr)
# arr = [90, 100, 95]
# print(solution(arr))



# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.
# def solution(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
# num = 3
# print(solution(num))