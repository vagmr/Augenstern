import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 生成100个标准高斯分布的数组
import numpy as np
x = np.random.randn(100)

# 定义函数f(x) = 0.5*x^2
def f(x):
  return 0.5 * x**2

# 创建数据df
df = pd.DataFrame(np.random.rand(100,3), columns = ['a','b','c'])

# 创建数据s
s = pd.Series(0.5*np.linspace(0,10,100)+np.random.randn(100),index = np.linspace(0,10,100))

# 建立画布，设置大小为12*12，分为2*2的四个子图
plt.figure(figsize=(12,12))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# 在第一个子图上绘制直方图和密度曲线，设置X轴区间为(-5,5)
plt.subplot(2,2,1)
sns.histplot(x, kde=True)
plt.xlim(-5,5)
plt.title("Histogram and Density Curve")

# 在第二个子图上绘制函数f(x)的曲线图，设置X轴区间为(-5,5)，颜色为蓝色
plt.subplot(2,2,2)
x = np.linspace(-5,5,100)
y = f(x)
plt.plot(x,y,color="blue")
plt.title("Function Plot")

# 在第三个子图上绘制df各列的相关系数热图，使用默认的颜色映射
plt.subplot(2,2,3)
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")

# 在第四个子图上绘制s的散点图和回归线，使用默认的颜色和样式
plt.subplot(2,2,4)
sns.regplot(x=s.index,y=s)
plt.title("Scatter Plot and Regression Line")

# 显示所有图形
plt.show()