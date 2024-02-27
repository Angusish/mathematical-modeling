import pandas as pd
import numpy as np

def G_R_E(df):
    n = list(df.columns)
    A1 = []
    for i in n:
        Max = np.max(df[i])
    A1.append(Max)

    A1 = np.array(A1)
    for i in n:
        df[i] = df[i] / np.average(df[i])
    m = len(df)
    for i in range(m):
        df[i:i + 1] = abs(df[i:i + 1] - A1)
        # 最大值
    MAX = []
    # 每个指标的最大值   
    for i in n:
        l = max(df[i])
        MAX.append(l)
    MAX = max(MAX)
    MIN = []
    for i in n:
        l = min(df[i])
        MIN.append(l)
    MIN = min(MIN)
    # 关联系数为0.5
    for i in n:
        df[i] = (MIN + 0.5 * MAX) / (df[i] + 0.5 * MAX)
    score = []
    for i in range(m):
        s = sum(df[i:i + 1].values[0]) / len(n)
        score.append(s)
    return score