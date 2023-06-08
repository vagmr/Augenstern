import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMenuBar, QMenu, QAction, QMessageBox, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon


class IPInfo(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化窗口
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('IP地址查询')
        self.resize(650, 350)
        self.center()

        # 设置窗口图标
        self.setWindowIcon(QIcon('ip.png'))

        # 创建一个垂直布局，并将其设置为该窗口的主布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加一个菜单栏
        self.create_menu_bar()

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

        # 修改样式
        self.setStyleSheet('''
            QWidget{
                background-color: #f5f6fa;
            }

            QTextEdit{
                background-color: #ffffff;
                border: 1px solid #dcdde1;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
                font-family:微软雅黑 ;
            }

            QPushButton{
                background-color: #3498db;
                border: 1px solid #3498db;
                border-radius: 5px;
                color: #ffffff;
                font-size: 14px;
                padding: 10px;
            }

            QPushButton:hover{
                background-color: #2980b9;
                border: 1px solid #2980b9;
            }
        ''')

    def center(self):
        # 居中显示窗口
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create_menu_bar(self):
        # 创建菜单栏
        menu_bar = QMenuBar(self)

        # 创建“文件”菜单
        file_menu = QMenu('文件', self)
        menu_bar.addMenu(file_menu)

        # 创建“退出”菜单项
        quit_action = QAction('退出', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.triggered.connect(self.quit_app)
        file_menu.addAction(quit_action)

        # 创建“操作”菜单
        operation_menu = QMenu('操作', self)
        menu_bar.addMenu(operation_menu)

        # 创建“查询”菜单项
        query_action = QAction('查询', self)
        query_action.setShortcut('Ctrl+Enter')
        query_action.triggered.connect(self.query_ip_info)
        operation_menu.addAction(query_action)

        # 添加菜单栏到布局中
        layout = self.layout()
        layout.setMenuBar(menu_bar)

    def query_ip_info(self):
        # 查询 IP 地址信息，并将结果显示在文本编辑框中
        try:
            # 获取公共 IP 地址
            url = 'https://api.ipify.org/?format=json'
            response = requests.get(url)
            data = response.json()
            ip_address = data['ip']

            # 查询 IP 地址信息
            url = f'https://ipapi.co/{ip_address}/json/'
            response = requests.get(url)
            data = response.json()

            # 显示 IP 地址信息到文本编辑框
            country = data['country_name']
            self.ip_info_text.setText(f'IP地址：{ip_address}，所在国家：【{country}】\n其它信息：{data}')
        except:
            # 显示查询失败提示信息
            QMessageBox.warning(self, '查询失败', '查询 IP 地址信息失败，请检查网络连接。')

    def quit_app(self):
        # 退出程序
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ip_info = IPInfo()
    ip_info.show()
    sys.exit(app.exec_())
