# Section04-3

# 선언
a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])
'''
Banana
Banana
110
Banana
Banana
'''

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')
'''
[1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
1hi
'''

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 1000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)
'''
[77, 2, 3, 4]
[77, 100, 1000, 1000, 3, 4]
[77, ['a', 'b', 'c'], 1000, 1000, 3, 4]
'''

del c[1]
print(c)
del c[-1]
print(c)
'''
[77, 1000, 1000, 3, 4]
[77, 1000, 1000, 3]
'''

# 리스트 함수
y = [5,2,3,1,4]

y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2,7)
print(y)

y.remove(2)
print(y)

y.pop()
print(y)

ex = [88,77]
y.extend(ex)
print(y)
'''
[5, 2, 3, 1, 4, 6]
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
[6, 5, 7, 4, 3, 2, 1]
[6, 5, 7, 4, 3, 1]
[6, 5, 7, 4, 3]
'''

# 튜플 선언
a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

print()
print()
'''
3
4
b
(('a', 'b', 'c'),)
('a', 'b')
(1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
'''

# 튜플 함수
z = (5,2,1,3,4)

print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))
'''
(5, 2, 1, 3, 4)
True
3
1
'''
