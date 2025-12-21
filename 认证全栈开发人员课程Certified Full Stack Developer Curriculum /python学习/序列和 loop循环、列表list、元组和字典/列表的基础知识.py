'''
列表数据类型是一组 有序元素，可以由 字符串、数字，甚至其他列表组成。
类似于 JavaScript，列表是可变的，使用基于零的索引，意味着列表的第一个元素位于索引 0。
'''



cities = ['Los Angeles', 'London', 'Tokyo']
# 访问列表中的第一个元素
print(cities[0])  # 索引值从 0开始
print(cities[-1]) # 负索引值从 -1开始，表示最后一个元素


# 把字符串转换成列表
developer = "Jennifer"
new_list = list(developer)
print(new_list) # ['J', 'e', 'n', 'n', 'i', 'f', 'e', 'r']



# 计算列表的长度
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5


# 更新列表的内容
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[3] = "PHP"
print(programming_languages)  # ['Python', 'Java', 'C++', 'PHP

# 不能超出列表的长度 ：试图更新一个不存在的索引会引发错误indexerror
# programming_languages[100] = "PHP"  # IndexError: list assignment index out of range

# 删除列表中的元素
del programming_languages[1] # 删除第 2 个元素：index索引为 1 的元素（'Java'）
print(programming_languages) # ['Python', 'C++', 'PHP']


# 检查某个元素是否在列表中
print('python' in programming_languages)  # False，区分大小写,小写的就会变成 false
print('Python' in programming_languages)  # True



# 嵌套列表
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
# 访问嵌套列表中的元素：python
print(developer[2][0]) # Python #第一个[2]指外层列表的索引 index，第二个[0]是指内层列表的索引 index




# unpacking values
developer = ['Alice', 34, 'Rust Developer']
name, age , role = developer
print(name) # Alice
print(age) # 34
print(role) # Rust Developer

# 剩余的元素可以用*代替，代表一串元素
data = ['Alice', 34, 'Rust Developer', 'USA', 'Engineer']
age , *rust =data
print(age)
print(rust) #[34, 'Rust Developer', 'USA', 'Engineer']




# 切片（取左不取右）
numbers = [10, 20, 30, 40, 50, 60, 70]
#取第 2 和 3 的元素，索引值为 1 和 2
print(numbers[1:3])     #[20, 30]

numbers_1 = [1, 2, 3, 4, 5, 6]
# 取奇数
print(numbers_1[0::2]) # [1, 3, 5] ,【0】是起始值的索引，【2】是步长
# 取偶数
print(numbers_1[1::2]) #[2, 4, 6],【1】是起始值的索引，【2】是步长