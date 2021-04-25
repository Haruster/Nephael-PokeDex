# 모듈 설치 -> pip(3) install pypokedex && pip(3) install pillow && pip(3) install urllib3

import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3

from io import BytesIO

window = tk.Tk();
window.geometry("600x500")
window.title("Kinesys PokeDex")
window.config(padx = 10, pady = 10)

title_label = tk.Label(window, text = "Kinesys PokeDex")
title_label.config(font = ("Arial", 32))
title_label.pack(padx = 10, pady = 10)
