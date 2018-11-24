# 리스트 생성 문제
# 1. 1 ~ 10 까지의 요소가 있는 리스트를 생성 하시오.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [0] * 10
for x in range(len(a)):
    a[x] = x + 1
print(a)

a = [x for x in range(1, 11)]
print(a)

a = []
for x in range(1, 11):
    a.append(x)
print(a)

# 2. 'A' ~ 'Z' 까지의 요소가 있는 리스트를 생성 하시오.
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(a)
print(a[0])

a = [''] * 26
for x in range(len(a)):
    a[x] = chr(65 + x)
print(a)

chr(65)

a = [chr(65 + x) for x in range(26)]
print(a)

a = []
for x in range(65, 91):
    a.append(chr(x))
print(a)

# 3. 1 ~ 99 까지 임의의 요소 5개가 있는 리스트를 생성 하시오.
from random import randint
a = [randint(1, 99), randint(1, 99), randint(1, 99),
     randint(1, 99), randint(1, 99)
]
print(a)

from random import randint
a = [0] * 5
for x in range(len(a)):
    a[x] = randint(1, 99)
print(a)

from random import randint
a = [randint(1, 99) for x in range(5)]
print(a)

from random import randint
a = []
for x in range(5):
    a.append(randint(1, 99))
print(a)


# 4. 1 ~ 99 까지 임의의 요소 10개가 있는 리스트를 생성 하시오.
#    단, 중복은 없어야 한다.
from random import randint
a = [0] * 10
idx = 0
for x in range(100):
    rand = randint(1, 99)
    if rand not in a:
        a[idx] = rand
        idx = idx + 1
        if idx == 10:
            break
print(a)

from random import randint
a = [0] * 10
idx = 0
while idx < 10:
    rand = randint(1, 99)
    if rand not in a:
        a[idx] = rand
        idx = idx + 1
print(a)

from random import randint
a = []
while len(a) < 10:
    rand = randint(1, 99)
    if rand not in a:
        a.append(rand)
print(a)






# 1~10 까지 임의의 값을 44개 생성후 사용자가 지정한 값이 앞에서 생성한 리스트의 요소들로 몇개 있는지 확인하고 
# 해당요소의 위치값을 전부 반환하는 코드를 작성

from random import randint
a =[]
for x in range(44):
    a.append(randint(1, 10))
print(a)

num = int(input('from 1 to 10 : '))
count = a.count(num)
print('입력값 {}는 {}개 있다'.format(num, count))

cnt = 0
st = 0
while cnt < count:
    print('입력값 {}는 위치값 {}에 있다'.format(num, a.index(num, st)))
    st = a.index(num, st) + 1
    cnt += 1


# 다음은 학생 성적 자료가 들어 있는 리스트 자료형이다.
# 이를 이용해서 학생들의 성적은 A, B, C, D, E, F 등급으로 분리하기 위한
# 코드를 작성하고 각 등급의 학생들만을 따로 관리하기 위한 2차 리스트도 만드시오.
# A : 100 ~ 90, B : 89 ~ 80, C : 79 ~ 70
# D :  69 ~ 60, E : 59 ~ 50, F : 49 ~

grade = [
    ('학생 A', 60), ('학생 B', 55),
    ('학생 C', 98), ('학생 D', 48),
    ('학생 E', 86), ('학생 F', 94),
    ('학생 G', 77), ('학생 H', 69),
    ('학생 I', 67), ('학생 J', 97),
]

a = []
b = []
c = []
d = []
e = []
f = []

print('{:-^70}'.format('학생 성적 관리표'))

for x in range(len(grade)):
    if 90 <= grade[x][1] <= 100:
        a.append(grade[x])

    elif 80 <= grade[x][1] <= 89:
        b.append(grade[x])

    elif 70 <= grade[x][1] <= 79:
        c.append(grade[x])

    elif 60 <= grade[x][1] <= 69:
        d.append(grade[x])

    elif 50 <= grade[x][1] <= 59:
        e.append(grade[x])

    elif 0 <= grade[x][1] <= 49:
        f.append(grade[x])

print('Group A students', a, sep = '\n')
print(sep='\n')
print('Group B students', b, sep = '\n')
print(sep='\n')
print('Group C students', c, sep = '\n')
print(sep='\n')
print('Group D students', d, sep = '\n')
print(sep='\n')
print('Group E students', e, sep = '\n')
print(sep='\n')
print('Group F students', f, sep = '\n')
print(sep='\n')

print('{:-<70}'.format('-'))




#ALTERNATIVE 1 (grade 입력 받아서 거기 속한 학생 보기)

grade = [
    ('학생 A', 60), ('학생 B', 55),
    ('학생 C', 98), ('학생 D', 48),
    ('학생 E', 86), ('학생 F', 94),
    ('학생 G', 77), ('학생 H', 69),
    ('학생 I', 67), ('학생 J', 97),
]

sep_grade = [[], [], [], [], [], []]

for idx in range(len(grade)):
    if 100 >= grade[idx][1] >= 90:
        sep_grade[0].append(grade[idx])

    elif 90 > grade[idx][1] >= 80:
        sep_grade[1].append(grade[idx])

    elif 80 > grade[idx][1] >= 70:
        sep_grade[2].append(grade[idx])

    elif 70 > grade[idx][1] >= 60:
        sep_grade[3].append(grade[idx])

    elif 60 > grade[idx][1] >= 50:
        sep_grade[4].append(grade[idx])

    elif 50 > grade[idx][1]:
        sep_grade[5].append(grade[idx])

c = input('A ~ F : ')
print(sep_grade[ord(c)-65])


#ALTERNATIVE 2 (Excellent code)

grade = [
    ('학생 A', 60), ('학생 B', 55),
    ('학생 C', 98), ('학생 D', 48),
    ('학생 E', 86), ('학생 F', 94),
    ('학생 G', 77), ('학생 H', 69),
    ('학생 I', 67), ('학생 J', 97),
]

sep_grade = [[], [], [], [], [], []]

for idx in range(len(grade)):
    y = grade[idx][1] // 10
    sep_grade[0 if 9-y < 0 else 9-y].append(grade[idx])

c = input('A ~ F : ')
print(sep_grade[ord(c)-65])


