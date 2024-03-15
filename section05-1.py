# Section05-1
# 제어문

print(type(True))
print(type(False))

# 예1
if True:
    print('Yes')

# 예2
if False:
    print("No")
else:
    print("Yes2")
print()

# 논리 연산자
a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)
'''
and :  True
or :  True
not :  False
True
False
'''
print()


# 다중 조건문
num = 82

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("num 등급 A", num)

print()

# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 170:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

'''

'''

print()
