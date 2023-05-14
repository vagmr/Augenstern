from selenium import webdriver
import time

# url = "https://xgo.vagmrgpt.top/zh"

# 设置Edge浏览器无界面模式
options = webdriver.EdgeOptions()
options.headless = True

# 启动Edge浏览器
driver = webdriver.Edge(options=options)

# 访问网页并等待加载完成
# driver.get(url)
time.sleep(5) # 等待5秒钟，视网速和网站性能而定

# 获取完整页面源码
source_code = driver.page_source

# 关闭浏览器
driver.quit()

print(source_code)
