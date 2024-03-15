# Section11

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter="|")
    # next(reader) # Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제3
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # next(reader) # Header 스킵

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('------------')

# 예제 4
w = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
    [10,11,12,],
]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제 5
import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx', engine='openpyxl')

print(xlsx.head())
print()

print(xlsx.tail())
print()

print(xlsx.shape)

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
