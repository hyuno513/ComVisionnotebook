# 클래스 메소드와 정적 메소드
# 1. 클래스 변수
# 클래스를 구현할 때 인스턴스마다 서로 다른 값을 가지는 경우에는 인스턴스 변수를 사용
# 모든 인스턴스 변수들은 self 키워드를 붙여서 사용
# 모든 인스턴스가 동일한 값을 사용할 때는 클래스 변수로 처리해서 모든 인스턴스들이 공유하도록 처리하는 것이 좋음
# 인스턴스 변수는 인스턴스마다 값을 별도로 저장해야 하지만 클래스 변수는 하나의 값을 모든 인스턴스가
# 공유하기 때문에 메모리 공간의 낭비를 막을 수 있음

# * self
# 관례적으로 모든 메서드의 첫 번째 매개변수 이름을 self로 지정.
# self가 파이썬의 예약어는 아님.
# self라는 명칭은 관례적으로 사용하는 단어일 뿐.
# (파이썬의 객체와 관련된 설계에 영향을 준 스몰톡 smalltalk이라는 프로그램에서 옴.)


class Korean:
    country = '한국'  # 클래스 변수

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


print(Korean.country)
man = Korean('홍길동', 35, '대구')
print(man.name)
# print(Korean.name) # AttributeError: type object 'Korean' has no attribute 'name'
print(man.country)
print(Korean.country)

# ★ * 10 , ctrl + w : 코드의 선택 영역을 확장하는 단축키

print('객체 프로퍼티 생성과 동일한 이름의 클래스 변수')
man.country = '미국'  # 객체의 변수 생성
print(man.country)  # 미국. 클래스 변수가 아니라 인스턴스 변수를 불러옴. man객체의 country 라는 인스턴스 변수와 country 클래스 변수 2개가 존재
print(man.__class__.country)  # 한국

print()
man.company = '삼성'  # 객체의 프로퍼티 생성
print(man.company)  # 삼성

man.__class__.country = '영국'
print(Korean.country)


# 2. 클래스 메소드
# 클래스 변수를 사용하는 메소드를 의미
# 주요 특징
# 1. 인스턴스 혹은 클래스로 호출
# 2. 생성된 인스턴스가 없어도 호출할 수 있음
# 3. @classmethod 데코레이터 decorator 를 표시하고 작성
# 4. 매개변수 self를 사용하지 않고 cls를 사용
# 클래스 메소드는 self를 사용하지 않기 때문에 인스턴스 변수에 접근할 수 없지만,
# cls를 통해서 클래스 변수에 접근할 수 있음

class Korean:
    country = '한국'  # 클래스 변수

    @classmethod
    def trip(cls, country):
        print(cls)
        if cls.country == country:
            print('국내여행입니다.')
        else:
            print('해외여행입니다.')


Korean.trip('한국')
Korean.trip('미국')

# 3. 정적 메소드
# 1) 인스턴스 또는 클래스로 호출
# 2) 생성된 인스턴스가 없어도 호출 가능
# 3) @staticmethod 데코레이터 decorator 를 표시하고 작성
# 4) 반드시 작성해야 할 매개변수가 없음

# 정적 메소드는 self와 cls를 모두 사용하지 않기 때문에 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메소드를
# 정의하는 경우에 적절
# 정적 메소드는 클래스에 소속이 되어 있지만, 인스턴스에는 영향을 주지 않고 또 인스턴스로 부터 영향을 받지도 않음

class Korean:
    country = '한국'  # 클래스 변수 country

    @staticmethod
    def slogan():
        print('Imagine your Korea')


Korean.slogan()