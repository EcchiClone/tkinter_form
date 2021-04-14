import tkinter as tk
from tkinter import messagebox
import time
import urllib.request
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup
import threading
import sys
import webbrowser

LOGTEXT = "이 라벨은 계속 계속 업데이트 됩니다."
BTNTEXT = "Download"

# 라벨 등을 지속적으로 업데이트합니다.
class LabelUpdate(threading.Thread):
    def __init__(self, _window):
        threading.Thread.__init__(self)
        self.win = _window
    def run(self):
        while True:
            time.sleep(0.1)
            self.win.log.set(LOGTEXT)
            self.win.btn_txt.set(BTNTEXT)

# 샘플 스레드입니다. 샘플 클래스를 호출합니다.
class NewThread(threading.Thread):
    def __init__(self, _window):
        threading.Thread.__init__(self)
        self.win = _window
    def run(self):
        print(type(self.win))
        instance = myClass(self.win.str1.get(), self.win.str2.get())

# 샘플 클래스입니다. 새 샘플 스레드에서 실행될 수 있도록 해 두었습니다.
class myClass():
    def __init__(self, __tag, __num):
        pass

# 새 윈도우를 만들고, 위젯 및 기능을 넣습니다.
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        # 라벨, 그리드 배치를 하였습니다.
        self.lb1 = tk.Label(window, text="INPUT").grid(row=0,column=0)
        self.lb2 = tk.Label(window, text="OUTPUT").grid(row=1,column=0)

        # 업데이트용 변수와 라벨
        self.log = tk.StringVar()
        self.log.set("")
        self.lb3 = tk.Label(window, textvariable=self.log).grid(row=3,column=0,columnspan=3)

        # 입력 가능한 텍스트칸 위젯 Entry
        self.str1=tk.StringVar()
        self.str2=tk.StringVar()

        self.entry1 = tk.Entry(window, textvariable=self.str1).grid(row=0,column=1,columnspan=2)
        self.entry2 = tk.Entry(window, textvariable=self.str2).grid(row=1,column=1,columnspan=2)

        # 버튼1
        self.btn_txt = tk.StringVar()
        self.btn_txt.set("btn")
        self.btn1 = tk.Button(window, textvariable=self.btn_txt, width=10, height=4)
        self.btn1["command"] = self.btn1_function
        self.btn1.grid(row=0,column=3,rowspan=3)
        
        # 체크박스용 변수와 체크박스
        self.int1=tk.IntVar()
        self.check1 = tk.Checkbutton(window, text="Safe", variable = self.int1)
        self.check1.select()

        self.int2=tk.IntVar()
        self.check2 = tk.Checkbutton(window, text="+R18", variable = self.int2)

        self.check1.grid(row=2,column=1)
        self.check2.grid(row=2,column=2)

        # 버튼2
        self.quit_btn = tk.Button(window, text="QUIT", fg="red", command=self.quit_btn_function, width=10, height=2)
        self.quit_btn.grid(row=3,column=3,rowspan=2)
        LabelUpdate(self).start()

    def btn1_function(self):
        global LOGTEXT
        print("PUSH DL BUTTON")
        if(self.v1.get()==0 and self.v2.get()==0):
            LOGTEXT = "체크박스가 선택되지 않았습니다."
            return
        NewThread(self).start()

    def quit_btn_function(self):
        sys.exit()


window = tk.Tk()

# 닫기 버튼 시 함수
def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        sys.exit()
window.protocol("WM_DELETE_WINDOW", on_closing)

# 타이틀, 파일아이콘, 윈도우상단아이콘, 윈도우크기, 크기재설정여부
window.title("Simple form [ver=0.1]")
window.iconbitmap(default='icon.ico')
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon.png'))
window.geometry("272x120+1200+200")
window.resizable(False,False)

# 앱 시작
app = Application(master=window)
app.mainloop()