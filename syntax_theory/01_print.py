print('이름', '김도은', sep=':')
print('전화번호: 010', '1234', '5678', sep='-' )        # '전화번호: 010' 을 하나로 두면 sep 를 쓸 수 있다


print('전화번호', end=':')
print('010', '1234', '5678', sep='-' )


print('주소', end=':')
print('seoul', 'jongno', 'jonnosamga')

print('주소:', '\b서울시', '종로구', '종로3가')             # /b 는 백스페이스
print('주소:', '서울시', '종로구', '종로3가')


print('\"C:\program files\python35\scripts\\"')
print('\"C:\program files\python35\lib\site-packages\\"')


print('"C:',  'program files', 'python35', 'scripts', '"', sep='\\')            # \\ 가 \ 를 출력하는 하나의 문자


input()
