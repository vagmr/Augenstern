import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, Menu
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import pygame
import PIL.Image, PIL.ImageTk
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize
import threading

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
    event.widget.configure(background=SELECT_COLOR)

def on_leave(event):
   event.widget.configure(background=BG_COLOR)

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

# 添加下拉菜单
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="打开音乐播放器")
file_menu.add_command(label="打开视频播放器")

# 创建第二个菜单栏
# 创建第二个菜单栏
menu_bar2 = Menu(root)

# 添加菜单和菜单项
about_menu = Menu(menu_bar2, tearoff=0)
#about_menu.add_command(label="关于")
menu_bar2.add_cascade(label="关于", menu=about_menu)



def open_music_player():
    # 创建新窗口
    music_player_window = tk.Toplevel(root)
    music_player_window.title("音乐播放器")
    music_player_window.geometry('400x100')

    # 初始化 pygame 模块
    pygame.init()

    # 定义变量用于存储音乐文件路径
    music_file_path = ''

    def play_music():
        # 确保有选择音乐文件
        if not music_file_path:
            tk.messagebox.showerror('错误', '请选择音乐文件！')
            return

        # 加载音乐
        pygame.mixer.music.load(music_file_path)

        # 播放音乐
        pygame.mixer.music.play()

    def stop_music():
        # 停止音乐
        pygame.mixer.music.stop()

    def select_music_file():
        nonlocal music_file_path
        music_file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[('MP3 Files', '*.mp3'), ('All Files', '*.*')])
        selected_file_label.config(text=os.path.basename(music_file_path))

    # 创建按钮和标签
    select_file_button = ttk.Button(music_player_window, text="选择音乐文件", command=select_music_file, style="AccentButton.TButton", cursor="hand2")
    select_file_button.pack(side=tk.LEFT, padx=10)

    selected_file_label = ttk.Label(music_player_window, text='未选择文件', font=("Microsoft Yahei", 10), foreground=FG_COLOR, background=BG_COLOR)
    selected_file_label.pack(side=tk.LEFT, padx=10)

    play_button = ttk.Button(music_player_window, text="播放", command=play_music, style="AccentButton.TButton", cursor="hand2")
    play_button.pack(side=tk.LEFT, padx=10)

    stop_button = ttk.Button(music_player_window, text="停止", command=stop_music, style="AccentButton.TButton", cursor="hand2")
    stop_button.pack(side=tk.LEFT, padx=10)
# 视频播放器模块
# =========================================================================================================================
# 定义视频播放器函数
def open_video_player():
    """
    打开一个视频播放器窗口，并允许用户播放视频文件。
    """
    # 创建主窗口
    video_window = tk.Toplevel()
    video_window.title("视频播放器")
    video_window.geometry("800x600")

    # 设置全局变量
    video_file_path = None
    is_playing = False
    fps = 30

    # 创建 Canvas 控件，用于显示视频帧
    width, height = 640, 360
    canvas = tk.Canvas(video_window, width=width, height=height)
    canvas.pack()

    # 创建播放、暂停、选择文件按钮
    play_button = tk.Button(video_window, text="播放", command=lambda: play_video())
    pause_button = tk.Button(video_window, text="暂停", state=tk.DISABLED, command=lambda: pause_video())
    open_button = tk.Button(video_window, text="选择视频文件", command=lambda: select_video_file())
    play_button.pack(side=tk.LEFT)
    pause_button.pack(side=tk.LEFT)
    open_button.pack(side=tk.LEFT)

    def select_video_file():
        """
        打开文件选择对话框，允许用户选择一个视频文件。
        """
        nonlocal video_file_path

        # 从文件选择对话框中获取视频文件路径
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.flv")])
        if path:
            video_file_path = path
            play_button.configure(state=tk.NORMAL)

    def play_video():
        """
        播放视频。
        """
        nonlocal is_playing
        is_playing = True
        play_button.configure(state=tk.DISABLED)
        pause_button.configure(state=tk.NORMAL)

        # 打开视频文件
        clip = VideoFileClip(video_file_path)

        def update_frame():
            """
            更新当前时间点下的帧，并将其缩放至 Canvas 的大小，最后显示在 Canvas 上。
            """
            if is_playing:
                # 截取当前时间点下的帧
                frame = clip.get_frame(clip.duration * canvas.coords()[2] / width, False)
                # 将获取到的视频帧进行缩放处理
                frame = resize(frame, (width, height))

                # 将视频帧转换为 Image 对象，并在 Canvas 上显示
                img = PIL.Image.fromarray(frame)
                imgtk = PIL.ImageTk.PhotoImage(image=img)
                canvas.imgtk = imgtk
                canvas.create_image(0, 0, anchor="nw", image=imgtk)
                canvas.update()

                # 设置 1000/fps 秒后更新下一帧
                video_window.after(1000 // fps, update_frame)

        # 创建线程，在其中更新视频帧
        t = threading.Thread(target=update_frame)
        t.start()

    def pause_video():
        """
        暂停播放视频。
        """
        nonlocal is_playing
        is_playing = False
        play_button.configure(state=tk.NORMAL)
        pause_button.configure(state=tk.DISABLED)

    # 呈现窗口
    video_window.mainloop()


# =================================================================================================================================
def about():
    # 创建新窗口
    about_window = tk.Toplevel(root)
    about_window.title("关于")
    about_window.geometry('300x200')

    # 添加标签控件，显示应用程序的名称、版本号、开发者等相关信息
    app_name_label = ttk.Label(about_window, text="TS 转 MP4 by vagmr", font=("Microsoft Yahei", 16), foreground=FG_COLOR, background=BG_COLOR)
    app_name_label.pack(pady=15)

    version_label = ttk.Label(about_window, text="版本号：0.11", font=("Microsoft Yahei", 12), foreground=FG_COLOR, background=BG_COLOR)
    version_label.pack()

    developer_label = ttk.Label(about_window, text="开发者：vagmr", font=("Microsoft Yahei", 12), foreground=FG_COLOR, background=BG_COLOR)
    developer_label.pack(pady=5)

    # 呈现窗口
    about_window.mainloop()

# 创建关于菜单项
about_menu.add_command(label="关于", command=about)


# 将下拉菜单添加到菜单栏
file_menu.entryconfig(0, command=open_music_player)
file_menu.entryconfig(1, command=open_video_player)
# 菜单功能模块对应函数调用

menu_bar.add_cascade(label="菜单", menu=file_menu)#菜单显示按钮
menu_bar.add_cascade(label="关于", menu=about_menu)




# 定义样式
style.configure("TEntry", foreground=FG_COLOR, background="#ffffff", fieldbackground="#f7f7f7", font=("Microsoft Yahei", 10))
style.configure("TLabel", foreground=FG_COLOR, background="#f7f7f7")
style.configure("AccentButton.TButton", font=("Microsoft Yahei", 10), foreground='#ffffff', background=SELECT_COLOR, borderwidth=0, padding=5)

root.mainloop()
