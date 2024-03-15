# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3,5,7]
v_tuple = (3,5,7)
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 * f2)
print(f1 * i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4

print(type(a), type(b)) # <class 'float'> <class 'int'>
result2 = a + b
print(result2, type(result2)) # 9.0 <class 'float'>

# 형변환
print(int(9.)) # 9
print(float(1)) # 1.
print(complex(3)) # (3+0j)
print(int(True)) # 1
print(int(False)) # 0
print(int('3')) # 3
print(complex(0)) # 0j

y = 100
y += 100 # y = y + 100
print(y) # 200

# 수치 연산자
print(abs(-7)) # 절대값
n,m = divmod(100, 8) # 몫 연산과 나머지 연산을 한번에 수행
print(n,m) # 12 4

import math

print(math.ceil(5.1)) # 6
print(math.floor(3.874)) # 3
