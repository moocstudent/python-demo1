import numpy as np
import matplotlib.pyplot as plt

# 我们使用numpy库生成横轴坐标，并使用matplotlib库绘制三角函数的图形。
# 我们计算了正弦、余弦和正切函数的值，并使用plt.plot()函数绘制了它们的
# 图形。最后，我们使用plt.legend()添加图例，使用plt.title()添加标题，
# 并使用plt.show()显示图形。

# 生成横轴坐标
x = np.linspace(-np.pi, np.pi, 200)

# 计算三角函数值
sine = np.sin(x)
cosine = np.cos(x)
tangent = np.tan(x)

# 绘制三角函数图形
plt.plot(x, sine, label='Sine')#正弦
plt.plot(x, cosine, label='Cosine')#余弦
plt.plot(x, tangent, label='Tangent')#正切

# 添加图例和标题
plt.legend()
plt.title('Trigonometric Functions')

# 显示图形
plt.show()