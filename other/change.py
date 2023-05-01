import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("TS 转 MP4 by vagmr")

# 选择输入文件
def select_input_file():
    input_file = filedialog.askopenfilename(
        defaultextension=".ts",
        filetypes=[('TS Files', '*.ts'), ('All Files', '*.*')]
    )
    input_entry.delete(0, tk.END)  # 清空输入框中的内容
    input_entry.insert(0, input_file)  # 在输入框中显示选中的文件路径

# 选择输出文件
def select_output_file():
    output_file = filedialog.asksaveasfilename(
        title='选择输出文件',
        defaultextension=".mp4",
        filetypes=[('MP4 Files', '*.mp4'), ('All Files', '*.*')]
    )
    output_entry.delete(0, tk.END)  # 清空输出框中的内容
    output_entry.insert(0, output_file)  # 在输出框中显示选中的文件路径

# 转换函数
def convert():
    # 获取用户输入的文件路径和输出路径
    input_file = input_entry.get()
    output_file = output_entry.get()

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        tk.messagebox.showerror('错误', '输入文件不存在！')
        return

    # 如果未命名输出文件，则使用默认名称
    if not output_file:
        default_name = f'vamgr{datetime.datetime.now().strftime("%Y%m%d")}.mp4'
        output_file = default_name
        output_entry.delete(0, tk.END)  # 清空输出框中的内容
        output_entry.insert(0, output_file)  # 在输出框中显示选中的文件路径

    # 使用FFmpeg将ts文件转换为mp4文件
    os.system(f'ffmpeg -i "{input_file}" -c copy "{output_file}"')

    # 显示转换完成提示框
    tk.messagebox.showinfo('提示', '转换完成！')

    # 弹出对话框询问用户是否删除 TS 文件
    result = tk.messagebox.askquestion('提示', '是否删除原始 TS 文件？')

    # 如果用户点击了 "是" 按钮，则删除 TS 文件
    if result == 'yes':
        os.remove(input_file)

# 创建 Label 和 Entry 控件
input_label = tk.Label(root, text="输入文件：")
input_label.grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)

output_label = tk.Label(root, text="输出文件：")
output_label.grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)

# 创建选择文件和转换按钮
select_input_button = tk.Button(root, text="选择输入文件", command=select_input_file)
select_input_button.grid(row=0, column=2, padx=10, pady=10)

select_output_button = tk.Button(root, text="选择输出文件", command=select_output_file)
select_output_button.grid(row=1, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text="转换", command=convert)
convert_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
