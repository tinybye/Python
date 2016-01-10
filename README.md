# Python
Python learning notes

# 第0000题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
其实就是对图片的简单操作，首先是需要从PIL导入Image, ImageDraw, ImageFont。
具体每一步代码都有注释解释。本题包含的知识点有以下几点：
1、The ImageDraw Module 创建绘画对象，使用ImageDraw.Draw方法创建。使用了基本绘画操作的添加文字，方法为text((x,y),message,fill,font)，每个参数对应的是添加文字的坐标、文字、颜色、字体
2、矢量字体支持 TrueType Font support 使用ImageFont.truetype(font,size)方法,每个参数对应的是字体的名称和字号。

# 第0001题