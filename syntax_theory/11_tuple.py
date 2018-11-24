'''
Tuple(튜플) 자료형
여러 자료형을 집합 형태로 담아서 관리 할 수 있게 한다.

특징
    1. Sequence Type : 초기에 생성된 데이터의 순서를 유지하고
                       순서 번호(Index Number)에 의해 접근 가능
    2. Iterable Type : 반복 가능 자료형으로 for 반복문에 의해 사용
                       할 수 있는 자료형
    3. Immutation Type : 변경 불가 자료형, 튜플 자료형의 요소를
                         추가/수정/삭제 할 수 없다.

생성 방법
    - 소괄호를 사용하여 소괄호 안에 자료(요소)를 담는다.
    - 각각의 자료(요소)를 구분하기 위해 ,(쉼표)를 사용한다.
    - 리스트, 사전, 문자열 자료형을 이용하여 튜플 자료형으로 변환 할 수 있다.
    - 튜플 자료형을 생성할 때 소괄호를 생략하면서 생성할 수 있다 (packing)

'''

t =(1, 2, 3, 'a', 'b', 'c')
print(t, type(t))

t = tuple('abcd')
print(t, type(t))

#packing
t = 1, 2, 3, 'a', 'b', 'c'
print(t, type(t))

t = (1,)
print(t, type(t))

'''
<indexing>
    튜플자료의 특정 요소 하나에 접근하기 위한 방법
    index 번호를 통해서 특정 요소에 접근 할 수 있다
    index 번호는 0번 부터 시작한다.
    index 번호는 음수 값으로도 사용 가능하다 (역순으로 접근)
    튜플 자료 뒤에 대괄호[]를 사용하여 접근하며 대괄호 안에 index 번호를 넣는다

'''
t = (1, 2, 3, 'a', 'b', 'c')
print(t[1], t[0], t[-1], t[-2])

'''
<slicing>
    튜플 자료의 특정요소들에 접근하기 위한 방법
    index 번호를 통해서 특정 요소들에 접근 할 수 있댜
    index 번호는 시작번호, 끝 번호 형태로 사용해야 한다
        끝번호의 경우 항상 끝번호의 이전 까지만 접근 한다
    튜플자료의 뒤에 [] 대괄호를 사용하고 대괄호 안에는 시작번호:끝번호 형태로 사용
    
    시작번호와 끝번호를 생략할 수 있다. 시작번호를 생략하면 index 번호는 0,
    끝번호를 생략하면 index 번호는 가장 마지막 요소에 접근 할 수 있는 번호롤 쓰인다.

    [시작번호:끝번호:step] 형태 사용가능

'''

t = (1, 2, 3, 'a', 'b', 'c')
print(t[1:3], t[3:6])           
print(t[:3], t[4:], t[:])       #생략가능    
print(t[1::2], t[::2])          #step
print(t[-5:-2], t[-2:-5:-1])

k = 'qwertyuiopasdfghjklzxcvbnm'
k = tuple(k)

#1. indexing을 이용하여 'Hello' 문자열을 출력하시오
s= k[15] + k[2] + k[18] + k[18] + k[8]
print(s)

#2. splicing 을 이용하여 'adgjl' 문자열을 출력하시오
print(k[10:19:2])

s = k[10:19:2]
s = s[0] + s[1] + s[2] + s[3] + s[4]
print(s)

s = k[10:19:2]
s1 = ''
for x in s:
    s1 += x
print(s1)

#3. 반복문을 이용한 튜플 사용
t = (1, 2, 3, 'a', 'b', 'c')
for x in t:
    print(x)

for x in range(len(t)):
    print(t[x])


t = (1, 2)
a, b = t[0], t[1]
print(a, b)

t = (2, 3)
a, b = t    #unpacking
print(a, b)

#주의사항
# unpacking 을 위한 변수의 수와 튜플 요소의 수가 일치해야한다
# Error
# t = (1, 2, 3)
# a, b = t
# print(a, b)

# Error
# t = (1, 2, 3)
# a, b, c, d = t
# print(a, b, c, d)

#n 차 튜플
# 튜플 자료형의 요소로 튜플 자료형이 반복적으로 사용하는 형태

# 2차 튜플
t = ((1, 2), (3, 4), (5, 6))
print(t[0], t[2])
print(t[0][1], t[2][0])
for x in t:
    for y in x:
        print(y, end=' ')



# 3차 튜플
t = (((1, 2), (3, 4)), ((5, 6), (7, 8)), ((9, 10), (11, 12)))

# 보기 편한 형태
# t = (
#         (
#             (1, 2), (3, 4)
#         ),
#         (
#             (5, 6), (7, 8)
#         ),
#         (
#             (9, 10), (11, 12)
#         )
#     )


print(t[0], t[2])
print(t[0][1], t[2][0])
print(t[0][1][0], t[2][0][1])
for x in t:
    for y in x:
        for z in y:
            print(z, end=' ')


# 튜플 함수
# count(value)
#     value로 지정된 값이 튜플 요소로 몇개 존재하는지 알려주는 함수
t = (1, 2, 3, 4, 2, 1, 3, 1)
count = t.count(1)
print(count)

# index(value[, start_index])
#     value로 지정된 값이 튜플의 몇번 Index에 존재하는지 알려주는 함수
#     옵션으로 start_index를 지정하면, 해당 start_index 부터 value를 찾는다.
t = (1, 2, 3, 4, 2, 1, 3, 1)
index = t.index(1)
print(index)
index = t.index(1, 1)
print(index)
index = t.index(1, 6)
print(index)







