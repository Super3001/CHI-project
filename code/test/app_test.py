# app_test.py

from pywinauto import Desktop, Application
import time
import tkinter as tk
import subprocess
from trigger import *

p_stop = False
class App:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Initial Text")
        self.label.pack()
        master.geometry('200x200')
        self.run()

    def run(self):
        print('run start:')
        st_ = time.time()
        p = subprocess.Popen(['python', 'code/test/serial_in_test.py'], stdout=subprocess.PIPE)
        for i, line in enumerate(iter(p.stdout.readline, b'')):
            if i==1:
                end_ = time.time()
                print(f'elapsed: {end_ - st_}s')
            # 处理每一行输出
            # print(f'{i}: {line} ',end='')
            # print(line)
            global p_stop
            if p_stop:
                p.kill()  # 杀死进程
                outs, errs = p.communicate()
            code = line.decode('utf-8').strip()
            self.deal(code)

    def deal(self, code):
        if type(code) == str and len(code)==2:
            print(code, end=' ')
            Trigger(code)
            

def main():
    global root, app
    root = tk.Tk()
    app = App(root)
    root.mainloop()

def shut(p):
    global p_stop
    p_stop = True
    time.sleep(0.1)
    try:
        root.destroy()
    except:
        print('destroyed')
        pass

if __name__ == "__main__":
    main()
