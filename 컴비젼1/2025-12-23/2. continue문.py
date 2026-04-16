# continue 문
# 반복문의 시작 지점으로 제어의 흐름을 옮기는 역활
# 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 사용

# 1에서 100까지의 모든 정수를 합하는데 3의 배수는 제외한 숫자들의 합을 알아내시오.

# total = 0
# for i in range(1, 101):
#     if i % 3 != 0:
#         total += i
# print(total)
#
# total = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         continue
#     total += i
# print(total)

# fruits = ['사과', '귤']
# count = 3  # 입력 가능한 횟수
#
# while count > 0:
#     fruit = input('어떤 과일을 저장할까요? >>> ')
#     if fruit in fruits:  # fruits 리스트에 fruit 변수에 있는 값이 있다면
#         print('동일한 과일이 있습니다.')
#         continue
#     fruits.append(fruit)
#     count -= 1
#     print(f'입력이 {count}번 남았습니다.')
#
# print(f'5개 과일은 {fruits}입니다.')


money = 10000

while money > 0:
    print(f'현재 {money}원이 있습니다.')
    a = int(input('사용할 금액 입력 >>> '))
    if a <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.')
        continue
    if money - a < 0:
        print(f'{a - money}원이 부족합니다.')
        continue
    money -= a
print(f'현재 {money}원이 있습니다.')
