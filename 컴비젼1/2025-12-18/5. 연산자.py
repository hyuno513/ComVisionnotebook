# 산술 연산자
a = 7
b = 2
print(f'{a}+{b}={a + b}')
print(f'{a}-{b}={a - b}')
print(f'{a}*{b}={a * b}')
print(f'{a}/{b}={a / b}')  # 나눗셈
print(f'{a}//{b}={a // b}')  # 몫
print(f'{a}%{b}={a % b}')  # 나머지

# 대입연산자
print("=" * 20)

a, b = 10, 20
print(f'a={a}, b={b} = {a, b}')
a, b = b, a  # 값을 교환
print(f'a = {a}, b = {b} = {a, b}')

# ==========================================

# 문제 : 출력 결과를 보고 코딩하시오.
piggy_bank = 1000

money = 10000

snack = 2000

# 출력 결과는 다음과 같습니다.

# 저금통에 용돈10000원을 넣었습니다.
# 지금 저금통에는11000원이 있습니다.
# 저금통에서 스낵 구입비 2000원을 뺐습니다.
# 지금 저금통에는 9000원이 있습니다.

# piggy_bank = piggy_bank + money
piggy_bank += money  # 위의 내용과 동일한 코드

print(f'저금통에 용돈{money}원을 넣었습니다.')
print(f'지금 저금통에는{piggy_bank}원이 있습니다.')
print(f'저금통에서 스낵 구입비 {snack}원을 뺐습니다.')
piggy_bank -= snack  # piggy_bank = piggy_bank - snack
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')

print("=" * 20)

# =============================

# 비교연산자
# 결과 값은 True와 False 둘 중 하나

a = 15
print(f'{a} > 10 : {a > 10}')  # True a가 10보다 크다.
print(f'{a} < 10 : {a < 10}')  # False a가 10보다 작다
print(f'{a} >= 10 :{a >= 10}')  # True a가 10보다 크거나 같다
print(f'{a} <= 10 :{a <= 10}')  # False. a가 10보다 작거나 같다
print(f'{a} == 10 :{a == 10}')  # False a와 10이 같다
print(f'{a} != 10 :{a != 10}')  # True a와 10이 다르다.

print("=" * 20)
# 논리연산자 : and & , or ||
# and 연산자는 모든 상황이 True가 떠야 True가 된다.
# 논리곱
print(f'True and True : {True and True}')  # True and True : True
print(f'True and False : {True and False}')  # True and False : False
print(f'False and True : {False and True}')  # False and True : False
print(f'False and False : {False and False}')  # False and False : False

print()

# 논리합
# or 연산자는 True가 하나만이라도 있으면 True로 출력된다.
print(f'True or True : {True or True}')  # True or True : True
print(f'True or False : {True or False}')  # True or False : True
print(f'False or True : {False or True}')  # False or True : True
print(f'False or False : {False or False}')  # False or False : False

# 논리 연산자
# 결과 값은 True 와 False 둘중 한나
# a and b : a와b가 모두 참(True)이면 True, 아니면 False
# a or b : a와 b중 하나라도 참(True)이면 True, 아니면 False
# not a : a가 참(True)

a = -10
b = 0

print(f'{a} >0 and {b} > 0 : {a > 0 and b > 0}')  # False / True and True
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}') # True
print(f'not {a} : {a, not a}')
print(f'not {b} : {b, not b}')

# 프로그래밍에서 0을 제외한 나머지 숫자는 무조건 True로 인식한다.

print('=' * 20)

# 시퀀스 연산자 : 순서가 있는 시퀀스 (리스트,튜플,range,문자열 등)에서 사용할 수 잇는 연산자
# + : 연결하기
# * : 반복하기
tree = '#'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)
print('-' * 20)

# 삼항 조건 연산자
# 일반적인 삼항 조건 연산자 : 조건식 ? 참 : 거짓
# 파이썬 삼항 조건 연산자 : 참 if 조건식 else 거짓

a = 10
b = 20
result = (a - b) if (a >= b) else (b - a) # 조건식 a >= b 은 False, b - a 실행
print(f'{a} 과 {b} 의 차이는 {result}입니다.')
