import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

#单纯ts转mp4
# 设置主题颜色
BG_COLOR = '#f7f7f7'
FG_COLOR = '#333333'
SELECT_COLOR = '#4788c7'

root = tk.Tk()
root.title("TS 转 MP4 by vagmr")
root.geometry('500x200')

# 创建 Canvas 控件，将背景图片绘制到 Canvas 上
image = Image.open("res/bc.jpg")
photo = ImageTk.PhotoImage(image)

# 获取窗口大小
window_width = root.winfo_width()
window_height = root.winfo_height()

# 创建 Canvas 控件，并设置其大小为窗口大小
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# 将图片绘制到 Canvas 控件上，并设置其大小与 Canvas 控件相同
canvas_image = canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.itemconfig(canvas_image, image=photo)
canvas.config(width=photo.width(), height=photo.height())

# 创建 Style 对象并设置主题
style = ThemedStyle(root)
style.theme_use('equilux')

def on_enter(event):
    event.widget['background'] = SELECT_COLOR

def on_leave(event):
    event.widget['background'] = BG_COLOR

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
input_label = ttk.Label(root, text="输入文件：", font=("Microsoft Yahei", 12), foreground=FG_COLOR, background=BG_COLOR)
input_label.place(relx=0.05, rely=0.25)
input_entry = ttk.Entry(root, width=50, font=("Microsoft Yahei", 10))
input_entry.place(relx=0.05, rely=0.35)
select_input_button = ttk.Button(root, text="选择文件", command=select_input_file, style="AccentButton.TButton", cursor="hand2")
select_input_button.place(relx=0.75, rely=0.35)
select_input_button.bind("<Enter>", on_enter)
select_input_button.bind("<Leave>", on_leave)

output_label = ttk.Label(root, text="输出文件：", font=("Microsoft Yahei", 12), foreground=FG_COLOR, background=BG_COLOR)
output_label.place(relx=0.05, rely=0.45)
output_entry = ttk.Entry(root, width=50, font=("Microsoft Yahei", 10))
output_entry.place(relx=0.05, rely=0.55)
select_output_button = ttk.Button(root, text="选择文件", command=select_output_file, style="AccentButton.TButton", cursor="hand2")
select_output_button.place(relx=0.75, rely=0.55)
select_output_button.bind("<Enter>", on_enter)
select_output_button.bind("<Leave>", on_leave)

# 创建转换按钮
convert_button = ttk.Button(root, text="转换", command=convert, style="AccentButton.TButton", cursor="hand2")
convert_button.place(relx=0.4, rely=0.8)
convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# 定义样式
style.configure("TEntry", foreground=FG_COLOR, background="#ffffff", fieldbackground="#f7f7f7", font=("Microsoft Yahei", 10))
style.configure("TLabel", foreground=FG_COLOR, background="#f7f7f7")
style.configure("AccentButton.TButton", font=("Microsoft Yahei", 10), foreground='#ffffff', background=SELECT_COLOR, borderwidth=0, padding=5)

root.mainloop()
