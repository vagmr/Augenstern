import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout

class IPInfo(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化窗口
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('IP地址查询')
        self.resize(650, 350)

        # 创建一个垂直布局，并将其设置为该窗口的主布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加一个文本编辑框用于显示 IP 地址信息
        self.ip_info_text = QTextEdit()
        self.ip_info_text.setFixedWidth(650)
        self.ip_info_text.setTabChangesFocus(True)
        self.ip_info_text.setReadOnly(True)
        layout.addWidget(self.ip_info_text)

        # 添加两个按钮元素，一个用于查询 IP 地址信息，另一个用于退出程序
        self.query_button = QPushButton('查询')
        self.query_button.clicked.connect(self.query_ip_info)
        layout.addWidget(self.query_button)

        self.quit_button = QPushButton('退出')
        self.quit_button.clicked.connect(self.quit_app)
        layout.addWidget(self.quit_button)

    def query_ip_info(self):
        # 获取公共 IP 地址
        url = 'https://api.ipify.org/?format=json'
        response = requests.get(url)
        data = response.json()
        ip_address = data['ip']

        # 查询 IP 地址信息，并将结果显示在文本编辑框中
        try:
            url = f'https://ipapi.co/{ip_address}/json/'
            response = requests.get(url)
            data = response.json()
            country = data['country_name']
            self.ip_info_text.setText(f'IP地址：{ip_address}，所在国家：【{country}】\n其它信息：{data}')
        except:
            self.ip_info_text.setText(f'IP地址：{ip_address}，查询失败')

    def quit_app(self):
        # 退出程序
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ip_info = IPInfo()
    ip_info.show()
    sys.exit(app.exec_())
