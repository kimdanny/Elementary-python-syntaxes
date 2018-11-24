'''
함수
특정기능을 수행하기 위한 코드들의 집합

함수 종류
1. 내장함수 (built-in function)
2. python 기본 라이브러리 함수 
    (from....import)
    (import....)
3. 사용자 정의 함수
    A. 사용자가 직접 만든 함수
    B. 다른 프로그래머가 만든 함수 - third party library

함수 사용 장점
1. 재사용성 높아진다
2. 유지보수가 쉬워진다

함수 생성
def 함수이름([인자]):
    실행코드1
    실행코드2

함수 사용(호출)
함수이름([인자])
변수명 = 함수이름([인자])

'''
def defa():
    print('call the function')

def defb():
    return 10

b = defa()
print(b)
a = defb()
print(a)

print(type(defa), type(defb))

#
def defc(x):
    print(x*10)
defc(3)


def f(x, y):
    print(x*y)

f(3, 5)


def defC(x):
    '''이 함수의 기능은 ........... 이고, 필요 인자는 다음과 같다.
    argument
        x : 정수형 자료
    '''
    print(x * 10)

help(defC)


#익명함수 (lambda 함수) : 함수의 이름이 없는 함수
# 간단하게 함수를 생성하고 사용하기 위해서 쓰인다
# 일시적, 임시적으로 사용하는 함수

a = lambda x, y: x+y
res = a(10, 20)
print(res)


lst = [('a', 6), ('b', 2), ('c', 9), ('d', 5)]
lst.sort(key=lambda x: x[1])
print(lst)

lst = [('a', 6), ('b', 2), ('c', 9), ('d', 5)]
lst.sort(reverse = True, key=lambda x: x[1])
print(lst)


#

# def sortkey(x):
#     return str(x)
lst = ['a', 6, 'b', 2, 'c', 9, 'd', 5]
lst.sort(key=lambda x: str(x))
# lst.sort(key = sortkey)
print(lst)


lst = [('a', 6), ('b', 2), ('c', 9), ('d', 5)]
mx = max(lst, key = lambda x: x[1])
mn = min(lst, key = lambda x: x[1])
print(mx, mn)


def defd(x, y, z):
    return (x, y, z)

print(defd(y=1, x=2, z=3))

#함수 기본값 인자       기본값 인자는 항상 맨 뒤에 둔다
def deff(x=1, y=2, z=3):
    return (x, y, z)

print(deff(y=3, z=4))


