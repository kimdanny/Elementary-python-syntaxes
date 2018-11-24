#1. 
for x in range(11):
    print(x, end=' ')

#2. 
for x in range(50, 60):
    print(x, end=' ')

#3. for 와 if 같이
for x in range(1, 100):
    if x % 2 == 0:
        print(x, end=' ')

#이것도 가능
for x in range(1, 101):
    print(x if x%2==0 else '', end=' ')


#4. 
for x in range(99, 0, -2):
    print(x, end=' ')

#이것도 가능
for x in range(99, 0, -1):
    if x%2==1:
        print(x, end=' ')


#5.
from random import randint
for x in range(10):
    x = randint(1, 100)
    print(x, end=' ')

#6
from random import randint
for x in range(16):
    x=chr(randint(97, 122))
    print(x, end=' ')

#이것도 가능    s를 반복문 밖에 둬라!
from random import randint
s=''
for x in range(16):
    c=chr(randint(97, 122))
    s += c
print(s)                    #print 를 안에 두면 반복하는 도중 계속 프린트       밖에 둬야 한번에 16자리 출력

'''
<debugging>

s           x           c
------------------------------
''          0           'a'
'a'         1           'g'
'ag'        2           'b'
'agb'       3           't'
'agbt'
            .
            .
            .
            .
            .
            .
'''



#7
from random import randint
tot=0

for x in range(5):
    n= randint(1, 100)
    tot += n
    print(n, end=' ')
print('총합은', tot)




#input 을 활용한 멈춰가며 보는 디버깅코드
from random import randint
tot=0

for x in range(5):
    input(x)
    n= randint(1, 100)
    #input(x)
    tot += n
    input(x)
    print(n, end=' ')
print('총합은', tot)


#8.

# 1   2   3   4   5   6   7   8
# 9   10  11  12  13  14  15  16
# 17  18  19  20  21  22  23  24
# 25  26  27  28  29  30  31  32

#8-1. (my code)
for x in range(8):
    print(x+1, end='  ')
print(sep='\n')
for a in range(9, 17):
    print(a, end=' ')
print(sep='\n')
for b in range(17, 25):
    print(b, end=' ')
print(sep='\n')
for c in range(25, 33):
    print(c, end=' ')

#8-2 (much better code)
for x in range(32):
    if (x+1) % 8 ==0:
        print('{:<4}'.format(x+1))
    else:
        print('{:<4}'.format(x+1), end=' ')


#8-3 (much better code)
s=''
for x in range(1, 33):
    if x%8 == 0:
        s += '{:<4}\n'.format(x)
    else:
        s += '{:<4}'.format(x)
print(s)



#9. 

# a   b   c   d   e   f   g   h
# i   j   k   l   m   n   o   p
# q   r   s   t   u   v   w   x
# y   z

#9-1. (my code)
c = 97
for x in range(8):
    x = chr(c)
    c = c + 1
    print(x, end= ' ')
print(sep='\n')

a = 97+8
for x in range(8):
    x = chr(a)
    a = a + 1
    print(x, end=' ')
print(sep='\n')

b = 97+16
for x in range(8):
    x = chr(b)
    b = b + 1
    print(x, end=' ')
print(sep='\n')

d = 97+24
for x in range(2):
    x = chr(d)
    d = d + 1
    print(x, end=' ')


#9-2 (much better code)
for x in range(26):
    if (x+1) % 8 == 0:
        print('{:<4}'.format(chr(x+97)))            #개행을 위한 코드 if print else print 는 자동으로 개행됨
    else:
        print('{:<4}'.format(chr(x+97)), end=' ')



#9-3 (much better code)
s=''                            #무의 상태는 ''로 표현
for x in range(26):
    if  (x+1) % 8 == 0:
        s += '{:<4}\n'.format(chr(x+97))
    else:
        s += '{:<4}'.format(chr(x+97))
print(s)



#10. 

# 1   2   3   4   5   6   7   8   9   A
# B   C   D   E   F   10  11  12  13  14
# 15  16  17  18  19  1A  1B  1C  1D  1E
# 1F  20  21  22  23  24  25  26  27  28
# 29  2A  2B  2C  2D  2E  2F


s=''
for x in range(1, 0x30):
    if x % 10 ==0:
        s += '{:<4X}\n'.format(x)
    else:
        s += '{:<4X}'.format(x)
else:
    print(s)


#중첩 반복문 문제
#1. 알파벳 대문자로 구성된 8자리의 시리얼 번호 5개를 생성하는 코드 65-90

from random import randint

serial = ''
for x in range(5):
    for y in range(8):
        serial += chr(randint(65, 90))
    else:
        serial += '\n'
else:
    print(serial)


#2. 로또 문제 (중복 고려 안함)

from random import randint

gamecount = int(input('how many games u wanna play: '))

for x in range(gamecount):
    for y in range(6):
        lott = randint(1, 46)
        print(lott, end='  ')
    else:
        print(sep='\n')         #  <- 이거는 개행의 목적으로 쓰임  그냥 print() 만 해도 개행되긴함

#2-1. 중복 고려함
from random import randint

gamecount = 3 #int(input('how many games u wanna play: '))

for x in range(gamecount):
    lott =''
    cnt = 0
    for y in range(50):
        rand = randint(1, 46)
        if str(rand) not in lott:
            lott += '{:<02} '.format(rand)
            cnt += 1
            if cnt == 6:
                break
    print(lott)

'''
#질문
#1. 왜 range(50) 인가:
    중복을 피하는 코드를 작성하려고 count 라는 변수를 추가했다.
    이 상황에서 range(6)이라고 한다면 중복이 생겼을 시에 count 수가 다 채워져서 
    6개 미만의 정수가 출력이 되는 상황이 생긴다
    이를 방지하려고 확률적으로 50번정도 돌리면 거의 6개의 정수를 다 뽑아낼수있다.
    더 방지하고 싶으면 10000 으로 하던가 ㅋㅋ ㅇㅋ?

#2. 왜 출력값에 46 이상의 값이 나오는가
ex.
30 80 28 39 31 14
36 46 43 15 27 38
11 41 34 17 60 50

'''




