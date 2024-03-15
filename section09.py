# Section09

# 예제 1
# 파일 읽기
f = open("./resource/review.txt", 'r')
content = f.read()
print(content)

f.close()


# 예제 2
with open("./resource/review.txt", 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("-------------------")
print("-------------------")

# 예제3
with open("./resource/review.txt", 'r') as f:
    for c in f:
        print(c.strip())

print("-------------------")
print("-------------------")


# 예제4
with open("./resource/review.txt", 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)


print("-------------------")
print("-------------------")


# 예제5
with open("./resource/review.txt", 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' ### ')
        line = f.readline()


print("-------------------")
print("-------------------")


# 예제6
with open("./resource/review.txt", 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' %%%%%% ')


print("-------------------")
print("-------------------")


# 예제7
score = []
with open("./resource/score.txt", 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('Average : {:6.3}'.format(sum(score)/len(score)))

print("-------------------")
print("-------------------")


# 파일 쓰기
# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'a') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제4
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n','Park\n','Cho\n',]
    f.writelines(list)

# 예제5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contest1!', file=f)
    print('Test Contest2!', file=f)

