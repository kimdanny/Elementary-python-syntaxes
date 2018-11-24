# input() 함수를 단 2번만 사용하여 이름과 체중, 키를 입력 받아 동작하는
# 비만도 계산 프로그램을 만드시오.

name = input('name: ')
# height = input('height: ')
# weight = float(input('weight: '))

bio = input('your height, weight (use comma between two values): ')
# height, weight = input('blabla').split(',') 도 가능
sp = bio.split(',')
height, weight = float(sp[0]), float(sp[1])
# userin = input('키(cm), 체중(kg) : ').split(',')
# 키, 체중 = map(float, userin) 도 가능

stdwt = (float(height)-100)*0.9
BMI = (float(height)/stdwt)*100

print(name,'\'s', 'standard weight is', round(stdwt, 2)\
     , 'kg'\
     )


if weight > float(stdwt) :
    print('so you are fukin overweight. stop eating')

elif weight == float(stdwt) :
    print('so you are normal')

else:
    print('so you are skinny. you gotta lift bro')


print(
    'and', name, '\'s BMI is', round(BMI, 2), '%'\
)



# 다음의 문자열을 다음의 형식으로 변환 하는 코드를 작성하시오.
csv = 'JavaScript,62.50%|SQL,51.20%|Java,39.70%\
|C#,34.10%|Python,32.00%|PHP,28.10%|C++,22.30%|C,19.00%|TypeScript,9.50%\
|Ruby,9.10%|Swift,6.50%|Objective-C,6.40%|VB.NET,6.20%|Assembly,5.00%\
|R,4.50%|Perl,4.30%|VBA,4.30%|Matlab,4.30%|Go,4.30%|Scala,3.60%\
|Groovy,3.30%|CoffeeScript,3.30%|Visual Basic 6,2.90%|Lua,2.80%|Haskell,1.80%'

# 1번 형식  list
# data = [
#     ('JavaScript', 62.5), ('SQL', 51.2), ('Java', 39.7),
#     ('C#', 34.1), ...
# ]
temp = csv.split('|')
data = []
for s in temp:
    d1, d2 = s.split(',')
    data.append((d1, float(d2[:-1])))       #튜플 자료형으로 추가
print(data)

#   d2[0:-1] 는 %가 빠진 그냥 숫자만이다


# 2번 형식  dictionary
# data = {
#     'JavaScript': 62.5, 'SQL': 51.2, 'Java': 39.7,
#     'C#', 34.1, ...
# }
samp = csv.split('|')
data = {}
for s in samp:
    a1, a2 = s.split(',')
    data.setdefault(a1, float(a2[:-1]))
print(data)

