#user interface

value = input('put any value')
print('you have put: ', value)          #input으로 사용자로부터 받은 값은 모두 string으로 처리된다

#1
num1 = int(input('put any integer'))
num2 = int(input('put any integer'))
print(num1, '+', num2, '=', num1+num2)

#2. next year age
name = input('what is your name?')
age = int(input('how old are you?'))
print('next year', name, 'will be a', age+1 ,'-year-old man')

#3. with format
age = input('age: ')
name = input('name: ')
print('{}\'s age is {} '.format(name, age))

#4. total, average score calculator
python = int(input('what is your python score'))
clang = int(input('what is your c language score'))
java  = int(input('what is your java score'))
tot = sum([python, clang, java])
avg = round(tot / 3, 2)
print('total score is', tot, 'your average score is', avg)

#5. BMI calculator with input and if elif else
name = input('name: ')
height = input('height: ')
weight = float(input('weight: '))

stdwt = (float(height)-100)*0.9
BMI = (float(height)/stdwt)*100

print(name,'\'s', 'standard weight is', round(stdwt, 2)\
     , 'kg'\
     )


if weight > float(stdwt) :
    print('so you are fukin overweight. stop eating')

elif weight==float(stdwt) :
    print('so you are normal')

else:
    print('so you are skinny. you gotta lift bro')

print(
    'and your BMI is', round(BMI, 2), '%'\
)


