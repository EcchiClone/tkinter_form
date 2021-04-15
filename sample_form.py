# 기능 관해선 적당히 남긴 것 같아 수정은 이걸로 끝...
# 아래와 같이 pyinstaller 등을 사용하여 실행파일로 만들 수 있다.
# pyinstaller.exe -F -w --onefile --icon=icon.ico sample_form.py

import tkinter as tk # 애플리케이션 gui
from tkinter import messagebox # tk 경고박스 등
import os # 폴더생성 등, konachan_gui.py 참고
from datetime import datetime # 시스템 시간
import time # time.sleep() 등에 사용
import threading # 스레드
import sys # 애플리케이션 종료 등
import urllib.request # 웹 정보에 접근, 처리 등
import webbrowser
from bs4 import BeautifulSoup

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

# 샘플 스레드입니다. 버튼 1을 클릭 시, 샘플 클래스를 호출합니다.
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
        self.lb1 = tk.Label(window, text="INPUT")
        self.lb1.grid(row=0,column=0)
        self.lb2 = tk.Label(window, text="OUTPUT")
        self.lb2.grid(row=1,column=0)

        # 업데이트용 변수와 라벨
        self.log = tk.StringVar()
        self.log.set("")
        self.lb3 = tk.Label(window, textvariable=self.log)
        self.lb3.grid(row=3,column=0,columnspan=3)

        # 입력 가능한 텍스트칸 위젯 Entry
        self.str1=tk.StringVar()
        self.str2=tk.StringVar()

        self.entry1 = tk.Entry(window, textvariable=self.str1)
        self.entry1.grid(row=0,column=1,columnspan=2)
        self.entry2 = tk.Entry(window, textvariable=self.str2)
        self.entry2.grid(row=1,column=1,columnspan=2)
        self.entry2.delete(0,"end")
        self.entry2.insert(0,"Hello, Output")

        # 버튼1
        self.btn_txt = tk.StringVar()
        self.btn_txt.set("btn")
        self.btn1 = tk.Button(window, textvariable=self.btn_txt, width=10, height=4)
        self.btn1["command"] = self.btn1_function # 이렇게 설정도 가능하고, 버튼 2처럼 직접 속성을 넣을 수도 있다.
        self.btn1.grid(row=0,column=3,rowspan=3)
        
        # 체크박스용 변수와 체크박스
        self.int1=tk.IntVar()
        self.check1 = tk.Checkbutton(window, text="CB1", variable = self.int1)
        self.check1.select()
        self.check1.grid(row=2,column=1)

        self.int2=tk.IntVar()
        self.check2 = tk.Checkbutton(window, text="CB2", variable = self.int2)
        self.check2.grid(row=2,column=2)


        # 버튼2
        self.quit_btn = tk.Button(window, text="QUIT", fg="red", command=self.quit_btn_function, width=10, height=2)
        self.quit_btn.grid(row=3,column=3,rowspan=2)
        LabelUpdate(self).start()

    # 버튼 1을 클릭 시 실행합니다
    def btn1_function(self):
        print("PUSH DL BUTTON")
        NewThread(self).start()

    # 버튼 2를 클릭 시 실행합니다
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
# window.iconbitmap(default='icon.ico')
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon.png'))
window.geometry("293x117+1200+200")
window.resizable(False,False)

# 앱 시작
app = Application(master=window)
app.mainloop()