import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox, QListWidget
from PyQt5.QtCore import QDate, Qt, QTimer
import sqlite3


class StudyTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Study Tracker')
        self.setGeometry(100, 100, 400, 400)

        self.records = {}  # 打卡记录字典

        # 日历部件
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.update_selected_date)

        # 文本标签和按钮
        self.label_date = QLabel(self)
        self.label_date.setAlignment(Qt.AlignCenter)

        self.label_theme = QLabel('打卡主题:', self)
        self.label_theme.setAlignment(Qt.AlignCenter)
        self.line_theme = QLineEdit(self)

        self.label_duration = QLabel('学习时长(分钟):', self)
        self.label_duration.setAlignment(Qt.AlignCenter)
        self.line_duration = QLineEdit(self)

        self.label_achievement = QLabel('成果记录:', self)
        self.label_achievement.setAlignment(Qt.AlignCenter)
        self.text_achievement = QTextEdit(self)

        self.btn_start = QPushButton('开始学习', self)
        self.btn_start.clicked.connect(self.start_timer)

        self.btn_end = QPushButton('结束学习', self)
        self.btn_end.clicked.connect(self.end_timer)
        self.btn_end.setEnabled(False)

        self.btn_add = QPushButton('添加记录', self)
        self.btn_add.clicked.connect(self.add_record)

        self.btn_save = QPushButton('保存记录', self)
        self.btn_save.clicked.connect(self.save_records)

        # 打卡记录显示区域
        self.record_list = QListWidget(self)

        # 布局管理
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.label_date)
        self.layout.addWidget(self.label_theme)
        self.layout.addWidget(self.line_theme)
        self.layout.addWidget(self.label_duration)
        self.layout.addWidget(self.line_duration)
        self.layout.addWidget(self.label_achievement)
        self.layout.addWidget(self.text_achievement)
        self.layout.addWidget(self.btn_start)
        self.layout.addWidget(self.btn_end)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.btn_save)
        self.layout.addWidget(self.record_list)

        self.setLayout(self.layout)

        # 计时器相关变量
        self.timer = QTimer()
        self.total_duration = 0

        # 数据库连接和表操作
        self.conn = sqlite3.connect('study.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS study_records
                               (date TEXT, theme TEXT, duration INTEGER, achievement TEXT)''')
        self.conn.commit()

    def update_selected_date(self):
        selected_date = self.calendar.selectedDate()
        self.label_date.setText(f"当前选中的日期：{selected_date.toString('yyyy-MM-dd')}")
        # 更新打卡记录显示区域内容
        self.update_record_list(selected_date)

    def start_timer(self):
        self.btn_start.setEnabled(False)
        self.btn_end.setEnabled(True)
        self.total_duration = 0
        self.timer.timeout.connect(self.update_duration)
        self.timer.start(60000)  # 每分钟触发一次

    def update_duration(self):
        self.total_duration += 1
        self.line_duration.setText(f"{self.total_duration} 分钟")

    def end_timer(self):
        self.timer.stop()
        confirm_box = QMessageBox.question(self, '确认', '是否已完成学习？', QMessageBox.Yes | QMessageBox.No)
        if confirm_box == QMessageBox.Yes:
            self.btn_start.setEnabled(True)
            self.btn_end.setEnabled(False)
            theme = self.line_theme.text()
            duration = self.total_duration
            achievement = self.text_achievement.toPlainText()

            if len(theme) == 0 or duration == 0 or len(achievement) == 0:
                return

            selected_date = self.calendar.selectedDate()
            record = (selected_date.toString('yyyy-MM-dd'), theme, duration, achievement)

            self.records[selected_date] = record
            self.add_record_to_list(record)

            QMessageBox.information(self, '提示', '已记录打卡信息')

            # 清空输入框和计时器
            self.line_theme.clear()
            self.line_duration.clear()
            self.text_achievement.clear()
            self.total_duration = 0
        else:
            self.timer.start()

    def add_record(self):
        theme = self.line_theme.text()
        duration = self.total_duration
        achievement = self.text_achievement.toPlainText()

        if len(theme) == 0 or duration == 0 or len(achievement) == 0:
            return

        selected_date = self.calendar.selectedDate()
        record = (selected_date.toString('yyyy-MM-dd'), theme, duration, achievement)

        self.records[selected_date] = record
        self.add_record_to_list(record)

        QMessageBox.information(self, '提示', '已添加打卡记录')

        # 清空输入框和计时器
        self.line_theme.clear()
        self.line_duration.clear()
        self.text_achievement.clear()
        self.total_duration = 0

    def save_records(self):
        records = list(self.records.values())
        self.cursor.executemany('INSERT INTO study_records VALUES (?, ?, ?, ?)', records)
        self.conn.commit()
        QMessageBox.information(self, '提示', '已保存所有打卡记录至数据库')

    def update_record_list(self, selected_date):
        self.record_list.clear()
        if selected_date in self.records:
            record = self.records[selected_date]
            item = f"日期：{record[0]}\n" \
                   f"主题：{record[1]}\n" \
                   f"学习时长：{record[2]}分钟\n" \
                   f"成果记录：{record[3]}"
            self.record_list.addItem(item)

    def add_record_to_list(self, record):
        item = f"日期：{record[0]}\n" \
               f"主题：{record[1]}\n" \
               f"学习时长：{record[2]}分钟\n" \
               f"成果记录：{record[3]}"
        self.record_list.addItem(item)

    def closeEvent(self, event):
        confirm_box = QMessageBox.question(self, '确认', '是否要退出应用程序？', QMessageBox.Yes | QMessageBox.No)
        if confirm_box == QMessageBox.Yes:
            self.cursor.close()
            self.conn.close()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tracker = StudyTracker()
    tracker.show()
    sys.exit(app.exec_())
