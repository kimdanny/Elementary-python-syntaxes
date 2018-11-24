'''
파일 입출력
프로그램에서 생성된 데이터를 파일 형태로 출력(저장)을 하거나
파일이 저장되어 있는 데이터를 읽어서 프로그램에서 사용하기 위한 데이터로 쓰기 위해 사용한다

open() 내장함수를 사용한다
open(path, mode, encoding)
    path : 파일을 읽거나 쓰기위한 경로.
            절대 경로 : 드라이브명 부터 시작하는 모든 경로
                    예) C:\\Program Files\\Python3\\python.exe
            상대 경로 : 프로그램이 실행되는 위치의 상대적인 경로
                    예) python.exe
                        .\\python.exe
                        ..\\Python3\\python.exe         #..은 현재 위치보다 상위폴더임을 알려준다

    mode : 파일을 읽기 또는 쓰기 모드를 지정하기 위해 사용하는 인자
            r (read) 읽기 모드 // w (write) 쓰기 모드(덮어쓰기) // a (append) 쓰기모드 (이어쓰기)

    encoding : 작성된 문자열을 자장할때 또는 읽을 때 사용할 변환 코드명 지정
                cp949 : MS 한글 기본 인코딩 방식
                utf-8 : 표준 인코딩 방식
'''
fo = open('D:\\File_Test\\DirA\\sampleA.txt', mode='r', encoding='cp949')
#print(fo.read)
print(fo.readlines())
fo.close()      #make sure you write close statement at the end

fo = open('..\\..\\File_Test\\DirA\\sampleA.txt', mode='r', encoding='cp949')
print(fo.read())
fo.close()

fo = open('D:\\201807_python 기초_김도은\\workspace\\ch02\\03_input_ex_bmi.py', mode='r', encoding='utf-8')
print(fo.read())
fo.close()


fo = open('D:\\File_Test\\DirB\\sampleA.txt', mode='w', encoding='utf-8')
fo.write('hello world \n')
fo.write('world hello \n')
fo.close()


fo = open('D:\\File_Test\\DirB\\sampleA.txt', mode='a', encoding='utf-8')
fo.write('append \n')
fo.close()





