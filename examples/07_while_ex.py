#1. 10~99 까지 while 사용하여 반복 출력
a = 10
while a < 100:
    print(a, end=' ')
    a += 1

#2. 대문자 A ~ Z 까지, 소문자 a ~ z 까지 반복 출력하는 코드 작성 
a, b = 65, 97
while a<91 and b<123:
    print(chr(a), chr(b))
    a+=1
    b+=1

#2-1. 
a = 65
while a <= 122:
    if 65 <=a <=90 or 97<= a <= 122:
        print(chr(a), end=' ')
    a += 1

#2-2. continue 를 활용한 2번문제
code = 64
while code < 122:
    # if 65 <= code <= 90 or 97 <= code <= 122:
    #     print(chr(code), end=' ')
    if 91 <= code <= 96:
        continue
    code = code + 1
    print(chr(code), end=' ')

#3. 100 ~ 199 까지의 누적 합을 구하는 코드를 작성
a = 100
tot = 0
while a < 200:
    for x in range(100, 200):
        tot += a
        a += 1
    else:
        print('100 ~ 199 까지의 누적 합 : {}'.format(tot))


#3-1 much better code
num = 100
tot = 0     # 누적 합 변수
while num <= 199:
    tot = tot + num
    num = num + 1
else:
    print('100 ~ 199 까지의 누적 합 : {}'.format(tot))


# 4. 
# 1 부터 2씩 증가하는 값에 대한 누적 합을 구하되 누적 합이 10000을 넘지 않는
# 선에서 구하고 마지막에 더해진 값도 구하시오.
# 1 + 3 + 5 + 7 + 9 ... x < 10000
 
num = 1
tot = 0
while tot + num < 10000:
    tot += num
    num += 2
else:
    print(tot, num-2)

#4-1. 무한반복 시키다가 조건에서 break. 단 이때는 else 활용을 못한다.
num = 1
tot = 0
while True:
    tot += num
    num += 2
    if tot + num >= 10000:
        print(tot, num-2)
        break



#5. 대문자 A~Z 까지 숫자0~9까지 사용하여 16자리 시리얼 번호 생성 (중복 없어야 한다)
from random import randint
srl = ''
for x in range(9):
    for y in range(16):
        srl += chr(randint(65, 90))
    else:
        srl += '\n'
else:
    print(srl)


#5-1
from random import randint

srlnum = 3 

for x in range(srlnum):
    alp =''
    cnt = 0
    while cnt < 16:
        rand = chr(randint(65, 90))
        if str(rand) not in alp:
            alp += rand
            cnt += 1
    else:
        print(alp)


#5-2 much better code

from random import randint

serial = ''
while len(serial) < 16:
    rand = randint(48, 90)
    if 58 <= rand <= 64:            #58~64까지는 특수문자라서 제외 시키는 코드
        continue
    else:
        if chr(rand) not in serial:
            serial += chr(rand)
else:
    print(serial)



#6. 사칙연산 자동 출제 프로그램
#간단한 사칙연산 문제를 풀 수 있게 문제만들고 정답과 오답을 체크하는 코드
#   1. 더하기, 빼기, 곱하기, 나누기 문제를 임의로 생성 할 수 있게 한다.
#   2. 연산을 위한 값은 1 ~ 99 까지의 범위를 사용 한다.
#   3. 빼기, 나누기 문제의 경우 큰 값에서 작은 값을 빼거나 나누게 한다.
#   4. 나누기 문제의 정답/오답 비교는 소수점 2번째 자리 까지 비교 하도록 한다.
#   5. 출제 문제의 정답을 맞춘 경우 +10 점 추가, 오답인 경우 -7점 추가하여
#      총 점수 50을 넘겨야 종료가 될수 있도록 한다.
#
#   추가 기능
#     A. 연산을 위한 값의 범위를 사용자가 설정 할 수 있도록 한다.
#     B. 프로그램 종료를 위한 점수를 사용자가 설정 할 수 있도록 한다.


from random import randint
a = randint(1, 4)

score = 0
endscore = int(input('goal score: '))

q = int(input('calculation range from: '))
w = int(input('calculation range to: '))


while score < endscore:
    if a == 1:           #addition
        b1 = randint(q, w)
        c1 = randint(q, w)
        if input('{} + {} = ? '.format(b1, c1)) == str(b1+c1):
            print('correct')
            score += 10
            a = randint(1, 4)
        else:
            print('wrong. The answer is ', b1+c1)
            score += -7
            a = randint(1, 4)

    elif a == 2:          #multiplication
        b2 = randint(q, w)
        c2 = randint(q, w)
        if input('{} X {} = ? '.format(b2, c2)) == str(b2*c2):
            print('correct')
            score += 10
            a = randint(1, 4)
        else:
            print('wrong. The answer is ', b2*c2)
            score += -7
            a = randint(1, 4)

    elif a == 3:          #division
        b3 = randint(q, w)
        c3 = randint(q, w)
        d3 = max(b3, c3)
        e3 = min(b3, c3)
        if input('{} / {} = ? (to 2 decimal places)'.format(d3, e3)) == str(round(d3/e3, 2)):
            print('correct')
            score += 10
            a = randint(1, 4)
        else:
            print('wrong. The answer is ', round(d3/e3, 2))
            score += -7
            a = randint(1, 4)

    elif a==4:              #subtraction
        b4 = randint(q, w)
        c4 = randint(q, w)
        d4 = max(b4, c4)
        e4 = min(b4, c4)
        if input('{} - {} = ? '.format(d4, e4)) == str(d4-e4):
            print('correct')
            score += 10
            a = randint(1, 4)
        else:
            print('wrong. The answer is ', d4-e4)
            score += -7
            a = randint(1, 4)
else:
    print('well done. your score is',score , ' GAME FINISHED')










