# new_list = [表达式 for 变量 in 可迭代对象 if 条件]


# 1.0-20的之间的偶数列表
# 设置一个空的偶数列表 ，之后用来存放偶数元素
even_numbers = []
# for循环 依次打印出 0-20之间的偶数
for num in range(0, 21):
    # 如何判断是偶数呢？整除2 ，余数 == 0
    if num % 2 == 0:
        # 依次把打印出的偶数元素，添加到原始的空的列表even_numbers
        even_numbers.append(num)
print(even_numbers)

# 2.如何把上述的偶数列表 ➡️ 列表推导式的表达式
even_numbers = [num for num in range(0, 21) if num % 2 == 0]
print(even_numbers)




# 2. 判断 0-10 之间，哪些是偶数 even ，哪些是奇数odd
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num % 2 == 0:
        print(f'even:{num}')
    else:
        print(f'odd:{num}')


# 2.1 列表推导式
# 判断 0-20 之间，哪些是偶数 even ，哪些是奇数odd
numbers = range(21) # range 生成 0-20 之间的数字
result = [(num,'even') if num % 2 == 0  else (num,'odd') for num in numbers ]
print(result)








# filter函数的使用
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
# 提取中间大于 4 的单词
# 定义一个函数，判断单词是否大于 4
def long_words(word):
    return len(word) > 4

# 使用filter函数，筛选单词大于 4 的元素
result1 = list(filter(long_words, words))
print(result1)




# map函数的使用
# 将摄氏度 ➡️ 华氏度
celsius = [0, 10, 20, 30, 40]
# 定义一个函数，把摄氏度转换成华氏度
def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

result2 = list(map(to_fahrenheit, celsius))
print(result2)




# sum函数
numbers = [5, 10, 15, 20]
sum1 = sum(numbers) # 默认起始值=0
print(sum1)    # 50


sum2 = sum(numbers,5) #起始值= 5
print(sum2)   # 55
sum3 = sum(numbers,start = 10)# 起始值是 10
print(sum3)  # 60