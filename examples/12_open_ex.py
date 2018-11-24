#1. 파일 읽고 터미널에 출력
path = 'C:\\python_academy\\IDE_100.csv'
fo = open(path, mode='r', encoding='utf-8')
data = fo.read()
fo.close
print(data)

#1-1 for 사용
path = 'C:\\python_academy\\IDE_100.csv'
fo = open(path, mode='r', encoding='utf-8')

for line in fo.readlines():
    print(line, end='')
fo.close()


# #2. 파일 읽고 새로운 파일로 출력
#     - NA 데이터 항목은 제외하고 새로운 파일로 출력
#     - 파일명은 new_IDE_100.csv 로 한다

path = 'C:\\python_academy\\IDE_100.csv'
fo = open(path, mode='r', encoding='utf-8')
data = fo.read()
fo.close()

path = 'C:\\python_academy\\IDE_100.csv'
fo = open(path, mode='w', encoding='utf-8')
fo.write(data.replace('NA\n', ''))
fo.close


#2-1    for if continue 사용
src_path = 'C:\\python_academy\\IDE_100.csv'
dst_path = 'C:\\python_academy\\new_IDE_100.csv'
fo = open(src_path, mode='r', encoding='utf-8')
fw = open(dst_path, mode='w', encoding='utf-8')

for line in fo.readlines():
    if line == 'NA\n':
        continue
    else:
        fw.write(line)

fo.close()
fw.close()


print(fo.readlines())
print(type(fo.readlines()))
new = fo.readlines().remove('NA\n')
print(new)
fo.close


# 3. IDE_100.csv에 존재하는 프로그램명과 작성 횟수를 출력 하시오.
#     예)
#         Visual Studio Code : 10회
#         Eclipse : 8회
#         ...
path = 'C:\\python_academy\\IDE_100.csv'
fo = open(path, mode='r', encoding='utf-8')
data = fo.readlines()
print(data.count('NA\n')
# ; 기준으로 split하고 count


# 4. 3번에서 작성한 코드를 이용하여 가장 많은 횟수를 기록한 프로그램명 부터
#    출력하시오.



# 5. 4번 까지 작성한 코드를 이용하여 터미널에 그래프를 그려서 출력 하시오.
#     예)
#         Visual Studio Code [#################       ] 34.9 %
#         Eclipse            [###########             ] 12.3 %
#         Notepad++          [#####                   ]  8.2 %

#ENGF0002

def withwrite():
    with open(r"sth.txt") as f:
        f.write(b"\X00\X01\X02\X04")

    with open("something.bin", "r+b") as f2:
        f2.seek(2)              #goto byte2
        b = f2.read(1)
        assert b == b"/x02"
        assert f2.tell() == 3