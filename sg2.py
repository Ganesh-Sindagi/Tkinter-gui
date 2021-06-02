import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xlrd


def auto_label(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90, size=8)


df = pd.read_excel(r"C:\Users\Ganesh Sindagi\Downloads\graphs.xlsx", sheet_name=[0, 1, 2])
xls = xlrd.open_workbook(r"C:\Users\Ganesh Sindagi\Downloads\graphs.xlsx", on_demand=True)
sn = xls.sheet_names()
print(sn)

for i in df:
    x = df[i]['USER']
    lw = df[i]['LW']
    cw = df[i]['CW']

    x_val = []
    lw_val = []
    cw_val = []

    for user in x:
        x_val.append(user)

    for size in lw:
        lw_val.append(round(size, 2))

    for size in cw:
        cw_val.append(round(size, 2))

    labels = x

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects_1 = ax.bar(x - width/2, lw_val, width, label='Last Week')
    rects_2 = ax.bar(x + width/2, cw_val, width, label='Current Week')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Size of Usage(GB)')
    ax.set_title(sn[i] + ' Shared drive usage')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    ax.legend()

    auto_label(rects_1)
    auto_label(rects_2)

    fig.tight_layout()
    img_path = "C:\\Users\\Ganesh Sindagi\\Desktop\\" + sn[i] + "_graph.png"
    plt.savefig(img_path)
    plt.show()
