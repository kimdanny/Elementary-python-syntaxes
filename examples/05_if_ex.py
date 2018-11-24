#1

from random import randint
a = randint(1, 100)
if a % 2 == 0:
    print(a, 'is an even number')
else:
    print(a, 'is an odd number')

#2 큰 값 나누기 작은 값
from random import randint
a = randint(1, 100)
b = randint(1, 100)
c = max(a, b) 
d = min(a, b)

print(c,'/', d, '=', round(c/d, 3))

#2 - 다른방법   a, b = b, a 를 사용
from random import randint
a = randint(1, 100)
b = randint(1, 100)
if a<b:
    a, b = b, a
    print('{}/{} = {}'.format(a, b, round(a/b, 3)))
else:
    print('{}/{} = {}'.format(a, b, round(a/b, 3)))

#3짝짝 아니면 홀홀 이면 곱하고      홀짝짝홀이면 더하고
from random import randint
a = randint(1, 100)
b = randint(1, 100)

if (a%2==0 and b%2 == 0) or (a%2==1 and b%2 == 1):                      #if (a%2)+(b%2) in (0, 2) 도 신박한 방법
    print(a, b,'=>',a*b)
else:
    print(a, b,'=>',a+b)


#4. BMI calculator with input and if elif else
name = input('name: ')
height = input('height: ')
weight = float(input('weight: '))

stdwt = (float(height)-100)*0.9
BMI = (float(height)/stdwt)*100

print(name,'\'s', 'standard weight is', round(stdwt, 2)\
     , 'kg'\
     )

if weight > float(stdwt) :
    print('so you are fukin overweight. stop eating')

elif weight==float(stdwt) :
    print('so you are normal')

else:
    print('so you are skinny. you gotta lift bro')


print(
    'and', name, '\'s BMI is', round(BMI, 2), '%'\
)

#5. 2018 7월 요일 출력

date = int(input('what date is today?'))  

if (31<date) or (date<=0):
    print('not a valid date')
elif date%7 == 1:
    print(date,'is sunday')
elif date%7 == 2:
    print(date, 'is monday')
elif date%7 == 3:
    print(date, 'is tuesday')
elif date%7 == 4:
    print(date, 'is wednesday')
elif date%7 == 5:
    print(date, 'is thursday')
elif date%7 == 6:
    print(date, 'is friday')
elif date%7 == 0:
    print(date, 'is saturday')

# doesnt have to end with 'else'

