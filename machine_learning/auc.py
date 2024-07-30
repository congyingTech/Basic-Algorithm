# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 8:46 下午
# @Author  : Mohn
# @FileName: auc.py

import numpy as np

def calc_auc(y_labels, y_scores):
    f = list(zip(y_scores, y_labels))
    rank = [values2 for values1, values2 in sorted(f, key=lambda x: x[0])]
    rankList = [i + 1 for i in range(len(rank)) if rank[i] == 1]
    pos_cnt = np.sum(y_labels == 1)
    neg_cnt = np.sum(y_labels == 0)
    auc = (np.sum(rankList) - pos_cnt * (pos_cnt + 1) / 2) / (pos_cnt * neg_cnt)
    print(auc)


def get_score():
    # 随机生成100组label和score
    y_labels = np.zeros(100)
    y_scores = np.zeros(100)
    for i in range(100):
        y_labels[i] = np.random.choice([0, 1])
        y_scores[i] = np.random.random()
    return y_labels, y_scores


if __name__ == '__main__':
    y_labels, y_scores = get_score()
    # 调用sklearn中的方法计算AUC，与后面自己写的方法作对比
    print('sklearn AUC:', roc_auc_score(y_labels, y_scores))

