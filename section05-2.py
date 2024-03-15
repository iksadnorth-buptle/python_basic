# Section05-2
# 제어문

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2)

print()

# 1~ 100 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

# 시퀀스(순서가 있는) 자료형 반복
# iterable : range, reversed, enumerate, filter, map, zip
    
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]
for v in names:
    print("You are : ", v)

word = "dreams"
for s in word:
    print(s)
'''
You are :  Kim
You are :  Park
You are :  Cho
You are :  Choi
You are :  Yoo
d
r
e
a
m
s
'''

print()

# 딕셔너리 반복
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul",
}

for key in my_info:
    print("my_info ", key)
print()

for key in my_info.keys():
    print("my_info ", key)
print()

for key in my_info.values():
    print("my_info ", key)
print()

for key, value in my_info.items():
    print("my_info ", key, value)
print()
'''
my_info  name
my_info  age
my_info  city

my_info  name
my_info  age
my_info  city

my_info  Kim
my_info  33
my_info  Seoul

my_info  name Kim
my_info  age 33
my_info  city Seoul
'''

# break
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
else:
    print("not found 33.......")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))
