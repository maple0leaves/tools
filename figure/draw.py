import matplotlib.pyplot as plt
# 设置字体格式
from matplotlib import rcParams
import matplotlib.patches as patches

size = 12  # 全局字体大小
# 设置英文字体
config = {
    "font.family": 'serif',
    "font.size": size,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}
rcParams.update(config)
# 设置中文宋体
fontcn = {'family': 'SimSun', 'size': size}
label_size = size
text_size = size
# 数据
mAP = [48.6, 46.8, 47.8, 47, 46.3,47.8]
param = [36.5, 36.5, 21.0, 46.6, 18.5,34.8]
param2 = [i * 30 for i in param]
FPS = [72.2,89.2, 67.5, 59, 75,46.6]

# 绘制参数量标准
param_legend = [15,25,35,45,55]
param_legend = [i * 30 for i in param_legend]
param_x = [43.5,49, 55, 62, 70]
param_y = [44.6, 44.6, 44.6, 44.6, 44.6]
param_color = [(0.45, 0.45, 0.45)] * 5
param_text = ['5M', '20M', '35M', '50M', '65M']

# 参数设置
lw = 2
ms = 15
my_text = ['SC-YOLOv7(ours)', 'YOLOv7', 'YOLOv5m',
           'YOLOv5l', 'YOLOv6n','YOLOv6m']
my_text2 = '-S'
# color = ['C8', 'C1', 'C0', 'C6', 'C4', 'C9', 'b', 'r']
color = ['r', 'C1', 'C0', 'C6', 'C4','C9']

# 绘制 mAP-Param
plt.figure()
plt.scatter(FPS, mAP, s=param2, color=color, alpha=0.6)
plt.scatter(param_x, param_y, s=param_legend, color=param_color, alpha=0.2)

# 绘制矩形框
ax = plt.gca()
rect = patches.Rectangle(xy=(41, 44.1), width=33, height=1.5,
                         linewidth=0.5, linestyle='-', fill=False, edgecolor='gray')
ax.add_patch(rect)

# 添加数学公式标签
# plt.ylabel('$M_\mathrm{mAP}$ (%)', fontsize=label_size)
# plt.xlabel('$N_\mathrm{FPS}$ (Frame/s)', fontsize=label_size)
plt.ylabel('$\mathrm{mAP.5:.95}$ (%)', fontsize=label_size)
plt.xlabel('$\mathrm{FPS}$ (Frame/s)', fontsize=label_size)
# plt.xlim([-20, 200])
# plt.ylim([30, 52.5])
plt.xlim([40, 100])
plt.ylim([44, 49.5])

# 添加方法名
plt.text(FPS[0] - 7, mAP[0] + 0.5, my_text[0], color="b", fontsize=text_size)
plt.text(FPS[1]-4, mAP[1]+0.5, my_text[1], color="k", fontsize=text_size)
plt.text(FPS[2]-5, mAP[2] + 0.4, my_text[2], color="k", fontsize=text_size)
plt.text(FPS[3]-5, mAP[3]+0.5, my_text[3], color="k", fontsize=text_size)
plt.text(FPS[4]-3, mAP[4] +0.5, my_text[4], color="k", fontsize=text_size)
plt.text(FPS[5] - 5, mAP[5] + 0.5, my_text[5], color="k", fontsize=text_size)
#
# plt.text(FPS[6] - 9, mAP[6] + 0.8, my_text[6], color="k", fontdict=fontcn)
# plt.text(FPS[6] + 4.5, mAP[6] + 0.8, my_text2, color="k", fontsize=text_size)
#
# plt.text(FPS[7] - 9, mAP[7] + 0.8, my_text[7], color="k", fontdict=fontcn)
# plt.text(FPS[7] + 4.5, mAP[7] + 0.8, my_text2, color="k", fontsize=text_size)

# 添加参数量标准大小
plt.text(param_x[0]-1.5, 45.2, param_text[0], color="k", fontsize=text_size)
plt.text(param_x[1]-2, 45.2, param_text[1], color="k", fontsize=text_size)
plt.text(param_x[2]-2, 45.2, param_text[2], color="k", fontsize=text_size)
plt.text(param_x[3]-2, 45.2, param_text[3], color="k", fontsize=text_size)
plt.text(param_x[4]-2, 45.2, param_text[4], color="k", fontsize=text_size)
plt.grid(linestyle='--')
plt.show()
