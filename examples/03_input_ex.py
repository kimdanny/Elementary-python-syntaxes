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
    'and', name, '\'s BMI is', round(BMI, 2), '%'\
)
