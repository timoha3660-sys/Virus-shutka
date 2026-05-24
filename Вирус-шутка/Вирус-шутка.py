import tkinter as tk
from tkinter import messagebox
import random
import winsound as wins
wins.Beep(500, 500)
import pyautogui
import time
from PIL import Image, ImageTk
import os
import sys
if sys.platform.startswith('win'):
    ver = sys.getwindowsversion()
    if ver.major == 6 and ver.minor == 1:
        version=7
    elif ver.major == 10 and ver.build >= 10240:
        if ver.build < 22000:
            version=10
        else:
            version=11
active_images=[]
active_windows=[]
photos=[os.path.dirname(os.path.abspath(__file__))+"\\Cross.png", os.path.dirname(os.path.abspath(__file__))+"\\Triangle.png", os.path.dirname(os.path.abspath(__file__))+"\\AMOGUS.png"]
current=0
interation=0
bsod=False
def show_BSOD(event=None):
    global bsod, version
    for curr in active_windows:
        curr.withdraw()
    bsod = True
    BSOD = tk.Tk()
    BSOD.config(cursor="none")
    BSOD.attributes('-fullscreen', True)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, f"BSOD{version}.png")
    image = Image.open(image_path)
    print(image)
    BSOD.update_idletasks()
    resized_photo = ImageTk.PhotoImage(image.resize((BSOD.winfo_width(), BSOD.winfo_height())))
    print(resized_photo)
    label=tk.Label(BSOD, image=resized_photo)
    label.image=resized_photo
    label.pack()
    BSOD.focus_force()
    def shutdown_after_timeout():
        os.system("shutdown /r /t 0")
    #BSOD.after(10000, shutdown_after_timeout)
    BSOD.mainloop()
show_BSOD()
def show_image(image_path):
    global active_images, active_windows, interation
    print('\a')
    interation += 1
    x, y = pyautogui.position()
    root = tk.Toplevel()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.configure(bg='black')
    root.wm_attributes("-transparentcolor", "black")
    image = Image.open(image_path)
    width, height = image.size
    canvas = tk.Canvas(root, width=width, height=height, bg='black', highlightthickness=0)
    canvas.pack()
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo
    active_images.append(photo)
    root.geometry(f"+{x}+{y}")
    active_windows.append(root)
if messagebox.askyesno(title="Начать", message="""ЭТО НЕ ВИРУС! ЭТО ШУТКА!
Если вы нажмёте "Да" - то
тогда начнётся хаос! Что-
бы остановить это - надо
выключить компьютер через
кнопку выключения на кор-
пусе компьютера.



Удачи!!"""):
    #show_BSOD()
    window=tk.Tk()
    window.withdraw()
    def update(event=None):
        global interation, current, photos, bsod, active_windows
        if not bsod:
            if interation == 100:
                interation = 0
                if current == 0:
                    current=1
                elif current == 1:
                    current=0
            """
            if interation == 666:
                current=2"""
            show_image(photos[current])
            window.after(10, update)
            window.after(60000, show_BSOD)
    messagebox.showwarning(message="Начнётся через 5 секунд.....")
    window.after(5000, update)
    window.mainloop()
    
