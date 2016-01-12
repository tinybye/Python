# Python
Python learning notes

# 第0000题：
题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
思路：其实就是对图片的简单操作，首先是需要从PIL导入Image, ImageDraw, ImageFont。
本题包含的知识点：
1、The ImageDraw Module 创建绘画对象，使用ImageDraw.Draw方法创建。使用了基本绘画操作的添加文字，方法为text((x,y),message,fill,font)，每个参数对应的是添加文字的坐标、文字、颜色、字体
2、矢量字体支持 TrueType Font support 使用ImageFont.truetype(font,size)方法,每个参数对应的是字体的名称和字号。

# 第0001题
题目：作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成200个激活码（或者优惠券）
思路：通过使用随机数来生成激活码。
本题包含的知识点：
random模块。本例中使用了random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限。

# 第0004题
ps.前面的两道题都是对数据库的操作先不管了。。。
题目：任一个英文的纯文本文件，统计其中的单词出现的个数。
思路：首先读取文件，之后使用正则表达式来判断单词的个数。
本题包含的知识点：
1、文件读取与写入。读取文件：f = open(filepath, 'r') 两个参数分别为传入文件名和标识符。读文件时标识符为'r'，写文件时标识符为'w'。f.read() 读文件，f.write('hehe') 写文件，f.close() 关闭文件。关闭文件以免数据丢失。
2、正则表达式。本例使用了re.findall(pattern, string[, flags]) 以列表的形式返回能匹配的子串。第一个参数为要匹配的字符，第二个参数是被匹配的字符串。r前缀不用考虑转义字符的问题，例如：s = r'ABC\-001'。

# 第0005题
