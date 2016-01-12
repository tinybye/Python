from random import Random

def code(number, codeLength = 8):
    #生成输出优惠券的文件
    codeFile = open('codes.txt', 'w')
    if number <= 0:
        return 'invalid number of codes'
    else:
        #提供每次随机生成的字符
        chars = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
        random = Random()
        #range生成范围内的整数list
        for j in range(1, number+1):
            str = ''
            for i in range(1, codeLength+1):
                #生成随机数选择一个字符
                index = random.randint(1, len(chars))
                str = str + chars[index-1]
            codeFile.write(str+'\n')
        return 'successful'
print(code(200))

