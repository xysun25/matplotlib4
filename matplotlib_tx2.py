from matplotlib import pyplot as plt
import matplotlib

# 中文字体
font = {'family':'MicroSoft YaHei',
        'weight':'bold',
        'size':12}
matplotlib.rc("font",**font)
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold",size=8)

a = ["战狼2","速度与激情9","功夫熊猫","西游降魔篇","变形金刚5：\n最后的战士","摔跤吧！爸爸","加勒比海盗5：\n死无对证"]
b = [56.01,26.94,17.53,16.49,12.96,11.8,6.88]

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# bar绘制条形图，只能接受含数字的可迭代对象
# width表示长条的宽度，默认0.8
plt.barh(range(len(a)),b,height=0.1,color="orange")

# 设置x轴刻度，将字符串传入x轴
plt.yticks(range(len(a)),a)

# 添加网格
plt.grid(alpha=0.3)

# 保存图片
plt.savefig("./movie.png")
plt.show()

