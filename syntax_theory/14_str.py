# string
'''
Sequence type : 초기에 생성된 문자들의 순서를 유지하고 index number에 의해 접근 가능
Iterable type : 반복가능 자료형, for 반복문에 의해 사용할 수 있는 자료형
Immutation type : 변경불가 자료형, 문자열의 특정 문자를 수정/추가/삭제 할 수 없다

'''
a = 'string type'
print(a[0], a[2])           #indexing
print(a[0:5], a[-6:-2])     #slicing

for c in a:
    print(a)

a ='12'
a1, a2 = a          #unpacking
print(a1, a2)

#function
# find(value[, start_index])
#         문자열에서 value에 해당하는 문자열을 찾아서 index 번호를 반환한다
#         start_index를 사용하면 해당위치부터 value 에 해당하는 문자열을 찾아서 index 번호를 반환한다

s = '''
Hello my name is danny. Nice to meet you.
'''
loc = s.find('name')
print(loc)
print(s[10:14])


s='''
    count(value)
    문자열에서 value가 해당하는 문자열의 갯수를 반환한다.
'''
cnt = s.count('value')
print(cnt)
location = s.find('value')
print(location)
print(len(s))

s='''
lower()
    알파벳 문자열을 소문자로 변경해서 반환하는 함수. 기존 문자열이 수정되는 것은 아니다
upper()
    대문자로 ㅇㅇ
'''
print(s.upper())


s='''-------------
strip([character])
    문자열의 앞/뒤 공백을 제거하여 반환하는 함수. 기존문자열이 수정되는 것은 아님
    char를 지정하면 해당문자 제거
    rstrip(), lstrip() 함수로 구분하여 오른쪽 공백 왼쪽 공백 개별적으로 제거하여 반환
-------------'''
print(s)
print(s.strip('-'))
print(s.lstrip('-'))
print(s.rstrip('-'))

s='''
split([value])
    문자열의 공백을 기준으로 문자열을 분리하여 리스트로 반환한다
    value 지정시 value 문자열을 기준으로 분리한다. 
'''
sp = s.split()      # 공백 기준으로 분리
print(sp)
spv = s.split('value')
print(spv)

s='''
replace(old, new)
    기존 문자열에서 old에 해당하는 문자열을 new에 해당하는 문자열로 변경하여 반환하는 함수
'''
change = s.replace('문자열', 'String')
print(change)

s='''
isnumeric()
        문자열이 숫자로만 구성된 문자열인지 확인하는 함수
'''
s1, s2 = '123456', '234gh'
print(s1.isnumeric(), s2.isnumeric())


s='''
isalpha()
        문자열이 숫자 또는 특수문자가 아닌 알파벳 또는 한글인지 확인하는 함수
'''
s1, s2, s3, s4 = '123456', '234gh', 'adf하이', 'asdf!@'
print(s1.isalpha(), s2.isalpha(), s3.isalpha(), s4.isalpha())


s='''
isalnum()
        문자열이 숫자 또는 알파벳 또는 한글로만 구성되어 있는지 확인
'''
s1, s2, s3, s4 = '123456', '234gh', 'adf하이', 'asdf!@'
print(s1.isalnum(), s2.isalnum(), s3.isalnum(), s4.isalnum())




