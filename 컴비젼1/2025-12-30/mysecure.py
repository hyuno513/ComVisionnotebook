# 모듈명 : mysecure.py
# secure_name()함수 : 김철수 -> 김**
# secure_no() 함수 : 951012-1234567 -> 951012-1******
# secure_phone() 함수 : 010-1234-5678 -> 010-****-5678

def secure_name(name):
    return name[0] + '**'


def secure_no(no):
    return no[0:8] + '******'


def secure_phone(phone):
    # return phone[0:4] + '****' + phone[8:]
    return phone.replace(phone[4:8], '****')

