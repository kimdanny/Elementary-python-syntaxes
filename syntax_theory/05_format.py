'''
format : 터미널에 출력하는 출력물에 대한 양식을 쉽게 만들어 줄 수 있는 기능
c style     python style
%s          {}              문자열
%d          {}              정수
%f          {}              실수

            {:b}            표현식없는 2진수
%o          {:o}            표현식없는 8진수
%x          {:x}            표현식없는 16진수
%X          {:X}            표현식없는 16진수

%.nf        {:.nf}          소수점 n 자리수까지 실수 출력

%nd         {:n}            n 문자열 자릿수
%ns         {:n}            n 문자열 자릿수
%n.mf       {:n.mf}         n 문자열 자릿수, m 소수점 자릿수

%10d        {:>10}          오른정렬
%-10d       {:<10}          왼정렬
            {:^10}          가운데정렬

%010d       {:010d}         숫자 0 으로 여백 채우기

            {:,}            큰 숫자에 쉼표넣기


'''
cstyle = '%s, %d, %f' % ('string', 100, 100.123)
print(cstyle)

pythonstyle = '{} {} {}'.format('string', 100, 12.24)
print(pythonstyle)

c = '%o %x %X' % (10, 10, 10)
print(c)

p = '{:b} {:o} {:x} {:X}'.format(10, 10, 10, 10)
print(p)

c =  '%.1f %.2f %.3f' % (1.123, 1.123, 1.123)
print(c)

p = '{:.1f} {:.2f} {:.3f}'.format(1.123, 1.123, 1.123)
print(p)

#C :  모두 오른쪽 정렬
c = '%10d %10s %10.2f' % (100, 'len', 100.23)
print(c)
#파이썬 : 문자열은 왼쪽 정렬, 정수실수는 오른쪽 정렬 (엑셀 처럼)
p = '{:10} {:10} {:10.2f}'.format(100, 'len', 100.123)
print(p)

c = '%10d\n%-10d' % (100, 100)
print(c)

p = '{:>10}\n{:<10}\n{:^10}'.format(100, 100, 100)
print(p)

c = '%010d' % (10)
print (c)

p = '{:010}'.format(10)
print(p)

p = '{:-<10}\n {:->10}\n {:-^10}'.format(10, 10, 10)
print(p)

p = '{:,}'.format(1000000000000)
print(p)



print(
   '{:<10,}'.format(85000)\
)


x, y, z = 10, 20, 30
s='{1:.2f} {0:} {2:}'.format(x, y, z)
print(s)

x, y = 10, 20
s='{} {} {name}'.format(x, y, name='danny')
print(s)


x = (1, 2, 3)
s= '{} {} {}'.format(*x) #unpacking
print(s)

x = {'a':1, 'b':2, 'c':3}
s='{a} {b} {c}'.format(**x) #unpacking
print(s)

def func(x, y, z):
    return x+y+z
x=(1, 2, 3)
print(func(*x))


#f-string
x, y, z = 1.12, 2, 3
s=f'{x:.4f} {y} {z}'
print(s)



