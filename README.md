# Python-Study
# 作业思路:
# 1.读取词典中的文件
# 2.將词典文件中的词语作为字典的键存储
# 3.字符串匹配:若太空旅客.txt中的文字成功于字典中的键匹配,则该键所对应的值+1
# 4.將字典中的键值对打印到result.txt文件中

# encoding:utf-8

import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

dic = {} # 建立一个字典存储匹配成功的词语,通过键值对的方式成为计数器
items = []  # 建立元组,返回的是由元组组成的列表,每个元组包含一对键值对

filepath = '/home/elaine/Desktop/树蛙/作业/result.txt' # 用filepath代替结果文件的路径

# 统计"主题"关注度
with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/主题/主题.txt', 'r', 'utf-8') as file:  # 第一个参数是文件,'r'表示读文件,第三个参数表示采用utf-8编码
    for line in file.readlines():
        line = line.strip('\n')  # 调用scrip方法可以將文本中的\n去掉
        items.append((line, 0))
         # append是追加的方法,將匹配到的词语作为键追加到dict中,并将对应的值赋为0

    # 用with open的方式读取文件更加简洁:不必写try...和finally...语句处理异常,也不用调用close()方法

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/主题/题材内容.txt', 'r', 'utf-8' ) as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/主题/风格.txt', 'r' , 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

# 统计"制作"关注度
with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/制作/制作.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/制作/出品公司.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/制作/导演.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/制作/编剧.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/制作/选景.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

# 统计"剧情"关注度
with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/剧情.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/发展.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/开头.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/泪点.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/笑点.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/剧情/结局.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

# 统计"视听"关注度
with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/视听.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/动作.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/画面.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

# with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/试听效果中的其他.txt', 'r', 'utf-8') as file:
#     for line in file.readlines():
#         line = line.strip('\n')
#         items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/镜头.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/视听/音乐.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

# 统计"角色"关注度
with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/角色.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/反派.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/男主角.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/女主角.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/配角.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

with codecs.open('/home/elaine/Desktop/树蛙/作业/词典/角色/角色中的其他.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        items.append((line, 0))

line_ = "" # line_用于保存太空旅客.txt中去掉\n后的字符串

with codecs.open('/home/elaine/Desktop/树蛙/作业/太空旅客.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        line_ = line_ + line

dic = dict(items)

for line in line_:
    if line in dic:
        dic[line]+=1

with codecs.open(filepath, 'a', 'utf-8') as file:  # 'a'表示在filepath代表的文件中
    for line in dic:
        output = line + str(dic[line]) + '\n'
        file.write(output)




