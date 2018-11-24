#conditional statement
'''
조건식의 결과 (true false) 에 따라 코드의 실행을 제어
사용형식 (syntax)
if condition:
    code1
    code2
elif condition:
    code3
else:
    code4

<Things to beware of>
1. colon (:) at the end
2. indent all statements under if  (usually 4 spaces)
3. same space characters for all indentation
'''

from random import randint
a = randint(0, 100)
if 1<a<=10:
    print(a, '어려')
elif 10<a<=20:
    print(a, 'school life')
elif 20<a<=50:
    print(a, 'hardship')
else:
    print(a, 'elderly')


'''
# if expression (if 식)
if 문을 문장으로 사용하는 것이 아니라 하나의 식으로 만들어서 쓰기 위한 방법
-----값(참) if 조건식 else 값 (거짓)------------
elif 는 없다
'''
from random import randint
print('even number' if randint(1, 10) % 2 ==0 else 'odd number')

a = 'even number' if randint(1, 10) % 2 ==0 else 'odd number'
print(a)


from random import randint
rand = randint(0, 3)
a = 'zero' if rand==0 else 'one' if rand==1 else 'two' if rand==2 else 'three'
print(a)


# 중첩 if 문
score = int(input('put your score: '))
if 0<=score<=100:
    if 76<= score <=100:
        print('your score is A*')
    elif 70<= score <76:
        print('your score is A')
    elif 60<= score <70:
        print('your score is B')
    elif 50<= score <60:
        print('your score is C')
    elif score <50:
        print('your score is F')
else:
    print('invalid score')

