# section04-4

# 딕셔너리(Dictionary) : 순서X, 중복X, 수정O, 삭제O
a = {'name': 'Kim','Phone': '010-7777-7777','birth': 870214,}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

print(type(a['name']))

# 조회
print(a['name'])
# print(a['address']) # 오류 발생
print(a.get('name'))
print(a.get('address')) # 오류 발생 X

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,3,4)

print()

# keys, values, items
print(a.keys()) # list 형태가 아닌 dict_keys 타입으로 제공됨. 인덱싱이 제공되지 않음
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
'''
dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
['name', 'Phone', 'birth', 'address', 'rank', 'rank2']
['Phone', 'birth']
dict_values(['Kim', '010-7777-7777', 870214, 'Seoul', [1, 3, 4], (1, 3, 4)])
['Kim', '010-7777-7777', 870214, 'Seoul', [1, 3, 4], (1, 3, 4)]
dict_items([('name', 'Kim'), ('Phone', '010-7777-7777'), ('birth', 870214), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 3, 4))])
[('name', 'Kim'), ('Phone', '010-7777-7777'), ('birth', 870214), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 3, 4))]
'''

# 집합
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(l)

print()
print()

# 집합 연산
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)
'''
{4, 5, 6}
{4, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{1, 2, 3}
{1, 2, 3}
'''

print()

# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(7)
print(s3)

s3.add(18)
print(s3)
s3.remove(15)
print(s3)

print(type(s3))
'''
{8, 10, 15, 7}
{7, 8, 10, 15, 18}
{7, 8, 10, 18}
<class 'set'>
'''