#!/usr/local/bin/python3.7

# 总共打印的行数目
end = input('小老弟你想输出多少行呢？')
end = int(end)

ans = [[] for i in range(end)]

# 横向元素的赋值
for i in range(end-1, -1, -1):
    value = i + 1
    for j in range(i+1):
        temp = value * value - j
        ans[i].append(temp)

# 纵向元素赋值
for i in range(1, end):
    for j in range(i - 1, -1, -1):
        minus = i - j
        ans[j].append(ans[i][i] - minus)

for i in range(0, end):
    for j in range(0, end):
        print(ans[i][j], '\t', end='')
    print('')
    print('')
    print('')
    print('')
