# section07-1

# 클래스 선언
# 클래스명 <= Upper CamelCase

# 예제1
class UserInfo:
    def __init__(self, name) -> None:
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스 - 인스턴스가 가지고 있는 자기 자신의 저장 공간.
user1 = UserInfo("Kim")
user1.user_info_p()

user2 = UserInfo("Park")
user2.user_info_p()

print(user1.name)
print(user2.name)

print(user1.__dict__) # 딕셔너리 형태로 출력.
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest:
    def function1(): # self 인자를 받고 있지 않기 때문에 클래스 함수
        print("function1 called!")
    def function2(self):
        print("function2 called!")

# 인스턴스 함수 호출
self_test = SelfTest()
# self_test.function1()
self_test.function2()

SelfTest.function2(self_test)

# 클래스 함수 호출
SelfTest.function1()


# 예제3
class WareHouse:
    stock_num = 0

    def __init__(self, name) -> None:
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)
print()

print(user1.name)
print(user2.name)
print(user3.name)
print()

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)
print()

del user1
print(user2.stock_num)
print(user3.stock_num)
print()
'''
{'name': 'Kim'}
{'name': 'Park'}
{'name': 'Lee'}
{'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x0000027E65C450D0>, '__del__': <function WareHouse.__del__ at 0x0000027E65C45158>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}

Kim
Park
Lee

3
3
3

2
2
'''