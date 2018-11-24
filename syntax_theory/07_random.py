from random import random
a = random()        #랜덤 함수는 0.0 ~ 1.0 미만의 임의의 값을 하나 생성한다
print(a)

a = random()*10     #0.0 ~ 10.0 미만의 임의의 값
print(a)

from random import randint
a = randint(1, 10)      #1 ~ 10까지(10포함) 임의의 값 생성
print(a)


from random import randrange
a = randrange(1, 10)        #1~10 미만의 임의의 값 생성
print(a)

a = randrange(2, 101, 2)        #2~101미만의 짝수 값 임의 생성
print(a)



#1
from random import randint
a = randint(1, 100)
print(a)

#2
from random import randrange
a = int(randrange(50, 100))

if a % 2 == 0:
    print('true')

else :
    print('false')


#3
from random import random
a = random()*100
b = random()*100

if a-b>0:
    print('true')
else:
    print('false')

#4
from random import randint
a = randint(50, 99)
print('random value : {} -> {}'.format(a, a % 2 == 0))

#5
from random import randint
a = randint(1, 100)
b = randint(1, 100)
print('{} > {} -> {}'.format(a, b, a>b))



#임의의 알파벳 문자 생성 (ascii code)
#chr(arg1) : 아스키 코드 정수 값을 사용하여 아스키코드 문자로 변환
#ord(arg2) : 아스키 코드 문자를 사용하여 아스키 코드 정수값으로 변환
from random import randint
print(chr(65), ord('A'))
print(chr(randint(65, 90)))
print(chr(randint(97, 122)))

#6 임의의 문자 하나를 생성하고 해당 문자가 다음의 범위에 속하는지 구분하는 코드
#범위= I~P

from random import randint
a = chr(randint(65, 90))
result = ord('I') <= ord(a) <= ord('P')

#result = 'I' <= a <= 'P'
#result = a in ('I', 'J', 'K', 'L', 'M', 'N', 'O', 'P')

print('{} -> {}'.format(a, result))



