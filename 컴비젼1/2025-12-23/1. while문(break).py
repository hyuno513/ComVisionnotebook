# 이름 바꾸기 단축키 : shift + F6

# break문
# while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# 반복문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문은 종료

# n = 1
# while n <= 10:
#     print(n)
#     n += 1 # n = n + 1
#
# print(n)  # 11
#
# n = 1
# while True:
#     print(n)
#     if n == 10:
#         break  # if 문에서 break문을 작성했지만 실제로 종료되는 것은 while문
#     n += 1
# print(n)  # 10


while True: # 무한 루프
    city = input('대한민국의 수도는 어디인가요? >>> ')
    city = city.strip() # strip() 은 공백문자를 제거시켜주는 상황
    if city == '서울' or city == 'seoul' or city == 'SEOUL': # 대소문자 모두 정답처리
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')