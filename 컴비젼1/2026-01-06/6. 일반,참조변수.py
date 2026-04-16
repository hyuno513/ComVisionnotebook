# # 일반 변수
# num1 = 10
# num2 = 20
# print(num1)  # 10
# print(num2)  # 20
#
# num1 = num2
# print(num1)  # 20
# print(num2)  # 20
#
# num2 = 30
# print(num1)  # 20
# print(num2)  # 30


# 참조 변수 관련
class Score:
    def __init__(self, no: int):  # no : int 굳이 안적어도 문제 x
        self.no = no

    def __str__(self) -> str:
        return str(self.no)


no1 = Score(10)
no2 = Score(20)
print(no1)
print(no2)
print(id(no1))
print(id(no2))

no1 = no2
print(no1)
print(no2)
print(id(no1))  # 1779145247632
print(id(no2))  # 1779145247632

no2.no = 30
print(no1)
print(no2)
print(id(no1))
print(id(no2)) 