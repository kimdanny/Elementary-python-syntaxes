#python data types
'''
boolean(true false), integer, float(real number), string("", ''), (tuple), [list], {dict}
'''

print(type(hex(100)))       # string
print(type(10))             #integer
print(type('10'))           #string
print(type(1.2))            #float
print(type(True))              #bool
print(type(False))              #bool
print(type((1, 2)))             #tuple
print(type([1, 2]))             #list
print(type({1, 2}))                 #set
print(type({'a' : 1, 'b' : 2}))         #dict

a=10
b=[1, 2]
print(type(a), type(b))

'''
변수이름 작명 규칙
1. 알파벳, 한글, 숫자, _ 를 사용한다
2. 알파벳은 대소문자 구분한다
3. 숫자로 시작하는 변수 이름을 사용할 수 없다 (1a 2a 는 안됨. a1 a2 는 됨)
4. 공백은 없어야함
5. 파이썬 예약어는 사용할 수 없다 (if, for, while, True, False, break, continue, .....)
'''
