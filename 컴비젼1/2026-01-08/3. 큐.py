'''
스택과 다르게 항목이 들어온 순서대로 접근 가능.
먼저 들어온 데이터가 먼저 나가는 선입선출 first in, first out (FIFO) 구조.
큐 역시 배열의 인덱스 접근이 제한 됨.
롤러코스트 타는 것을 기다리는 사람들의 줄로 생각하면 쉽다.

* enqueue : 큐 뒤쪽에 항목을 삽입.
* dequeue : 큐 앞의 항목을 반환하고, 제거
* peek   : 큐 앞쪽의 항목을 조회.
* empty : 큐가 비어있는지 확인
* size : 큐의 크기를 확인.
'''
from typing import Any


class Queue:
    def __init__(self):
        self.items = [] # 빈 리스트 생성

    def is_empty(self) -> bool:  # 큐가 비어있는지 확인
        return not bool(self.items)

    def enqueue(self, item): # 큐 뒤쪽에 항목을 삽입
        self.items.insert(0,item) # 뒤쪽에 삽입이지만 0번 인덱스에 데이터가 추가

    def size(self) -> int:  # 큐의 크기를 확인
        return len(self.items)  # len 함수 : 길이를 재는 함수

    def peek(self) -> Any:  # 스택 맨 끝 항목을 조회
        if self.items:
            return self.items[-1]
        else:
            print('Queue is empty')

    def dequeue(self) -> Any: # 큐 앞의 항목을 반환하고 제거
        value = self.items.pop()
        # 만약에 value가 없는 경우 ??
        if value is not None:
            return value
        else:
            print('큐가 비어 있습니다.')

    def __repr__(self) -> str:  # 객체를 어떤 데이터 타입이던 객체를 문자열 표현으로 반환
        return repr(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(f'큐가 비었나요? {queue.is_empty()}')  # True
    print('큐에 숫자 0~9를 추가합니다.')
    for i in range(10):
        queue.enqueue(i)
    print(f'큐 크기: {queue.size()}')  # 10
    print(queue) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f'peek: {queue.peek()}')  # 0
    print(f'dequeue: {queue.dequeue()}')  # 0
    print(f'peek: {queue.peek()}')  # 1
    print(f'큐가 비었나요? {queue.is_empty()}')  # False
    print(queue) # [9, 8, 7, 6, 5, 4, 3, 2, 1]