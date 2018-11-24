# 사전 자료형 활용

# 메뉴판
# {'메뉴명': 가격, ....}

#사전을 이용
menu = input('메뉴 입력 : ')
menu_board = {
    '아메리카노': 3000, '카페모카': 3500, '카페라떼': 3500,
}
print(menu_board[menu])

#list 를 이용하면 좀 불편
menu_board = [
    ['아메리카노', 3000], ['카페모카', 3500], ['카페라떼', 3500],
]
for values in menu_board:
    if values[0] == menu:
        print(values[1])

# 다음은 Stackoverflow에서 2016년도에 조사한 프로그램 언어 선호도
# 조사 데이터 이다.
program = {
    'JavaScript': 55.4, 'SQL': 49.1, 'Java': 36.3, 'C#': 30.9,
    'PHP': 25.9, 'Python': 24.9, 'C++': 19.4, 'C': 15.5,
    'Node.js': 17.2, 'AngularJS': 17.9, 'Ruby': 8.9,
    'Objective-C': 6.5,
}
# 1. Python 의 선호도는 얼마인가?
x = program['Python']
print('Python의 선호도는 {}% 입니다.'.format(x))

# 2. 가장 높은 선호도를 가지는 프로그램과 가장 낮은 선호도를 가지는 프로그램은
#    무엇인가?
high, low = 0, 100
high_key, low_key = '', ''
for k in program.keys():
    if program[k] > high:
        high, high_key = program[k], k

    if program[k] < low:
        low, low_key = program[k], k
else:
    print('가장 높은 선호도를 가지는 프로그램은 {}% 로 {} 입니다.'\
    .format(high, high_key))
    print('가장 낮은 선호도를 가지는 프로그램은 {}% 로 {} 입니다.'\
    .format(low, low_key))

#같은 코드
'''
high, low = 0, 100
high_key, low_key = '', ''
for k, v in program.items():
    if v > high:
        high, high_key = v, k

    if v < low:
        low, low_key = v, k
else:
    print('가장 높은 선호도를 가지는 프로그램은 {}% 로 {} 입니다.'\
    .format(high, high_key))
    print('가장 낮은 선호도를 가지는 프로그램은 {}% 로 {} 입니다.'\
    .format(low, low_key))
'''
# 3. 위 자료를 선호도 순으로 출력하기 위한 코드를 작성 하시오.(순위도 같이 출력)
order = list(program.items())
for idx in range(len(order)):
    order[idx] = [order[idx][1], order[idx][0]]
else:
    order.sort(reverse=True)
   
for rank in range(len(order)):
    print('{} 순위 -> {}'.format(rank+1, order[rank][1]))