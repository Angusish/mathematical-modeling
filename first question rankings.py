import pandas as pd

df = pd.read_excel("./问题一结果排名.xlsx", sheet_name="ghl")


def pdlb(a):
    if a == "A":
        return 0.6
    elif a == 'B':
        return 0.66
    else:
        return 0.72


all = 0
i = 1
for index, row in df.iterrows():
    rate = pdlb(row['材料分类'])
    i += 1
    all += row['平均供货量'] / rate
    print(all)
    if all >= 28200:
        print(df['供应商id'][index])
        break

    all = 0
i = 1
for index, row in df.iterrows():
    rate = pdlb(row['材料分类'])

    i += 1
    all += row['平均供货量'] / rate
    # print(all)
    if i > 27:
        print(all)
        break