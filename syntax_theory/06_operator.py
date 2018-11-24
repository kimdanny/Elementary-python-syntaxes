#산술 연산자
'''
+   -   *   /       사칙연산
// 나눈 몫 만 구한다
%  나눈 나머지만 구한다 -> 특정 값에 대한 배수를 구할 때 사용
** 거듭제곱
'''
print('10+10= {}'.format(10+10))
print('30-10= {}'.format(30-10))
print('30*10= {}'.format(30*10))
print('30/10= {}'.format(30/10))
print('30//10= {}'.format(30//10))
print('30%10= {}'.format(30%10))
print('5**3= {}'.format(5**3))

#비교 연산자
'''
==  !=  >   <   >=  <=
print true or false
'''
print(100==100, 10==4)
print(10 != 10, 3 != 4)
print(2<3, 2>3)
print(2<=2, 3>=3)

#논리 연산자
'''
and     only and only if    (both are true)
or      at least one is true
not     negation
'''
a = (10==10)
b = (10==12)
print(a or b)
print(a and b)
print(a and not b)
print(1 and 1, 1 and 0, 0 and 0)
print(1 or 1, 1 or 0, 0 or 0)

#식별 연산자
'''
is          같으면 true
is not      같으면 false
'''
print(a is a)
print(type(1) is int)
print(type('1') is str)

#멤버 연산자
'''
in          왼쪽 값이 오른쪽에 존재하는가
not in      왼쪽 값이 오른쪽에 존재하지 않는가
멤버는 튜플 리스트 사전 문자열과 같은 집합 형태의 자료형을 이용한다
'''
print(1 in (2, 3, 4, 5), 1 in (1, 2, 5, 8))
print(1 not in (2, 3, 4, 5), 1 not in (1, 2, 5, 8))

#비트 연산자
'''
&       and bit
|       or bit
^       xor bit
<<      왼쪽 피연산자 값을 오른쪽 피연산자 bit 수만큼 왼쪽으로 이동
>>      왼쪽 피연산자 값을 오른쪽 피연산자 bit 수만큼 오른쪽으로 이동
'''
print(bin(0b0 & 0b0), bin(0b1 & 0b0), bin(0b0 & 0b1), bin(0b1 & 0b1))
print(bin(0b0 | 0b0), bin(0b1 | 0b0), bin(0b0 | 0b1), bin(0b1 | 0b1))
print(bin(0b0 ^ 0b0), bin(0b1 ^ 0b0), bin(0b0 ^ 0b1), bin(0b1 ^ 0b1))
print(bin(0b1111<<2))
print(bin(0b1111>>2))

#복합 할당(=) 연산자
'''
+=      왼쪽 변수의 값에 오른쪽 피연산자의 값을 더하고 왼쪽 변수에 할당
-=                                           빼고      
*=                                           곱하고
/=                                           나누고
//=                                          나눈 몫을
%=                                           나눈 나머지를
**=                                          거듭제곱한 값을
'''
a = 10
a += 2 # a = a + 2
print(a)





num1, num2, num3 = 5, 15, 27
print(num2 - num3)
print(num2*5)
print(num1**2)
print(num3/num1)
print(num2/num1)

print( 7>8 )
print( 5<2 )
print( 6%3>2 )
print( 5+5 != 2*5 )
print( True ==1 )
print( 1== '1' )
print( 10 // 3 == 10%3 )
print( 15 %4 in (0, 1, 2) )
