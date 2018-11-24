'''
반복문
for : 일정 횟수 또는 한정된 범위 안에서 특정 코드를 반복 실행하기 위해 사용
while : 지정된 조건안에서 특정 코드를 반복 실행하기 위해 사용

일정 횟수를 지정하여 반복
range() 내장함수를 사용하여 일정 횟수를 지정할 수 있다
range(종료값)      0~종료값 이전까지 반복
range(시작값, 종료값)          시작~종료값 이전까지 반복
range(시작, 종료, 증감값)      종료값이전까지 증감시키며 

사용 형식
for 변수명 in range(종료값):
실행코드1
'''

for x in range(5):              #0, 1, 2, 3, 4
    print('{} 번째 반복'.format(x))

for x in range(2, 5):           #2, 3, 4
    print('{} 번째 반복'.format(x))


for x in range(2, 10, 2):       #2, 4, 6, 8
    print('{} 번째 반복'.format(x))


#한정 범위 만큼 반복
#범위 설정은 (튜플), 리스트, 사전, 문자열과같은 집합형태의 자료형을 사용

s= '123456'
for x in s:
    print(x)

t = (1, 2, 3, 'a', 'b')
for x in t:
    print(x)



'''
for..........else 문
syntax:

for x in range(10):
    반복 실행 코드
else:
    반복문이 정상적으로 종료된 후 실행 할 코드


break 문: 반복을 강제로 종료 시키기 위해 사용하는 문
'''

for x in range(3):
    print(x)
else:
    print('정상종료')


for x in range(3):
    print(x)
    break
else:
    print('정상종료')


'''
중첩 for문
syntax:
for x in range(5):
    for y in range(3):
        recursive code

x           y
--------------
0           0
            1
            2
1           0
            1
            2
2           0
            1
            2
3           0
            1
            2
4           0
            1
            2
5           0
            1
            2
'''
#구구단
for x in range(9):
    for y in range(9):
        print('{}X{}={}'.format(x+1, y+1, (x+1)*(y+1)))







