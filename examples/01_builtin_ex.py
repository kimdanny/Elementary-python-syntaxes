
print(max(72, 58, 89, 77, 59, 99, 62, 54, 82))
print(min(72, 58, 89, 77, 59, 99, 62, 54, 82))
print(sum([72, 58, 89, 77, 59, 99, 62, 54, 82]))
print(divmod(652, 99))

print(divmod(sum([72, 58, 89, 77, 59, 99, 62, 54, 82]), max(72, 58, 89, 77, 59, 99, 62, 54, 82)))

print('quotient:', divmod(652, 99)[0], ',', 'remainder:',  divmod(652, 99)[1])          #[0]: 처음, [1]:뒤


a = sum([72, 58, 89, 77, 59, 99, 62, 54, 82])
b = max(72, 58, 89, 77, 59, 99, 62, 54, 82)         # 합과 최대치를 변수화 시킨다

print('quotient:', divmod(a, b)[0], \
         'remainder:',divmod(a, b)[1])              # 줄바꿈 후에 뒤에 \ 를 붙여줘야 연속해서 인식한다, \ 뒤에는 공백이 있으면 안된다.

         

