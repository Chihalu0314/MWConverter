import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import threading

def convert_to_mp3(filepath, label):
    if filepath.endswith(".mp4"):
        label.config(text="変換中です...", bg="yellow")
        clip = VideoFileClip(filepath)
        clip.audio.write_audiofile(filepath.replace(".mp4", ".mp3"), codec="libmp3lame")
        label.config(text="MP3への変換が完了しました！", bg="green")

def convert_to_wav(filepath, label):
    if filepath.endswith(".mp4"):
        label.config(text="変換中です...", bg="yellow")
        clip = VideoFileClip(filepath)
        clip.audio.write_audiofile(filepath.replace(".mp4", ".wav"), codec="libmp3lame")
        label.config(text="WAVへの変換が完了しました！", bg="green")

def convert_to_mp4(filepath, label):
    if filepath.endswith(".mp3"):
        label.config(text="変換中です...", bg="yellow")
        clip = AudioFileClip(filepath)
        clip.write_audiofile(filepath.replace(".mp3", ".mp4"), codec="libmp3lame")
        label.config(text="MP4への変換が完了しました！", bg="green")

def open_file(label, mp4_button, mp3_button, wav_button):
    filepath = filedialog.askopenfilename()
    if filepath.endswith(".mp3"):
        label.config(text="ファイルを選択しました。変換ボタンを押してください。", bg="lightgrey")
        mp4_button.config(state="normal", command=lambda: threading.Thread(target=convert_to_mp4, args=(filepath, label)).start())
        mp3_button.config(state="disabled")
        wav_button.config(state="disabled")
    elif filepath.endswith(".mp4"):
        label.config(text="ファイルを選択しました。変換ボタンを押してください。", bg="lightgrey")
        mp3_button.config(state="normal", command=lambda: threading.Thread(target=convert_to_mp3, args=(filepath, label)).start())
        wav_button.config(state="normal", command=lambda: threading.Thread(target=convert_to_wav, args=(filepath, label)).start())
        mp4_button.config(state="disabled")

root = tk.Tk()
root.title("MPConverter")
root.geometry("600x320")
root.configure(bg="lightgrey")

open_button = tk.Button(root, text="ファイルを選択", bg="blue", fg="white", font=("Helvetica", 16))
open_button.pack(pady=10)

mp4_button = tk.Button(root, text="MP4に変換", state="disabled", bg="blue", fg="white", font=("Helvetica", 16))
mp4_button.pack(pady=10)

mp3_button = tk.Button(root, text="MP3に変換", state="disabled", bg="blue", fg="white", font=("Helvetica", 16))
mp3_button.pack(pady=10)

wav_button = tk.Button(root, text="WAVに変換", state="disabled", bg="blue", fg="white", font=("Helvetica", 16))
wav_button.pack(pady=10)

label = tk.Label(root, text="", bg="lightgrey", font=("Helvetica", 16))
label.pack()

open_button.config(command=lambda: open_file(label, mp4_button, mp3_button, wav_button))

root.mainloop()
