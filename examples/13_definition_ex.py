# 1. 사칙연산을 위한 함수를 만드시오.
#    함수 이름은 add, sub, div, mul로 하세요.

x = float(input('first number: '))
y = float(input('second number: '))

from random import randint
quest = randint(1, 4)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mul(x, y):
    return x * y

if quest == 1:
    add(x, y)
    quest = randint(1, 4)
elif quest == 2:
    sub(x, y)
    quest = randint(1, 4)
elif quest == 3:
    div(x, y)
    quest = randint(1, 4)
elif quest == 4:
    mul(x, y)
    quest = randint(1, 4)

#
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mul(x, y):
    return x * y

add(10, 2)

# 2. python 내장 함수 중 bin, oct, hex 함수를 모방하여 동일한 기능으로 동작하게
#    만들어 보시오.
a = int(input('put any number: '))
def my_bin(number):
    res = []
    while number > 0 :
        res.append(number % 2)
        number = number // 2
    res.reverse()
    
    binary = '0b'
    for c in res:
        binary += str(c)

    return binary
    
print(my_bin(a))



# 3. 2번에서 만든 함수를 다음과 같은 결과로 나올 수 있도록 수정 하시오.
#    예) mybin(10, True) -> 0b1010
#        mybin(10, False) -> 1010

def my_bin(number, opt):
    binary = ''
    while number > 0 :
        binary += str(number % 2)
        number = number // 2

    if opt == True:
        return '0b' + binary
    else:
        return binary

print(my_bin(10, True))
print(my_bin(10, False))



#3-1
def my_bin(number, opt):
    binary = ''

    while number > 0 :
        binary = str(number % 2) + binary
        number = number // 2
        
        #if 를 한줄 코드로
    return '0b' + binary if opt == True else binary

print(my_bin(10, True))
print(my_bin(10, False))



# 4. 3번에서 만든 함수를 다음과 같은 결과로 나올 수 있도록 수정 하시오.
#    예) my_bin(10) -> 0b1010
#        my_bin(10, False) -> 1010
#        my_hex(10) -> 0xA
#        my_hex(10, False) -> A
#        my_hex(10, False, False) -> a
#        my_hex(10, upper=False) -> 0xa

def my_bin(number, opt=True):
    binary = ''

    while number > 0 :
        binary = str(number % 2) + binary
        number = number // 2

    return '0b' + binary if opt == True else binary

print(my_bin(10))
print(my_bin(10, False))

def my_hex(number, opt=True, upper=True):
    hexa_decimal = ''

    while number > 0 :
        temp = number % 16
        if temp >= 10:
            if upper == True:
                hexa_decimal = chr(55 + temp) + hexa_decimal
            else:
                hexa_decimal = chr(87 + temp) + hexa_decimal
        else:
            hexa_decimal = str(temp) + hexa_decimal

        number = number // 16

    return '0x' + hexa_decimal if opt == True else hexa_decimal

print(my_hex(10, False))        # -> A
print(my_hex(10, False, False)) # -> a
print(my_hex(10, upper=False))  # -> 0xa


#5. 65~90 대문자, 97~122 소문자 
# 시리얼 번호를 생성하는 함수
#문자만 있는 시리얼 번호
#    1. 이 함수는 인자로 시리얼 번호의 길이, 생성 갯수를 사용 한다.
#    2. 시리얼 번호는 기본값으로 8을 사용하며, 최대 24 까지 사용 가능.
#    3. 시리얼 번호의 알파벳은 대문자 또는 소문자를 선택하여 생성 할 수 있게 한다.
#    4. 시리얼 번호 생성에서 중복 허용 및 불가를 선택하여 생성 할 수 있게 한다.
#    5. 생성된 시리얼 번호를 파일로 출력 하는 함수를 따로 만들어서 출력하게 한다.

from random import randint

def makesrl(howmany, upper = True, length=8):
    serial = ''
    while 8<= length <=24:
        if upper == True:
            for x in range(howmany):
                for y in range(length):
                    serial += chr(randint(65, 90))
                else:
                    serial += '\n'
            else:
                return serial

        elif upper == False:
            for x in range(howmany):
                for y in range(length):
                    serial += chr(randint(97, 122))
                else:
                    serial += '\n'
            else:
                return serial
    else:
        print('invalid length')


def srlopen(path, data):
    fw = open(path, mode='w', encoding='utf-8')
    for line in data:
        fw.write(line)
    fw.close()
data = makesrl(5, upper=True, length=24)

srlopen('C:\\python_academy\\function test.txt', data)



#5-1
# 시리얼 번호를 생성하는 함수
#숫자와 문자가 함께있는 시리얼 번호
#    1. 이 함수는 인자로 시리얼 번호의 길이, 생성 갯수를 사용 한다.
#    2. 시리얼 번호는 기본값으로 8을 사용하며, 최대 24 까지 사용 가능.
#    3. 시리얼 번호의 알파벳은 대문자 또는 소문자를 선택하여 생성 할 수 있게 한다.
#    4. 시리얼 번호 생성에서 중복 허용 및 불가를 선택하여 생성 할 수 있게 한다.
#    5. 생성된 시리얼 번호를 파일로 출력 하는 함수를 따로 만들어서 출력하게 한다.

from random import randint
def genSerial(count, length=8, case='upper', overlap=True):
    #length 가 24보다 크면 24로 맞춰줌
    length = 24 if length > 24 else 8 if length < 8 else length
    #upper 면 대문자 lower 면 소문자, 이상한 문자면 대문자
    case = 65 if case == 'upper' else 97 if case == 'lower' else 65
    serial = []
    for x in range(count):
        serial.append('')
        while len(serial[-1]) < length:
            char = str(randint(0, 9)) if randint(0, 2) == 0 else chr(randint(case, case+25))
            #randint가 0이면 숫자붙이고 1, 2면 문자붙인다         #대문자부터 25개, 소문자부터 25개
            serial[-1] += char if overlap == True else char if char not in serial[-1] else ''
            #중복 허용이면 무조건 추가, 불가면 빈문자열 추가
    return serial
def fileOut(path, data):
    fw = open(path, mode='w', encoding='utf8')
    for line in data:
        fw.write(line+'\n')
    fw.close()
data = genSerial(10, 8, case='upper', overlap=False)
fileOut('C:\\python_academy\\function test.txt', data)







