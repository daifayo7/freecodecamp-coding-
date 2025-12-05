"""
Build an RPG Character  创建角色扮演游戏角色
In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.
在本实验中，你将通过构建一个为角色扮演游戏冒险创建角色的小型应用程序来练习 Python 的基础知识。

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
目标： 完成以下用户故事，并通过所有测试以完成实验。

User Stories:  用户故事：

You should have a function named create_character.
你应该有一个名为 create_character 函数。
The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
该函数应按顺序接受角色名称，后跟三个属性：力量、智力和魅力。
The character name should be validated:
角色名称需要验证：
If the character name is not a string, the function should return The character name should be a string.
如果角色名称不是字符串，则该函数应返回 The character name should be a string 。
If the character name is longer than 10 characters, the function should return The character name is too long.
如果角色名称长度超过 10 个字符，则该函数应返回 The character name is too long 。
If the character name contains spaces, the function should return The character name should not contain spaces.
如果角色名称包含空格，则该函数应返回 The character name should not contain spaces 。
The stats should also be validated:
统计数据也需要进行验证：
If one or more stats are not integers, the function should return All stats should be integers.
如果一个或多个统计量不是整数，则该函数应返回 All stats should be integers 。
If one or more stats are less than 1, the function should return All stats should be no less than 1.
如果一个或多个统计量小于 1，则该函数应返回 All stats should be no less than 1 。
If one or more stats are more than 4, the function should return All stats should be no more than 4.
如果一个或多个统计量大于 4，则该函数应返回 All stats should be no more than 4 。
If the sum of all stats is different than 7, the function should return The character should start with 7 points.
如果所有统计量的总和不等于 7，则该函数应返回 The character should start with 7 points 。
If all values pass the verification, the function should return a string with four lines:
如果所有值都通过验证，则该函数应返回一个包含四行的字符串：
the first line should contain the character name
第一行应包含角色名称
lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
第 2-4 行应以属性缩写 STR 、 INT 或 CHA （按此顺序）开头，然后是一个空格，接着是与属性值相等的实心圆点 ( ● )，最后是使总数达到 10 的空心圆点 ( ○ )。例如：如果力量值为 3，则必须有 3 个实心圆点和 7 个空心圆点。圆点数量在编辑器中已设置好。
Here's the string create_character("ren", 4, 2, 1) should return:
字符串 create_character("ren", 4, 2, 1) 应该返回以下结果：

ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
NOTE: while str and int are common abbreviations for the stats, remember that those are reserved keywords in Python and should not be used as variable names.
注意：虽然 str 和 int 是统计信息的常用缩写，但请记住，它们是 Python 中的保留关键字，不应该用作变量名。

Run the Tests (Ctrl + Enter)
运行测试（Ctrl + Enter）
Reset this lesson  重置本课程
Get Help
  获取帮助
Tests  测试
Waiting:1. You should have a function named create_character.
1. 你应该有一个名为 create_character 函数。
Waiting:2. When create_character is called with a first argument that is not a string it should return The character name should be a string.
2. 当 create_character 被调用时，如果第一个参数不是字符串，则应返回 The character name should be a string 。
Waiting:3. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.
3. 当 create_character 函数的第一个参数长度超过 10 个字符时，它应该返回 The character name is too long 。
Waiting:4. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.
4. 当使用第一个参数包含空格来调用 create_character 时，它应该返回 The character name should not contain spaces 。
Waiting:5. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.
5. 当 create_character 被调用时，如果第二个、第三个或第四个参数不是整数，则应返回 All stats should be integers 。
Waiting:6. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.
6. 当使用小于 1 第二个、第三个或第四个参数调用 create_character 时，它应该返回 All stats should be no less than 1 。
Waiting:7. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.
7. 当使用大于 4 第二个、第三个或第四个参数调用 create_character 时，它应该返回 All stats should be no more than 4 。
Waiting:8. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.
8. 当使用第二个、第三个或第四个参数调用 create_character 时，如果这些参数的总和不为 7 ，则应返回 The character should start with 7 points 。
Waiting:9. create_character("ren", 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
9. create_character("ren", 4, 2, 1) 应该返回 ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○ 。
Waiting:10. When create_character is called with valid values it should output the character stats as required.
10. 当使用有效值调用 create_character 时，它应该按要求输出角色属性。
"""

full_dot = '●'
empty_dot = '○'
# 导入1～10之间的随机数
# import random
# full_num = random.randint(1, 10)       # ● 的数量,用每个属性的值代替，strength,intelligence,charisma
# empty_num = 10 - full_num              # ○ 的数量

# 1.定义一个 创建角色的函数
def create_character(name,strength,intelligence,charisma):
    # 2.角色的名称字符串验证
    # 2.1 不是 not 字符串
    if not isinstance(name,str):
        return 'The character name should be a string' # 报错
    # 2.2 名称name的长度 大于 10个字符串
    if len(name) > 10:
        return 'The character name is too long'
    # 2.3 包含 空格
    if ' ' in name:
        return 'The character name should not contain spaces'

    # 3.统计数据的验证
    # 3.1 必须为整数
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return 'All stats should be integers'
    # 3.2 小于 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    # 3.3 大于 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    # 3.4 统计量的总和不等于 7
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    # 4.通过验证后，第一行返回包含角色名称的字符串name
    # 4.1 第 2-4 行应以属性缩写 STR 、 INT 或 CHA （按此顺序）开头，然后是一个空格，
    # 接着是与属性值相等的实心圆点 ( ● )，最后是使总数达到 10 的空心圆点 ( ○ )。
    # return name + "\n" + strength + "\n" +  intelligence + "\n" + charisma
    sec_column = "STR" + ' ' + strength * full_dot  + (10 - strength) * empty_dot
    third_column = "INT" + ' ' + intelligence * full_dot  + (10 - intelligence) * empty_dot
    forth_column = "CHA" + ' ' + charisma * full_dot  + (10 - charisma) * empty_dot
    return name + "\n" + sec_column + "\n" +  third_column + "\n" + forth_column




if __name__ == '__main__':

    print(create_character("simonwolf",3,1,3))