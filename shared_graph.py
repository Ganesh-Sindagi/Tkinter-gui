import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\Ganesh Sindagi\Downloads\graphs.xlsx", sheet_name=[0, 1, 2])
x = df[2]['USER']
lw = df[2]['LW']
cw = df[2]['CW']

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
rects1 = ax.bar(x - width/2, lw_val, width, label='Last Week')
rects2 = ax.bar(x + width/2, cw_val, width, label='Current Week')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Size of Usage(GB)')
ax.set_title('ozd1132w Shared drive usage')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=90)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=90,size=8)


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.savefig(r'C:\Users\Ganesh Sindagi\Desktop\plot.png')
plt.show()