import jieba
import math
import time
import re
import sys
import argparse
from jieba import analyse
from gensim import corpora, models, similarities

# 全局变量
time_start = 0
time_end = 0
time_last = 0  # 测试运行时间
total_size = 0  # 文章总长度
ans = 0
sim_value = []  # 记录相似值
word_lenth = []  # 记录每句长度
origin_txt = []
origin_add_txt = []


# 将文章进行拆分成句子
def Split_sentence(file_txt):
    head = '\u4e00'
    tail = '\u9fff'
    word = ""
    sentence_list = []  # 保存拆分的句子
    for each in range(len(file_txt)):
        if head <= file_txt[each] <= tail:  # 中文编码范围
            word += file_txt[each]
        elif file_txt[each] == "，":  # 以逗号分句
            sentence_list.append(word)
            word = ""
        else:
            continue

    if word != '':
        sentence_list.append(word)
        word = ''

    return sentence_list


if __name__ == '__main__':
    time_start = time.time()

    # sys.argv[1] 论文原文的文件的绝对路径
    # sys.argv[2] 抄袭版论文的文件的绝对路径
    # sys.argv[3] 输出的答案文件的绝对路径

    # 读入初始文件
    file = open(sys.argv[1], 'r', encoding='UTF-8')
    origin_file = file.read()
    file.close()
    origin_txt = Split_sentence(origin_file)  # 初始文件分句


    # 读入相似文件
    file = open(sys.argv[2], 'r', encoding='UTF-8')
    origin_add_file = file.read()
    file.close()
    origin_add_txt = Split_sentence(origin_add_file)  # 相似文件分句

    # 计算每句相似度 以及 每句长度
    # 利用jieba.luct进行分词 保存在list列表中
    ori_list = [[word for word in jieba.lcut(sentence)] for sentence in origin_txt]
    # print(ori_list)

    ori_add_list = [[word for word in jieba.lcut(sentence)] for sentence in origin_add_txt]
    # print(ori_add_list)

    # 生成词典
    dictionary = corpora.Dictionary(ori_list)

    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(word) for word in ori_list]

    # 通过TF模型算法，计算出tf值
    tf = models.TfidfModel(corpus)

    # 通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())

    # 计算稀疏矩阵相似度，建立索引
    index = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)

    # 每句长度-单个变量
    word_size = 0
    sim = 0
    for word in range(len(ori_add_list)):
        # 新的稀疏向量
        new_vector = dictionary.doc2bow(ori_add_list[word])
        # 算出相似度
        sim_list = index[tf[new_vector]]
        # 选出最大相似度
        sim = max(sim_list)
        # 加入相似度列表
        sim_value.append(sim)
        # 相似文章每句长度值
        word_size = len(ori_add_list[word])
        # 总长度值
        total_size += word_size
        # 加入长度列表
        word_lenth.append(word_size)

    total_sum = 0
    for i in range(0, len(word_lenth)):
        total_sum += word_lenth[i] * sim_value[i]

    # 加权求平均
    ans = total_sum / total_size
    # 保留后两位
    ans = (str("%.2f") % ans)

    # print(ans)
    # 写入文件
    file = open(sys.argv[3], 'w', encoding='UTF-8')
    file.write(ans)
    file.close()

    time_end = time.time()
    time_last = time_end - time_start
    # print(time_last)
