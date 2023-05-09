import tkinter as tk
import os
import threading
import requests
from tkinter import filedialog


class DownloadWindow(object):
    def __init__(self, master):
        self.master = master
        master.title("m3u8 downloader")

        # Create URL input area
        self.url_label = tk.Label(master, text="m3u8 URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        # Create output directory selection area
        self.dir_label = tk.Label(master, text="Output directory:")
        self.dir_label.pack()
        self.dir_frame = tk.Frame(master)
        self.dir_frame.pack()
        self.dir_entry = tk.Entry(self.dir_frame)
        self.dir_entry.pack(side=tk.LEFT)
        self.dir_button = tk.Button(
            self.dir_frame, text="Choose", command=self.choose_dir)
        self.dir_button.pack(side=tk.LEFT)

        # Create download button
        self.download_button = tk.Button(
            master, text="Download", command=self.download)
        self.download_button.pack()

        # Create log area
        self.log_text = tk.Text(master, height=10)
        self.log_text.pack()

    def choose_dir(self):
        chosen_dir = filedialog.askdirectory()
        self.dir_entry.insert(0, chosen_dir)

    def download(self):
        url = self.url_entry.get()
        output_dir = self.dir_entry.get()

        if url == "":
            self.log("Please enter a URL.")
            return

        if output_dir == "":
            self.log("Please choose an output directory.")
            return

        t = threading.Thread(target=self.do_download, args=(url, output_dir))
        t.start()

    def do_download(self, m3u8_url, output_dir):
        self.log(f"Downloading {m3u8_url}...")
        try:
            m3u8_data = requests.get(m3u8_url).text
            base_url = m3u8_url[:m3u8_url.rfind('/')+1]
            lines = m3u8_data.split('\n')
            ts_urls = [base_url +
                       line for line in lines if line.endswith('.ts')]
            key_url = [line.split('=')[1]
                       for line in lines if line.startswith('#EXT-X-KEY')][0]
            key_data = requests.get(key_url).content

            # Download and decrypt each .ts file
            index = 1
            for ts_url in ts_urls:
                self.log(f"Downloading {ts_url}")
                output_path = os.path.join(output_dir, f"{index:04}.ts")
                self.download_file(ts_url, output_path)
                index += 1

            # Merge .ts files to .mp4
            mp4_output = os.path.join(output_dir, 'output.mp4')
            os.system(
                f"cd {output_dir} && ffmpeg -i 'concat:*' -c copy {mp4_output}")

            # Remove .ts files
            for ts_url in ts_urls:
                os.remove(os.path.join(output_dir, f"{index:04}.ts"))

            self.log("Download complete!")
        except Exception as e:
            self.log(f"Error: {e}")

    def download_file(self, url, output_path):
        with open(output_path, 'wb') as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                downloaded = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    downloaded += len(data)
                    f.write(data)
                    progress = (downloaded / total_length) * 100
                    self.log(
                        f"Downloaded {progress:.2f}% of {total_length/1024/1024:.2f}MB")

    def log(self, text):
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)


root = tk.Tk()
app = DownloadWindow(root)
root.mainloop()
