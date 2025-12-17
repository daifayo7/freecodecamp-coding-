
# 创建一个密码提取函数
def pin_extractor(poems):
    # 创建一个空的列表 secret_codes
    secret_codes = [ ]


    # for 循环，遍历每一首诗歌 poem
    for poem in poems:
        print(poem)
        secret_code = ''

        # 将 poem 字符串 拆分成列表 list
        lines = poem.split('\n')
        # print(lines) # ['Stars and the moon', 'shine in the sky', 'white and bright', 'until the end of the night']


        # 提示：使用 for 循环，打印列表lines 的每一行的内容line
        for line_index,line in enumerate(lines): # 使用 enumerate() 枚举函数获取每一行的索引 index 和内容 line
            # print(line_index,line) # 打印每一行的索引index和内容line

        # 把每一行的字符串拆分成 单词列表
            words =line.split(' ')

            """现在函数在提取诗歌代码方面做得不错，但有个例外需要考虑：诗的行可能比预期短，这会导致函数出错（你可以尝试去除诗中的单词 bright）。
                Put the line secret_code += str(len(words[line_index])) in an if statement that checks that there are enough words in the words list.
                把这行 secret_code += str(len(words[line_index])) 放在一个 if 语句中，检查单词列表中是否有足够的单词。"""

            #单词长度必须＞索引值 index ： if 条件判断，检查单词列表 words 的长度是否大于 当前行的索引 line_index
            if len(words) > line_index:
                # 打印每一行中对应索引 index 的单词的长度 length
                # print(str(len(words[line_index])))# str : 把整数int 转换成字符串 str 类型以便拼接
                secret_code += str(len(words[line_index])) # 拼接每一行中对应索引 index 的单词的长度 length 到 secret_code 字符串中
            else:
                secret_code += '0' # 如果单词列表 words 的长度不够，就拼接 '0' 到 secret_code 字符串中

        secret_codes.append(secret_code) # 把提取到的密码 secret_code 添加到 列表 secret_codes 中
    return secret_codes # 返回 提取到的密码 列表 secret_codes
    # 注意缩进对齐


# poem 这个变量存放 诗歌内容
# 多行字符串:使用''' ''' 或者 """ """ 包含的字符串，可以跨越多行
poem = 'Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night'

# poem2
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

# poem3
poem3 = 'There\nonce\nwas\na\ndragon'

# 诗歌内容
# 变量 poems 存放 多首诗歌内容
poems = [poem,poem2,poem3]
print(poems)


if __name__ == '__main__':

    #调用提取密码的函数
    print(pin_extractor([poem, poem2, poem3]))