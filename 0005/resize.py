from PIL import Image
import glob

def reSize(dirPath, sizeX, sizeY):
    #遍历路径下的所有图片
    for file in glob.glob(dirPath + '*.jpg'):
        print (file)
        ori = Image.open(file)
        #重置大小
        modi = ori.resize((sizeX, sizeY))
        #保存并覆盖原文件
        modi.save(file)

reSize('img/', 640, 1733)
