import datetime
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

root = tk.Tk()
root.title('ts文件转换器 by vagmr')
root.geometry('600x450')
root.resizable(width=True, height=True)

style = ttk.Style()

style.configure('TButton', background='#2a4d69', foreground='white',
                font=('微软雅黑体', 12), width=10, height=2)

style.configure('TLabel', background='#f0f0f0', foreground='#333333',
                font=('微软雅黑体', 12))

style.configure('TEntry', foreground='#333333',
                font=('微软雅黑体', 10), background='#f0f0f0')

style.configure('TProgressbar', background='#2a4d69', troughcolor='#f0f0f0')

top_frame = ttk.Frame(root, padding=10)
top_frame.pack(fill='both', expand=True)

input_label = ttk.Label(top_frame, text='选择输入文件:')
input_label.grid(row=0, column=0, pady=10, sticky='w')

input_entry = ttk.Entry(top_frame)
input_entry.grid(row=0, column=1, padx=5, pady=10, sticky='we')

input_button = ttk.Button(top_frame, text='选择路径',
                          command=lambda: choose_file(input_entry))
input_button.grid(row=0, column=2, pady=10, padx=10)

output_label = ttk.Label(top_frame, text='选择输出文件:')
output_label.grid(row=1, column=0, pady=10, sticky='w')

output_entry = ttk.Entry(top_frame)
output_entry.grid(row=1, column=1, padx=5, pady=10, sticky='we')

output_button = ttk.Button(top_frame, text='选择路径',
                           command=lambda: choose_file(output_entry, save=True))
output_button.grid(row=1, column=2, pady=10, padx=10)

convert_button = ttk.Button(top_frame, text='开始转换',
                            command=lambda: convert(input_entry.get(), output_entry.get()))
convert_button.grid(row=2, column=0, pady=20, padx=10, columnspan=3)

progress_frame = ttk.Frame(root, padding=10)
progress_frame.pack(fill='both', expand=True)

ttk.Separator(progress_frame, orient='horizontal').pack(fill='x', pady=(0, 10))

progress_label = ttk.Label(progress_frame, text='进度:')
progress_label.pack(side='left', padx=10)

progress = ttk.Progressbar(progress_frame, mode='indeterminate')
progress.pack(side='left', fill='x', expand=True, padx=10)

log_frame = ttk.Frame(root, padding=10)
log_frame.pack(fill='both', expand=True)

ttk.Separator(log_frame, orient='horizontal').pack(fill='x', pady=(0, 10))

log_label = ttk.Label(log_frame, text='日志输出:')
log_label.pack(side='left', padx=10)

log_text = tk.Text(log_frame, height=5, bg='#f0f0f0', fg='#333333',
                   font=('微软雅黑体', 10))
log_text.pack(side='left', fill='both', expand=True, padx=10,
              pady=10, ipadx=5, ipady=5)

# 添加垂直滚动条
scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=log_text.yview)
scrollbar.pack(side='right', fill='y')

log_text.configure(yscrollcommand=scrollbar.set)


def choose_file(entry, save=False):
    if save:
        filename = filedialog.asksaveasfilename(
            title='选择文件', defaultextension='.mp4',
            filetypes=[('MP4 文件', '*.mp4')])
    else:
        filename = filedialog.askopenfilename(
            title='选择文件', filetypes=[('TS 文件', '*.ts')])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)


def convert(input_file, output_file):
    if not input_file or not os.path.exists(input_file):
        messagebox.showerror('错误', '输入文件不存在！')
        return

    progress.configure(mode='determinate', maximum=100, value=0)  # 设置进度条模式和最大值
    progress.start()

    if not output_file:
        default_name = f'video_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.mp4'
        output_file = os.path.join(os.path.dirname(input_file), default_name)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_file)

    cmd = f'ffmpeg -i "{input_file}" -c copy "{output_file}"'
    log_text.delete('1.0', tk.END)
    log_text.insert(tk.END, f'开始转换: {input_file} -> {output_file}\n\n')

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        log_text.insert(tk.END, line.decode('utf-8'))
        log_text.see(tk.END)
        log_text.update_idletasks()

        if b'realtime' in line:  # 根据输出信息中的关键字来更新进度条
            percent = int(line.split(b'realtime')[1].split(b'%')[0])
            progress.step(percent - progress['value'])  # 更新进度条
    progress.stop()
    messagebox.showinfo('提示', '转换完成！')
    result = messagebox.askquestion('提示', '是否删除原始 TS 文件？')
    if result == 'yes':
        os.remove(input_file)


root.mainloop()
