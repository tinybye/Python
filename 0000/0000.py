from PIL import Image, ImageDraw, ImageFont

def add_num(num, fill, font_name):
    #打开图像文件
    im = Image.open('img.jpg')
    #获取图像的尺寸
    xsize , ysize = im.size
    #创建绘画对象
    draw = ImageDraw.Draw(im)
    #获取右上角需要显示的数字
    text = str(num)
    #创建Font对象
    font = ImageFont.truetype(font_name, xsize//3)
    #添加文字
    draw.text((ysize//5 * 4, 0), text, fill, font)
    #保存图像
    im.save("out.jpg")

num = 4
fill = (255, 0, 255)
font_name = "verdana.ttf"
add_num(num, fill, font_name)
