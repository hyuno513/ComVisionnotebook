# 단축키 : ctrl + shift + F10 = 내가 보고 있는 페이지를 실행
# 단축키2 : shift + F10 = 마지막으로 실행된 페이지를 실행
# 표준 입력
# input() 함수 : 표준 입력 장치(키보드)로 부터 입력받을 때 사용
n = input('')
print(n)

n = input('정수를 입력하세요.')
# n + 10 // 현재의 n은 정수가 아니라 문자열이다.
print(n)

n = int(input('정수를 입력하세요'))  # Casting 정수로 형변환
n = n + 10
print(n)
