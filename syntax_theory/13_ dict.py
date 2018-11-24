#Dictionary data type
# 특징
#     1. Mapping Type : Sequence Type과 다르게 Index Number를 사용하지 않고
#                       Key를 사용하여 Index 처럼 활용을 하게 된다.
#     2. Iterable Type : 반복 가능 자료형으로 for 반복문에 의해 사용 할 수 있는
#                        자료형
#     3. Mutation Type : 변경 가능 자료형, 사전 자료의 요소를 추가/수정/삭제
#                        할 수 있다.

# 생성 방법
#     - {}(중괄호)를 사용하여 생성 한다.
#     - 사전형은 항상 Key와 Value의 쌍으로 생성해야 한다.
#       {key1:value1, key2:value2, ....}
#     - 튜플, 리스트 자료형을 사전형으로 변환 할 수 있다.
#       단, 2차 튜플/리스트 형태의 자료형만 변환 할 수 있으며, 구조는 다음과 같다.
#       ((key1, value1), (key2, value2), (key3, value3), ...)

d = {}
print(d, type(d))  

t = (('key', 'value'), ('a', 1), ('b', 2))
d = dict(t)
print(d, type(d))

# 사전형 자료에 접근 하는 방법
#     - Indexing과 동일하게 [](대괄호)를 사용하여 접근 한다.
#     - [] 안에는 key 가 사용 된다.

d = {'key': 'value', 'a': 1, 'b': 2}
print(d['key'], d['a'])

#반복문을 사용한 접근법
d = {'key': 'value', 'a': 1, 'b': 2}
for k in d:
    print(k, d[k])

#사전요소 수정 (요소만 바꿀 수 있다. key 는 바꾸지 못함)
d = {'key': 'value', 'a': 1, 'b': 2}
d['key'] = 'change'
print(d)


#dictionary function
# update(dict) : 사전형 자료의 새로운 key:value 요소를 추가/수정
#                    기존 요소에 동일한 key가 있으면, 수정
#                    기존 요소에 동일한 key가 없으면, 추가
d = {}
d.update({'a':1, 'b':2, 'c':3, 'd':4})
print(d)
d.update({'e':5, 'a':7})            # a 는 수정 e 는 추가
print(d)

#     get(key[, value]) : 사전형의 요소 중 key에 해당하는 요소의 값을 반환 한다.
#                         value 옵션을 사용하면, None 대신 value를 반환 한다.

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d.get('b'))
print(d.get('h'))       #None
print(d.get('h', 'not exist'))


#     keys() : 사전형 요소에서 key에 해당하는 요소만 반환 하는 함수
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d.keys())
for k in d.keys():
    print(d[k])

#     values() : 사전형 요소에서 value에 해당하는 요소만 반환 하는 함수
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d.values())
for v in d.values():
    print(v)


#     items() : 사전형 요소에서 key, value 쌍을 반환하는 함수
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d.items())
print(list(d.items()))
print(tuple(d.items()))
for kv in d.items():
    print(kv)


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for k, v in d.items():          # key 와 value 가 unpacking 되어서 k, v에 입력됨
    print(k, v)


#     pop(key) : 사전형의 key에 해당하는 요소를 반환 후 삭제 하는 함수
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
temp = d.pop('c')
print(temp)
print(d)


#   popitem() :  사전형의 마지막 요소의 key, value 의 쌍을 반환 후 삭제
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
temp = d.popitem()
print(temp)
print(d)

#     clear() : 사전형의 모든 요소 삭제
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d.clear()
print(d)

#   fromkeys(iterable[ ,value]) : iterable요소를 사용하여 key 를 생성한다
                                    # 옵션으로 value를 사용하면 기본값으로 사용

l = ['a', 'b', 'c', 'd', 'e', 'f']
d = dict.fromkeys(l, 1)
print(d)

#     setdefault(key[, value]) : 사전 자료형에 새로운 key, value를 추가하는 함수
#                                옵션으로 value를 사용하면, 해당 값을 요소로 사용
d = {'a':1, 'b':2}
d.setdefault('c', 3)
print(d)


d = {chr(x): x for x in range(65, 91)}
print(d)




