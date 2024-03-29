import pandas as pd
import numpy as np
#  提取四个特征


dhl = pd.read_excel("./1.1.xlsx", sheet_name=0)  # 订货量数据
ghl = pd.read_excel("./1.1.xlsx", sheet_name=1)  # 供货量数据


def pd_(a):
    if a == "A":
        return 0.6
    elif a == 'B':
        return 0.66
    else:
        return 0.72


m = []
for index, row in ghl.iterrows():
    all = 0
    cnt = 0
    for gh, dh in zip(row[2:], dhl.iloc[index][2:]):
        if dh == 0:
            continue
        cnt += 1
        all += gh
        # print(all)
    m.append(all / cnt)
    # print(all/cnt)
df = pd.DataFrame(m)
df['供应商ID'] = dhl['供应商ID']
df.to_csv("./mean.csv", encoding="utf_8_sig")


def count_rate(dh, gh):
    all = 0
    ok = 0
    no = 0
    for target, fact in zip(dh, gh):
        if target == 0:
            continue
        if fact >= target:
            ok += 1
        else:
            no += 1

        all += 1
    rate = ok / all
    return rate


gysid = ghl['供应商ID']
clfl = ghl["材料分类"]
max_ghl = []
mean_ghl = []
rates = []
cols = [x for i, x in enumerate(dhl.drop(['供应商ID', '材料分类'],axis=1).columns) if dhl.iat[0,i]!=0]
# print(cols)
for index, row in ghl.iterrows():
    max_ghl.append(row[2:].max())
    mean_ghl.append(row[cols].mean())
    rates.append(count_rate(dhl.iloc[index][2:], row[2:]))

df = pd.DataFrame({"供应商ID": gysid, "材料分类": clfl, "最大供货量": max_ghl, "平均供货量":mean_ghl,"订单完成率":rates})

df.to_excel("./特征.xlsx", encoding="utf_8_sig")   