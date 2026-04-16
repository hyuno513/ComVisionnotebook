# 메소드
# 메소드 method란 특정 객체 object가 가지고 있는 함수 functuin을 의미
# 함수는 독립적으로 호출할 수 있지만, 메소드는 특정 객체를 통해서만 호출할 수 있음.

# 함수와 다르게 메소드는 특정 객체 소속이어서, 메소드를 호출하려면
# 특정 객체를 통해서만 호출 가능

# 1. 문자열 메소드
# 문자열 str을 처리하기 위해 많은 메소드를 제공

# 1) format()
# 정렬 옵션
# < : 지정된 공간 내에서 왼쪽 정렬
# > : 지정된 공간 내에서 오른쪽 정렬
# ^ : 지정된 공간 내에서 가운데 정렬

# 10d는 10자리의 필드 폭을 의미
print("10자리 폭 왼 쪽 정렬 '{:<10d}'".format(123))  # 10자리 폭 왼 쪽 정렬
print("10자리 폭 오른 쪽 정렬 '{:>10d}'".format(123))  # 10자리 폭 오른 쪽 정렬
print("10자리 폭 가운데 쪽 정렬 '{:^10d}'".format(123))  # 10자리 폭 가운데 정렬

# 2) count() ★ * 5
# 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드
s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))

# 인덱스를 지정해서 범위를 지정할 수 있음
s = 'best of best'
print(s.count('best', 5))

# 마이너스 인덱스를 사용할 수 있음
s = 'best of best'
print(s.count('best', -7))  # 1/ o 부터 검색

# 3) find() ★ * 5
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# 찾고자 하는 문자열이 있으면 그 문자열이 처음으로 나온 위치 즉 인덱스 index 를 반환
print()
s = 'apple'
print(s.find('p'))

# 찾는 문자열이 없는 경우 -1 반환
s = 'apple'
print(s.find('z'))  # -1

# 4) 대소문자 변환 메소드
# upper : 모두 대문자로 변환한 결과를 반환
# lower : 모두 소문자로 변환한 결과를 반환
# capitalize : 첫 글자는 대문자로 변환하고 나머지는 소문자로 변환한 결과를 반환
print()
s = 'BEST of best'
print(s.upper())  # BEST OF BEST
print(s.lower())  # best of best
print(s.capitalize())  # Best of best

# 5) join()
# 인수로 전달한 반복가능객체(문자열, 리스트등)의 각 요소 사이에
# 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 반환
print()

print('-'.join('python'))  # p-y-t-h-o-n

print('+'.join(['a', 'b', 'c', 'd', 'e']))  # a+b+c+d+e

# 포함하는 문자 없이 단순하게 리스트의 요소들을 연결하고자 한다면 빈 문자열 사용
print(' '.join(['x', 'y', 'z']))  # x y z
a = {'a': 'apple', 'b': 'banana'}
print(''.join(a))  # ab /딕셔너리의 경우 key를 연결

# 6) split() * 5
# 하나의 문자열을 여러 개의 문자열로 분리해서 저장한 리스트를 반환
print()
s = 'Life is too short'
s2 = s.split()  # split()메소드에 아무 인수도 전달하지 않으면 공백문자를 기준으로 각 문자열이 분리
print(s2)  # ['Life','is','too','short]

s = '010-1234-5678'
s2 = s.split('-')  # 공백 대신 특정 문자열을 기준으로 분리하는 방법
print(s2)  # ['010','1234','5678']

# 7) replace()
# 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환
print()
s = 'Life is too short'
s2 = s.replace('short', 'long')
print(s2)  # Life is too long

# 특정 문자열을 제거하기 위한 용도로 사용
s = '010-1234-5678'
s2 = s.replace('-', '')
print(s2)  # 01012345678.

# 8) 불필요한 문자열 제거 메서드
# 문자열 양끝에 있는 불필요한 문자열을 제거
# lstrip() : 왼쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# rstrip() : 오른쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# ★ strip() : 양 끝에 있는 불필요한 문자열을 제거한 결과를 반환
print()
s = '       apple'
print(len(s))  # 12

s2 = s.strip()
print(s2)
print(len(s2))

# 공백 문자 이외에 불필요한 문자열을 직접지정하여 제거
s = '<head'
s2 = s.strip('<')
print(s2)
