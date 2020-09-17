import jieba
import re
import sys
from jieba import analyse
from gensim import corpora, models, similarities

# 计算相似度
def Split_sentence(file_txt):
    head = '\u4e00'
    tail = '\u9fa5'
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

def Calculation_Similiarity(origin_txt,origin_add_txt):
    sim_value = []
    word_lenth = []
    total_sum = 0
    total_size = 0
    # 利用jieba.luct进行分词 保存在list列表中
    ori_list = [[word for word in jieba.lcut(sentence)] for sentence in origin_txt]

    ori_add_list = [[word for word in jieba.lcut(sentence)] for sentence in origin_add_txt]

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
    size = 0
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
        # 文章总长度值
        size += word_size
        # 加入长度列表
        word_lenth.append(word_size)

    total_size = size

    for i in range(len(word_lenth)):
        total_sum += word_lenth[i] * sim_value[i]

    # 加权求平均
    ans = total_sum / total_size

    return ans
