# 인수와 매개변수
# 함수로 전달되는 인수(argment)를 저장하는 변수를 매개변수(parameter)라고 함

# 1. 인수가 있는 함수
def introduce(name, age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')


introduce('james', 25)  # 내 이름은 james이고, 나이는 25살 입니다.
introduce(age=25, name='james')  # 내 이름은 james이고, 나이는 25살 입니다.


# 2. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용
# 매개변수로 기본값을 설정할 수 있음
print()

def greet(message='안녕하세요'):
    print(message)


greet('반갑습니다')  # 반갑습니다
greet()

# 디폴트 매개변수가 있는 경우 뒤로 배치

def greet(name, message='안녕하세요'):
    print(f'{name}님 {message}.')


greet('김철수')  # 김철수님 안녕하세요.
greet('김철수', '반갑습니다.')  # 김철수님 반갑습니다.