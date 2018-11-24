#built in function : 파이선에서 기본적으로 사용 가능한 기능
#함수 사용법
'''
function(argument) or 함수이름(arg1, arg2 ....)
인자 (argument) : 함수의 기능이 동작하기 위해서 함수 내부로 전달해야하는 값
'''

print(max(3, 5, 8))     # maximam value
print(min(3, 5, 8))     # minimum value

# using variables
a, b, c = 3, 5, 8
print(max(a, b, c))
print(min(a, b, c))

print(sum([1, 2, 3, 4]))        # argument should be written as a form of either []:tuple or ():list

print(pow(3, 4))                # 3^4

print(divmod(5, 4))             # get quotient and remainder
print('quotient:', divmod(5, 4)[0],',', 'remainder', divmod(5, 4)[1])

print(round(2.3456, 2))         #round up to 2 decimal places
print(round(123, -1))           #round up to -1 place

print(hex(100))                 #16진수
print(oct(23))                  #8진수
print(bin(23))                  #2진수
#2진수: 0b, 8진수: 0o, 16진수: 0x,          진법 변환된 값은 문자열로 처리된다 = string object cannot be interpreted as an integer

print(oct(0x64))                # 16진수를 8진수로 바꾼다
print(bin(0o234))               #8진수를 2진수로 바꾼다
print(bin(100+0x100))

bin(int(hex(100), base=16))         #진법 변환된 값은 문자열로 처리된다. 따라서 bin(hex(100)) 은 에러




