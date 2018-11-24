'''
while 문
조건에 따라서 특정 코드를 반복하거나 반복을 중단할 때 사용
조건의 결과가 참이면 반복, 거짓이면 반복 중단

syntax

while 조건식:
    반복 실행코드 1


while 조건식:
    코드1
else:
    조건식이 거짓인 경우 실행할 코드2

'''

count =0
while count<10:
    print(count, end=' ')
    count += 1 
else:
    print('conditional statement has become false, count={}'.format(count))



#while 을 이용한 로또번호 중복x

from random import randint

gamecount = 3 #int(input('how many games u wanna play: '))

for x in range(gamecount):
    lott =''
    cnt = 0
    while cnt < 6:
        rand = randint(1, 46)
        if str(rand) not in lott:
            lott += '{:<02} '.format(rand)
            cnt += 1
    else:
        print(lott)


#프로그램을 중단하지 않고 계속 동작하게 만들기 위해서도 사용. 
while True:     #infinite loop
    exit = True if input('wanna end? (yes/no): ') == 'yes' else False
    if exit == True:
        break




