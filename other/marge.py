import pandas as pd
import numpy as np

def student_grade():
    nd = np.empty((100,3))
    for j in range(3):
        for i in range(100):
            nd[i,j] = np.ceil(70+30*np.random.rand(1))
    for i in range(20):   #添加分数异常值
        nd[int(np.ceil(100*np.random.rand(1)))-1,int(np.ceil(3*np.random.rand(1)))-1] = int(np.ceil(100*np.random.rand(1)))
        
    for i in range(15):   #添加缺失值
        nd[int(np.ceil(100*np.random.rand(1)))-1,int(np.ceil(3*np.random.rand(1)))-1] = np.NaN
    return nd

def height_weight():
    nd = np.empty((100,2))
    for i in range(100):   #生成身高信息
        nd[i,0] = np.ceil(165+30*np.random.rand(1))
    for i in range(100):   #生成体重信息
        nd[i,1] = np.ceil(nd[i,0]/2.5 + 5*np.random.randn(1))
        
    for i in range(10):    #添加身高异常值
        nd[int(np.ceil(100*np.random.rand(1)))-1,0] = int(np.ceil(250*np.random.rand(1)))
    for i in range(20):    #添加体重异常值
        nd[int(np.ceil(100*np.random.rand(1)))-1,0] = int(np.ceil(120*np.random.rand(1)))
        
    for i in range(15):    #添加缺失值
        nd[int(np.ceil(100*np.random.rand(1)))-1,int(np.ceil(2*np.random.rand(1)))-1] = np.NaN
    return nd

df1 = pd.DataFrame(student_grade(),columns=['语文','数学','英语'])
df1.index.name = '学号'
df2 = pd.DataFrame(height_weight(),columns=['身高(cm)','体重(kg)'])
df2.index.name = '学号'

df = pd.merge(df1, df2, on='学号', how='outer')

# 处理缺失值
df.dropna(inplace=True)

# 处理异常值
df.loc[df['语文'] > 100, '语文'] = 100
df.loc[df['数学'] > 100, '数学'] = 100
df.loc[df['英语'] > 100, '英语'] = 100

df.loc[df['身高(cm)'] < 100, '身高(cm)'] = 100
df.loc[df['身高(cm)'] > 220, '身高(cm)'] = 220
df.loc[df['体重(kg)'] < 40, '体重(kg)'] = 40
df.loc[df['体重(kg)'] > 150, '体重(kg)'] = 150

print(df.head())
