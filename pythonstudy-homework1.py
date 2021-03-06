# encoding:utf-8

import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

dic = {} # 建立一个字典存储匹配成功的词语,通过键值对的方式成为计数器
items = []  # 建立元组,返回的是由元组组成的列表,每个元组包含一对键值对

resultpath = '/home/elaine/Desktop/树蛙/作业/result.txt' # 用filepath代替结果文件的路径

def buildkey(pathofdict):  # 定义buildkey这个函数(方法),用于將词典的文件中的词语作为键保存在元组中
    with codecs.open(pathofdict, 'r', 'utf-8') as file:  # 第一个参数是文件,'r'表示读文件
        for line in file.readlines():
            line = line.strip('\n')  # 调用strip方法可以將文本中的\n去掉
            items.append((line, 0))
            # append是追加的方法
    # 用with open的方式读取文件更加简洁:不必写try...和finally...语句处理异常,也不用调用close()方法

# 统计"主题"关注度
buildkey('/home/elaine/Desktop/树蛙/作业/词典/主题/主题.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/主题/题材内容.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/主题/风格.txt')

# 统计"制作"关注度
buildkey('/home/elaine/Desktop/树蛙/作业/词典/制作/制作.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/制作/出品公司.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/制作/导演.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/制作/编剧.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/制作/选景.txt')

# 统计"剧情"关注度
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/剧情.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/发展.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/开头.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/泪点.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/笑点.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/剧情/结局.txt')

# 统计"视听"关注度
buildkey('/home/elaine/Desktop/树蛙/作业/词典/视听/视听.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/视听/动作.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/视听/画面.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/视听/镜头.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/视听/音乐.txt')

# 统计"角色"关注度
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/角色.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/反派.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/男主角.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/女主角.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/配角.txt')
buildkey('/home/elaine/Desktop/树蛙/作业/词典/角色/角色中的其他.txt')

line_ = "" # line_用于保存太空旅客.txt中去掉\n后的字符串

with codecs.open('/home/elaine/Desktop/树蛙/作业/太空旅客.txt', 'r', 'utf-8') as file:
    for line in file.readlines():
        line = line.strip('\n')
        line_ = line_ + line

dic = dict(items)

for line in line_:
    if line in dic:
        dic[line]+=1

with codecs.open(resultpath, 'a', 'utf-8') as file:  # 'a'表示在filepath代表的文件中
    for line in dic:
        output = line + str(dic[line]) + '\n'
        file.write(output)