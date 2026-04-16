# 조건문

# 1.if 문
# if 조건식 :
#   조건식의 결과가 True 일 때 실행문

num = 15
# if num > 0:
#     print('양수')
# if True:
#     print('True')

# 들여쓰기 indentation 규칙
# 1. 공백 space이나 탭 tab을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관이 없음
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 함. 공백과 탭을 혼용하여
# 사용할 수 없고 들여쓰기 수준도 동일해야 함
# 5. 주로 사용하는 들여쓰기는 공백 4개, 공백 2개, 탭 1개.

# if num > 0: print('양수')  # 실행문이 하나면 한 줄 코드로 가능

# 단축키 : 정렬단축키 : ctrl + Alt + L

# 2. if-else 문
# if 조건식 :
# 조선식의 결과가 True일 때 실행문
# else :
# 조건식의 결과가 False일 때 실행문
# num = 1
# if num>=0:
#     print('양수')
# else:
#     print('음수')

# 3. if-elif 문
# if 조건식1:
#   조건식1의 결과가 True일 때 실행문
# elif 조건식2 :
#   조건식1의 결과가 False이고, 조건식2의 결과가 True일 때 실행문
# elif 조건식3 :
#   조건식1,2의 결과가 False이고, 조건식3의 결과가 True일 때 실행문
# else:
# 조건식1,2,3의 결과가 False일 때 실행문

important = 56
# if important >= 100:
#     print('상')
# else:
#     if important >= 50:
#         print('중')
#     else:
#         print('하')

# if important >= 100:
#     print('상')
# elif important >= 50:
#     print('중')
# else:
#     print('하')


# 나이를 입력받아 7살 이하면 '미취학', 8~13이면 '초등학생', 14~16살이면 '중학생',
# 17~19살이면 '고등학생', 20살 이상이면 '성인'을 출력하는 프로그램입니다.

# age = int(input('몇 살 입니까?'))  # int() 함수를 이용해서 정수로 변환
#
# if age <= 7:
#     print('미취학')
# elif age < 14:
#     print('초등학생')
# elif age < 17:
#     print('중학생')
# elif age < 20:
#     print('고등학생')
# else:
#     print('성인')


# 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요.

# 실행 예)
# 정수1 입력 >>>2
# 정수2 입력 >>>3
# 정수3 입력 >>>1

# 가장 큰 수는 3입니다
a = int(input('정수1 입력 >>> '))
b = int(input('정수2 입력 >>> '))
c = int(input('정수3 입력 >>> '))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(f'가장 큰 수는 {max}입니다.')
