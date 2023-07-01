import sys
import requests
import json
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QColor, QPainter, QPalette, QIcon
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEvent, pyqtSignal, QPoint,QEasingCurve
import os




def generate_sign(appid, q, salt, secret_key):
    sign_str = f"{appid}{q}{salt}{secret_key}"
    md5 = hashlib.md5()
    md5.update(sign_str.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

class StyledLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(100)
        self.setPlaceholderText("请输入要翻译的文本")
        self.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 18px;
                color: #333;
                background-color: #F0F0F0;
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.OutBack)

        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self and event.type() == QEvent.HoverEnter:
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(self.geometry().adjusted(-5, -5, 5, 5))
            self.animation.start()
        elif obj == self and event.type() == QEvent.HoverLeave:
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(self.geometry().adjusted(5, 5, -5, -5))
            self.animation.start()

        return super().eventFilter(obj, event)

class StyledButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 14px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: #FFF;
                border-radius: 10px;
            }
        """)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.OutBack)

        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self and event.type() == QEvent.HoverEnter:
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(self.geometry().adjusted(-5, -5, 5, 5))
            self.animation.start()
        elif obj == self and event.type() == QEvent.HoverLeave:
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(self.geometry().adjusted(5, 5, -5, -5))
            self.animation.start()

        return super().eventFilter(obj, event)

class TranslationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("翻译应用")
        # 获取当前文件所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建图标文件的绝对路径
        icon_path = os.path.join(current_dir, "res", "ip.png")

        # 设置窗口图标
        self.setWindowIcon(QIcon(icon_path))
        # self.setWindowIcon(QIcon("res/ip.png"))

        layout = QVBoxLayout()

        label = QLabel("请输入要翻译的文本：")
        label.setFont(QFont("Arial", 14))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.text_input = StyledLineEdit()
        layout.addWidget(self.text_input)

        self.translate_button = StyledButton("翻译")
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
            QTextEdit {
                font-family: Arial;
                font-size: 16px;
                color: #333;
                background-color: #F0F0F0;
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.output_text)

        save_button = StyledButton("保存为JSON")
        save_button.clicked.connect(self.save_json)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def translate_text(self):
        text = self.text_input.text().strip()
        if text:
            appid = "20210103000662299"
            salt = "123456vagmr"

            secret_key = "4Nw0vyG4eA5iZUig4GTn"
            sign = generate_sign(appid, text, salt, secret_key)

            api_url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
            target_lang = "en"
            params = {
                "q": text,
                "from": "zh",
                "to": target_lang,
                "appid": appid,
                "salt": salt,
                "sign": sign
            }

            response = requests.get(api_url, params=params)
            translation = json.loads(response.text)
            translated_text = translation["trans_result"][0]["dst"]

            self.output_text.setText(translated_text)
        else:
            QMessageBox.warning(self, "错误", "请输入要翻译的文本。")

    def save_json(self):
        if self.output_text.toPlainText():
            reply = QMessageBox.question(self, "保存确认", "是否保存翻译结果为JSON文件？", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                filename, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "JSON 文件 (*.json)")
                if filename:
                    output_data = {
                        "source_text": self.text_input.text(),
                        "translated_text": self.output_text.toPlainText(),
                        "target_lang": "en"
                    }
                    with open(filename, "w", encoding="utf-8") as file:
                        json.dump(output_data, file, ensure_ascii=False)
                    QMessageBox.information(self, "保存成功", "翻译结果已保存到文件中。")
        else:
            QMessageBox.warning(self, "错误", "没有可保存的翻译结果。")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranslationWidget()
    window.show()
    sys.exit(app.exec_())
