import sys
import requests
import json
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QColor, QPainter, QPalette
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation

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

class TranslationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("翻译应用")
        self.setStyleSheet("""
            font-family: Arial;
            font-size: 12px;
            background-color: #FFF;
        """)
        self.resize(600, 400)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("请输入要翻译的文本:"))
        self.text_input = StyledLineEdit()
        input_layout.addWidget(self.text_input)
        layout.addLayout(input_layout)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
            font-family: Arial;
            font-size: 14px;
            color: #333;
            background-color: #F0F0F0;
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 10px;
        """)
        layout.addWidget(self.output_text)

        button_layout = QHBoxLayout()
        self.translate_button = QPushButton("翻译")
        self.translate_button.setStyleSheet("""
            font-family: Arial;
            font-size: 14px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: #FFF;
            border-radius: 10px;
        """)
        self.translate_button.clicked.connect(self.translate_text)
        button_layout.addWidget(self.translate_button)

        self.save_button = QPushButton("保存为JSON文件")
        self.save_button.setStyleSheet("""
            font-family: Arial;
            font-size: 14px;
            padding: 10px 20px;
            background-color: #2196F3;
            color: #FFF;
            border-radius: 10px;
        """)
        self.save_button.clicked.connect(self.save_json)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def translate_text(self):
        text = self.text_input.text()
        if text:
            appid = "20210103000662299"
            salt = "1435660288"
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
