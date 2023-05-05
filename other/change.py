import datetime
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


root = tk.Tk()
root.title('视频转换器')
root.geometry('600x400')

# 添加输入文件路径和输出文件路径选择框
input_label = tk.Label(root, text='输入文件:')
input_label.grid(row=0, column=0, padx=10, pady=10)

input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

output_label = tk.Label(root, text='输出文件:')
output_label.grid(row=1, column=0, padx=10, pady=10)

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

def choose_input_file():
    filename = filedialog.askopenfilename(title='选择输入文件', filetypes=[('TS 文件', '*.ts')])
    if filename:
        input_entry.delete(0, tk.END)  # 清空输入框中的内容
        input_entry.insert(0, filename)  # 在输入框中显示选中的文件路径

def choose_output_file():
    filename = filedialog.asksaveasfilename(title='选择输出文件', defaultextension='.mp4',
                                            filetypes=[('MP4 文件', '*.mp4')])
    if filename:
        output_entry.delete(0, tk.END)  # 清空输出框中的内容
        output_entry.insert(0, filename)  # 在输出框中显示选中的文件路径

input_button = tk.Button(root, text='选择文件', command=choose_input_file)
input_button.grid(row=0, column=3, padx=10, pady=10)

output_button = tk.Button(root, text='选择文件', command=choose_output_file)
output_button.grid(row=1, column=3, padx=10, pady=10)

# 添加转换按钮和进度条
def convert():
    # 获取用户输入的文件路径和输出路径
    input_file = input_entry.get()
    output_file = output_entry.get()

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        tk.messagebox.showerror('错误', '输入文件不存在！')
        return

    # 显示进度条
    progress.config(mode='indeterminate')
    progress.start()

    # 如果未命名输出文件，则使用默认名称
    if not output_file:
        default_name = f'vamgr{datetime.datetime.now().strftime("%Y%m%d")}.mp4'
        output_file = default_name
        output_entry.delete(0, tk.END)  # 清空输出框中的内容
        output_entry.insert(0, output_file)  # 在输出框中显示选中的文件路径

    # 使用FFmpeg将ts文件转换为mp4文件
    cmd = f'ffmpeg -i "{input_file}" -c copy "{output_file}"'
    log_text.insert(tk.END, f'\n> {cmd}\n')
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        log_text.insert(tk.END, line.decode('utf-8'))
        log_text.see(tk.END)
        log_text.update_idletasks()

    # 停止并销毁进度条
    progress.stop()

    # 显示转换完成提示框
    tk.messagebox.showinfo('提示', '转换完成！')

    # 弹出对话框询问用户是否删除 TS 文件
    result = tk.messagebox.askquestion('提示', '是否删除原始 TS 文件？')

    # 如果用户点击了 "是" 按钮，则删除 TS 文件
    if result == 'yes':
        os.remove(input_file)

    progress.destroy()

convert_button = tk.Button(root, text='开始转换', command=convert)
convert_button.grid(row=2, column=1, pady=10)

progress = ttk.Progressbar(root, length=300)
progress.grid(row=2, column=2)

# 添加日志输出区域
log_label = tk.Label(root, text='输出日志:')
log_label.grid(row=7, column=0, padx=10, pady=10)

log_text = tk.Text(root, height=17)
log_text.grid(row=7, column=1, pady=10)

root.mainloop()
