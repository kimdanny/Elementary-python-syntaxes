'''
1. sequence type : 초기에 생성된 데이터의 순서를 유지하고
                    인덱스 넘버에의해 접근가능
2. Iterable type : 반복가능 자료형으로 for 반복문에의해 사용
3. Mutation type : 변경 가능 자료형, 리스트 자료의 요소를 추가 수정 삭제 가능

# 생성 방법
[] 대괄호를 사용하여 생성한다
각각의 요소를 구분하기 위한 , 쉼표를 사용한다
튜플 사전 문자열 자료형에 대해 리스트 자료형으로 변환 할 수 있다
리스트는 빈 리스트 형태로 생성가능하다

'''

l = []
print(l, type(l))

l = [1, 2, 3]
print(l, type(l))

t = (1, 2, 3, 'a', 'b')
l=list(t)
print(l, type(l))

l1 =[1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = l1 + l2
print(l3, type(l3))

l = [1, 2]*3
print(l, type(l))

#List comprehension - 반복문을 이용하여 리스트 자료형 생성
l = ['a' for x in range(10)]
print(l, type(l))

l = [x for x in range(10)]
print(l, type(l))

#Unpacking
l = [1, 2]
l1, l2 = l
print(l1, l2)


#Indexing and Slicing
#튜플에서 사용하는 방식과 동일
l = [1, 2, 3, 'a', 'b', 'c']
print(l[0], l[-2], l[1], l[0:3])
print(l[-5:-2], l[0:6:2], l[-6::2])


#n 차 리스트
# 2 차 리스트
l = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(l[0][1], l[2][0])
print(l[1:3])
print(l[1:3][0][1])

l = [[chr(x), chr(x+1)] for x in range(65, 91, 2)]
for x in l:
    print(x)
print(l)


l = [[chr(x), chr(x+1)] for x in range(65, 91, 2)]
print(l)
for x in l:
    print(x)
    for y in x:
        print(y)

l = [['A', 'B'], ['C', 'D'], ['E', 'F']]
print(l)
for idx in range(len(l)):
    print(l[idx])
    print(l[idx][0], l[idx][1])


# 리스트의 특정 요소 수정
l = [1, 2, 3, 4, 5, 6]
l[3] = 40
l[0:2] = 10, 20
print(l)
for idx in range(len(l)):
    l[idx] = (idx +1)*10
print(l)

# 리스트에 10개의 요소를 생성하고 그 안의 값을 3의 배수로 생성.
l = [0] * 10
for idx in range(len(l)):
    l[idx] = (idx + 1) * 3
print(l)


#list function
#     append(value) : 리스트의 마지막 요소에 value를 추가 한다.
l = []
l.append(10)
for x in range(2, 5):
    l.append(x * 10)
l.append([1, 2, 3])
print(l)

#     extend(iterable) : 리스트의 마지막 요소에 iterable의 요소들을 추가
l = []
l.extend([1, 2, 3])
l.extend(('a', 'b', 'c'))
print(l)

#     insert(index, value) : 리스트의 index 위치에 value를 추가
l = [1, 2, 3]
l.insert(1, 10)
l.insert(2, 20)
print(l)

#     pop([index]) : 리스트의 마지막 요소를 반환 후 삭제
#                    index 값을 사용하는 경우 index 위치의 요소를 반환 후 삭제
l = [1, 2, 3, 4, 5]
x = l.pop()         #x 는 요소 반환값 (뭐가 지워졌는지)
y = l.pop(1)        #y 도 요소 반환값
print(l, x, y)


#     remove(value) : 리스트의 요소 중 value에 해당하는 요소 삭제
l = [1, 2, 3, 'a', 'b', 'c', ['d', 'f']]
l.remove('a')
print(l)
l[-1].remove('d')
print(l)
# l.remove('d') 는 에러

#     clear() : 리스트의 모든 요소 삭제
l = [1, 2, 3, 'a', 'b', 'c', ['d', 'f']]
l.clear()
print(l)

#   count(value) : 리스트의 요소중 value에 해당하는 요소 수 반환
l = [1, 2, 3, 2, 1, 4, 1]
print(l.count(1))

#   index(value[, start_index]) : 리스트의 요소중 value에 해당하는 요소의 index 번호를 반환한다.
#                                 start_index 지정하면 start_index 부터 value에 해당하는 요소의 index 번호를 반환
l = [1, 2, 3, 2, 1, 4, 1]
print(l.index(1))
print(l.index(1, 1))
print(l.index(1, 5))
