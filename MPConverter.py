import tkinter as tk
from tkinter import filedialog, ttk, simpledialog
from moviepy.editor import *
import threading

def convert_audio_to_mp3_or_wav(filepath, label):
    if filepath.endswith(".mp4"):
        label.config(text="変換中です...", bg="yellow")
        clip = VideoFileClip(filepath)
        audio_format = simpledialog.askstring("フォーマット選択", "mp3かwavのどちらに変換しますか？", initialvalue="mp3")
        if audio_format not in ["mp3", "wav"]:
            label.config(text="無効なフォーマットが選択されました。", bg="red")
            return
        clip.audio.write_audiofile(filepath.replace(".mp4", f".{audio_format}"), codec=audio_format)
    elif filepath.endswith(".mp3"):
        label.config(text="変換中です...", bg="yellow")
        audioclip = AudioFileClip(filepath)
        imgclip = ImageClip("image.jpg", duration=audioclip.duration)
        videoclip = CompositeVideoClip([imgclip.set_audio(audioclip)])
        videoclip.write_videofile(filepath.replace(".mp3", ".mp4"), codec='mpeg4', fps=24)
    label.config(text="変換が完了しました！", bg="green")

def convert(label):
    filepath = filedialog.askopenfilename()
    threading.Thread(target=convert_audio_to_mp3_or_wav, args=(filepath, label)).start()

root = tk.Tk()
root.title("動画・音声変換ツール")
root.geometry("400x200")
root.configure(bg="lightgrey")

button = tk.Button(root, text="ファイルを選択して変換", command=lambda: convert(label), bg="blue", fg="white", font=("Helvetica", 16))
button.pack(pady=20)

label = tk.Label(root, text="", bg="lightgrey", font=("Helvetica", 16))
label.pack()

root.mainloop()
