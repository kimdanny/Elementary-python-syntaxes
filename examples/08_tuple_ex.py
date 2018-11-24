# 1. 다음의 튜플 자료형을 이용하여 다음과 같은 형식의 출력 결과가 나올수
#    있도록 하시오.
#                 스XX스 메뉴
# 
#    메뉴      tall      grande    venti
# 
#  콜드브루    5,000     5,500     6,000
#  아메리카노  4,100     4,600     5,100
#  카페라떼    4,600     5,100     5,600


item = (
    ('Menu', 'tall', 'grande', 'venti'),
    ('Coldbrew', 5000, 5500, 6000),
    ('Americano', 4100, 4600, 5100),
    ('Caffe Latte', 4600, 5100, 5600),
)

menu = '{:^80}\n'.format('starbucks menu')
for x in item:
    cnt=0
    for y in x:
        if cnt == 0:
            menu += '{:<20}'.format(y)
        else:
            if type(y) is int:
                menu += '{:<20,}'.format(y)
            else:
                menu += '{:<20}'.format(y)
        cnt += 1
    else:
        menu += '\n'
print(menu)

#1-1 (alternative)

item = (
    ('Menu', 'tall', 'grande', 'venti'),
    ('Coldbrew', 5000, 5500, 6000),
    ('Americano', 4100, 4600, 5100),
    ('Caffe Latte', 4600, 5100, 5600),
)

menu = '{:^80}\n'.format('STARBUCKS MENU')
for x in item:
    for idx in range(len(x)):
        if idx == 0:
            menu += '{:^20}'.format(x[idx])
        else:
            menu += '{:<20,}'.format(x[idx]) if type(x[idx]) is int else\
                    '{:<20}'.format(x[idx])
    else:
        menu += '\n'
print(menu)



# 2. 다음의 튜플 자료형을 이용하여 8자리 시리얼 번호를 생성하는 코드를 작성하시오.
# 3. 8자리의 시리얼 번호의 검증을 위한 코드를 작성하시오.
#    검증 조건은 각각의 튜플 요소에 존재하는 문자로만 만들어 있는지 검사를 하여
#    tup_serial[0]의 요소중 일부와 tup_serial[1]의 요소중 일부가 존재하는
#    시리얼 번호는 잘못된 시리얼 번호로 판별할 수 있도록 하시오.
#    예)
#        검증 통과 -> GIK4A0CY
#        검증 에러 -> A5MQ6N2H

tup_serial = (
    ('A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y',
     '0', '2', '4', '5', '8'),
    ('B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z',
     '1', '3', '6', '7', '9'),
)

#2-1
from random import randint
for x in tup_serial:
    serial = ''
    for y in range(8):
        serial += x[randint(0, len(x)-1)]
    else:
        print(serial)


#2-2
tup_serial = (
    ('A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y',
     '0', '2', '4', '5', '8'),
    ('B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z',
     '1', '3', '6', '7', '9'),
)

from random import randint
serial = ''
for x in range(1):
    for y in range(8):
        serial += tup_serial[randint(0, 1)][randint(0, 17)]
    else:
        serial += ' '
else:
    print(serial)


#2-3
tup_serial = (
    ('A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y',
     '0', '2', '4', '5', '8'),
    ('B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z',
     '1', '3', '6', '7', '9'),
)

from random import randint
serial = ''
for x in range(10):
    idx = randint(0, 1)
    for y in range(8):
        l = len(tup_serial[idx])
        serial += tup_serial[idx][randint(0, l-1)]
    else:
        serial += '\n'
else:
    print(serial)


#3.

tup_serial = (
    ('A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y',
     '0', '2', '4', '5', '8'),
    ('B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z',
     '1', '3', '6', '7', '9'),
)
# VVPTNH9V -> OK
# HZPVRRD1 -> OK
# Z7LD37BF -> OK
# C2MH2K0K -> Error
chk_serial = 'Z7LD37B9'
for x in tup_serial:
    if chk_serial[0] in x:
        for c in chk_serial:
            if c not in x:
                print('비정상 시리얼 번호 입니다.')
                break
        else:
            print('정상 시리얼 번호 입니다.')


