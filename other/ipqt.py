import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMenuBar, QMenu, QAction, QLabel, QMessageBox, QDesktopWidget, QApplication, QHBoxLayout, QLineEdit

class IPInfo(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化窗口
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('IP地址查询')
        self.resize(650, 400)
        self.center()

        # 设置窗口图标
        # self.setWindowIcon(QIcon('ip.png'))

        # 创建一个垂直布局，并将其设置为该窗口的主布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加一个菜单栏
        self.create_menu_bar()

        # 添加一个标题标签元素
        title_label = QLabel('IP地址查询结果：')
        title_label.setStyleSheet('font-size: 18px; font-weight: bold;')
        layout.addWidget(title_label)

        # 添加一个文本编辑框用于显示 IP 地址信息
        self.ip_info_text = QTextEdit()
        self.ip_info_text.setFixedWidth(650)
        self.ip_info_text.setTabChangesFocus(True)
        self.ip_info_text.setReadOnly(True)
        layout.addWidget(self.ip_info_text)

        # 添加两个按钮元素，一个用于查询 IP 地址信息，另一个用于退出程序
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.query_button_default = QPushButton('默认配置查询')
        self.query_button_default.clicked.connect(self.query_default_ip_info)
        button_layout.addWidget(self.query_button_default)

        self.query_button_custom = QPushButton('自定义查询')
        self.query_button_custom.clicked.connect(self.query_custom_ip_info)
        button_layout.addWidget(self.query_button_custom)

        self.clear_button = QPushButton('清除')
        self.clear_button.clicked.connect(self.clear_text_edit)
        button_layout.addWidget(self.clear_button)

        self.quit_button = QPushButton('退出')
        self.quit_button.clicked.connect(self.quit_app)
        button_layout.addWidget(self.quit_button)

        # 添加地址输入框
        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        self.ip_address_label = QLabel("IP地址:")
        input_layout.addWidget(self.ip_address_label)

        self.ip_address_input = QLineEdit("")
        self.ip_address_input.setFixedWidth(200)
        self.ip_address_input.setPlaceholderText("请输入IP地址，例如：8.8.8.8")
        input_layout.addWidget(self.ip_address_input, 1)

        # 修改样式
        self.setStyleSheet('''
            QWidget{
                background-color:#e8e9b9;
            }   
            
            QPushButton:hover{
                background-color: transparent;
                border: 1px solid #3498db;
            }

            QLabel{
                padding-left: 10px;
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

            QLineEdit{
                background-color: #ffffff;
                border: 1px solid #dcdde1;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
                font-family:微软雅黑 ;
            }

            QLineEdit::focus{
                border: 1px solid #3498db;
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

        # 创建“默认配置查询”菜单项
        query_default_action = QAction('默认配置查询', self)
        query_default_action.setShortcut('Ctrl+D')
        query_default_action.triggered.connect(self.query_default_ip_info)
        operation_menu.addAction(query_default_action)

        # 创建“自定义查询”菜单项
        query_custom_action = QAction('自定义查询', self)
        query_custom_action.setShortcut('Ctrl+F')
        query_custom_action.triggered.connect(self.query_custom_ip_info)
        operation_menu.addAction(query_custom_action)

        # 添加菜单栏到布局中
        layout = self.layout()
        layout.setMenuBar(menu_bar)
        # 创建“关于”菜单项
        about_action = QAction('关于', self)
        about_action.triggered.connect(self.show_about_info)
        menu_bar.addAction(about_action)

        # 添加菜单栏到布局中
        layout = self.layout()
        layout.setMenuBar(menu_bar)

    def query_default_ip_info(self):
        # 使用默认配置查询 IP 地址信息，并将结果显示在文本编辑框中
        try:
            # 获取公共 IP 地址
            url = 'https://api.ipify.org/?format=json'
            response = requests.get(url)
            data = response.json()
            ip_address = data['ip']

            # 查询 IP 地址信息
            url = f'https://ipapi.co/{ip_address}/json/'
            response = requests.get(url, timeout=5)
            data = response.json()

            # 显示 IP 地址信息到文本编辑框
            country = data['country_name']
            self.ip_info_text.setText(f'IP地址：{ip_address}，所在国家：【{country}】\n其它信息：{data}')
        except requests.exceptions.Timeout:
            QMessageBox.warning(self, '查询失败', '请求超时，请检查网络连接。')
        except:
            # 显示查询失败提示信息
            QMessageBox.warning(self, '查询失败', '查询 IP 地址信息失败，请检查网络连接。')

    def query_custom_ip_info(self):
        # 使用自定义配置查询 IP 地址信息，并将结果显示在文本编辑框中
        try:
            ip_address = self.ip_address_input.text()

            if not ip_address:
                QMessageBox.warning(self, '点击错误', '必须输入IP地址才能进行查询')
            else:
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

    def clear_text_edit(self):
        # 清空文本编辑框中的内容
        self.ip_info_text.clear()

    def quit_app(self):
        # 退出程序
        QApplication.quit()
    def show_about_info(self):
    # 设置对话框样式
        style_sheet = '''
            QMessageBox{
            background-color: aqua;
            padding:5px 0;
        }
        QMessageBox QLabel{
            color: #000000;
            font-size: 18px;
        }
        QMessageBox QPushButton{
            background-color: #3498DB;
            color: #FFFFFF;
            border-radius: 5px;
            padding: 5px;
            font-size: 16px;
        }
        QMessageBox QPushButton:hover{
            background-color: #2980B9;
        }
    '''

    # 弹出对话框显示作者信息
        message_box = QMessageBox()
        message_box.setWindowTitle('关于')
        message_box.setText('本程序由vagmr开发。' +'\n' + 'version:1.1 '+'\n'+'增加了对请求超时的处理机制，修复了程序卡死的bug'
                          + '\n '+ '将是最后一次更新了 '  )
        message_box.setStyleSheet(style_sheet)
        message_box.addButton(QPushButton('确定'), QMessageBox.AcceptRole)
        message_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ip_info = IPInfo()
    ip_info.show()
    sys.exit(app.exec_())
