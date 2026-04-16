# while 문
# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용
# while 조건식 :
# 반복실행문

# n = 1
# while n <= 10:
#     print(n)
#     n += 1  # n = n + 1

# while문의 중첩
# while문 내부에 또 다른 while문이 나타나는 것

# day = 1
# hour = 1
# while day <= 5:
#     hour = 1
#     while hour <= 3:
#         print(f'{day}일차 {hour}교시 입니다.')
#         hour += 1
#     day += 1

# 100부터 50 사이의 짝수를 출력
# n = 100
# while n >= 50:
#     print(n)
#     n -= 2  # n = n -2
#
# while n >= 50:
#     if n % 2 == 0:
#         print(n)
#     n -= 1

# 구구단 2단 부터 9단까지 출력
# 각 단 앞에 제목, 마지막에 구분선을 넣어 볼 것
# dan = 2
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f'{dan}x{n}={dan * n}')
#         n += 1
#     print(f'{dan}단이 끝났습니다.')
#     dan += 1
#
# dan = 2
# while dan <= 9:
#     n = 1
#     print(f'{dan}단 시작')
#     while n <= 9:
#         print(f'{dan}x{n}={dan * n}')
#         n += 1
#     print(f'{dan}단이 끝났습니다.')
#     dan += 1


# number = 1
#
# while number <= 100:
#     if number % 10 - 1 == 0: # 이해해오기
#         print()
#     print(f'{number}  ', end=' ')
#     number += 1


