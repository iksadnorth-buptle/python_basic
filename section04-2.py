# Section04-2

str1 = "I am Boy."
str2 = "NiceMan"
str3 = " "
str4 = str('')

print(len(str1),len(str2),len(str3),len(str4),) # 9 7 1 0

# 이스케이프 문자
escape_star1 = "Do you have a \"big collection\""
print(escape_star1) # Do you have a "big collection"
escape_star2 = "Tab\tTab\tTab"
print(escape_star2) # Tab     Tab     Tab

# Raw String 
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1) # C:\Programs\Test\Bin
raw_s2 = r'\\a\\a'
print(raw_s2) # \\a\\a

# 멀티라인
multi1 = """
문자열
멀티라인
테스트
"""
multi2 = \
"""
문자열
멀티라인
테스트
"""

print(multi1)
print(multi2)
"""
문자열
멀티라인
테스트


문자열
멀티라인
테스트
"""

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)

str_o4 = "Niceman"

print('a' in str_o4) # True
print('f' in str_o4) # False
print('z' not in str_o4) # True

# 문자열 형 변환
print(str(77))

# 문자열 함수 
a = 'niceman'
b = 'orange'

print(a.islower()) # True
print(b.endswith('e')) # True
print(a.capitalize()) # Niceman
print(a.replace('nice', 'good')) # goodman
print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']

# 문자열 슬라이싱 
a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:])
print(a[0:4:2])

print(b[1:-2])
print(b[::-1])
"""
nic
nice
niceman
niceman
nc

ran
egnaro
"""