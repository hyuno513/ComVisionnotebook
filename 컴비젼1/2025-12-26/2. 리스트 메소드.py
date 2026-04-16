# # 2. 리스트 메소드
# # 1) append()
# # 리스트의 끝에 인수로 전달된 데이터를 추가
#
# my_list = ['apple', 'banana']
# my_list.append('cherry')
# print(my_list)  # ['apple', 'banana', 'cherry']
#
# # 2) extend()
# # 리스트에 다른 리스트나 튜플과 같은 반복가능객체를 추가하여 기존 리스트를 확장
# print()
# my_list = ['apple', 'banana']
# my_list.extend(['cherry', 'mango'])
# print(my_list)  # ['apple', 'banana', 'cherry', 'mango']
#
# my_list = ['apple', 'banana']
# my_list += ['cherry', 'mango']  # my_list = my_list + [cherry, manggo]
#
# # 3) insert()
# # 리스트의 특정 인덱스에 데이터를 추가
# print()
# my_list = ['apple', 'banana']
# my_list.insert(0, 'cherry')
# print(my_list)  # ['cherry', 'apple', 'banana']
#
# # 4) clear()
# # 리스트에 저장된 모든 요소를 삭제
# print()
# my_list = ['apple', 'banana']
# my_list.clear()
# print(my_list)  # []
#
# my_list = ['apple', 'banana']
# my_list = []
# print(my_list)  # []
#
# # 5) pop()
# # 리스트의 마지막 요소가 반환되면서 삭제
# print()
# my_list = ['apple', 'banana']
# item = my_list.pop()
# print(item)  # banana
# print(my_list)  # ['apple']
#
# # 6) remove()
# # 인수로 전달된 값과 동일한 요소를 찾아서 제거. 동일한 요소가 여러 개인 경우에는 첫 번째 요소가 제거
# print()
# my_list = ['apple', 'banana', 'cherry', 'mango']
# my_list.remove('cherry')
# print(my_list)  # ['apple', 'banana', 'mango']
#
# my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
# my_list.remove('cherry')
# print(my_list)  # ['apple', 'banana', 'mango', 'cherry']

# 다음은 리스트에 포함된 잘못된 데이터를 모두 제거하는 프로그램입니다.
# 리스트에 저장된 정상 데이터는 모두 'a'를 포함한 문자열이며, 그렇지 않은 경우 잘못된 데이터입니다.

a_list = ['above', 'cookie', 'app', 'about', 'bisket', 'apple', 'april']
for i, item in enumerate(a_list):
    if 'a' not in item:
        print(f'{a_list.pop(i)}이 제거됩니다.')

print(a_list)
