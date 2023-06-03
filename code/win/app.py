
def read_path():
    with open('code\win\path.txt','r', encoding='utf-8') as f:
        # lines = f.readlines()
        path_dict = {}
        for line in f.readlines():
            # print(line)
            if len(line) < 2:
                continue
            window_name,path = line.split(': ')
            path = path.replace('\n','')
            path_dict[window_name] = path
    return path_dict

path_dict = read_path()
print(path_dict)
           
from pywinauto import Desktop, Application

# 获取当前桌面
desktop = Desktop(backend="uia")
"""
# 获取用户输入的窗口名
window_name = input("请输入窗口名：")

# 遍历所有窗口，找到匹配的窗口，并将其置于最前面
for window in desktop.windows():
    if  window_name in window.window_text() :
        window.set_focus()
        break
else:
    # 如果没有找到匹配的窗口，则打开应用程序
    app = Application().start(path_dict[window_name])
"""

def get_last_accessed_window():
    from pywinauto import Desktop
    import os
    desktop = Desktop(backend="uia")
    desktop_window = desktop.window()
    props = desktop_window.GetProperties()
    windows_props = props['Children']
    latest_access_time = 0
    latest_window = None

    for window_prop in windows_props:
        access_time = window_prop['time_last_accessed']
        
        if access_time > latest_access_time:
            latest_access_time = access_time
            latest_window = window_prop
            
    print(latest_window)

def print_windows():
    # 获取当前桌面
    desktop = Desktop(backend="uia")

    # 获取最前面的窗口
    window = desktop.windows()[0]

    # 所有窗口？
    for window in desktop.windows():
        print(window)
    
    
# 加入窗口    
"""
import tkinter as tk

root = tk.Tk()
root.title("下拉框与输入框")

# 创建提示语
label1 = tk.Label(root, text="  左转：")
label2 = tk.Label(root, text="请输入：")
label3 = tk.Label(root, text="请选择：")

# 创建下拉菜单
options = ["选项1", "选项2", "选项3"]
var1 = tk.StringVar(value=options[0])
var3 = tk.StringVar(value=options[0])
menu1 = tk.OptionMenu(root, var1, *options)
menu3 = tk.OptionMenu(root, var3, *options)

# 创建输入框
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# 使用grid布局
label1.grid(row=0, column=0)
menu1.grid(row=0, column=1)
entry1.grid(row=0, column=2)
label2.grid(row=1, column=0)
entry2.grid(row=1,column=2)
label3.grid(row=2, column=0)
menu3.grid(row=2, column=1)
entry3.grid(row=2, column=2)

root.mainloop()


import tkinter as tk

root = tk.Tk()

# 创建三个标签和输入框
label1 = tk.Label(root, text="左转：")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="右转：")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="请输入内容3：")
entry3 = tk.Entry(root)

# 将标签和输入框添加到界面中
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

# 运行界面
root.mainloop()


import tkinter as tk

def on_key_release(event):
    \"""响应键盘输入的函数\"""
    print(event.widget.get())
    

root = tk.Tk()

entry = tk.Entry(root)
entry.bind("<KeyRelease>", on_key_release)
entry.grid(row=0,column=1)

root.mainloop()

# 回车响应
import tkinter as tk

def print_input(event):
    # 从输入框获取内容并打印
    print(entry.get())

root = tk.Tk()

# 创建一个输入框
entry = tk.Entry(root)

# 将回车键与响应函数绑定
entry.bind('<Return>', print_input)

# 将输入框放置在窗口中
entry.pack()

root.mainloop()

"""

import threading
import time
import tkinter as tk
# from serial_input import *

window_name = ['not in anyone of the windows']*10
window_name = ['语雀','Code']+['not in anyone of the windows']*10
# trigger = [0]*10

# def parseData(angle) -> list[int]:
#     if angle[1] < 20:
#         trigger[1] = True 
#     elif angle[0] < -80:
#         trigger[0] = True
#     else:
#         trigger[0] = False
#         trigger[1] = False
        
def focus(window_name, r=False):
    from pywinauto import Desktop, Application

    # 获取当前桌面
    desktop = Desktop(backend="uia")
    for window in desktop.windows():
        if window_name in window.window_text() :
            if r: # reverse
                window.minimize()
            else:
                window.set_focus()
            break
    else:
        # 如果没有找到匹配的窗口，则打开应用程序
        app = Application()
        try:
            app.start(path_dict[window_name])
        except Exception as e:
            print(e)
            exit(0)

def print_input(event):
    # 从输入框获取内容并打印
    left_command = event.widget.get()
    if left_command[0] != '%%':
        window_name[0] = left_command

def Trigger(code):
    if code[0]=='1':
        focus(window_name[0])
    # root.after(100)  # 每100毫秒调用一次
    
    if code[1]=='0':
        # print_windows()
        focus(window_name[0], r=True)

# Angle = None

class App:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Initial Text")
        self.label.pack()
        
        # Create a thread to update the label
        self.thread = threading.Thread(target=self.update_label)
        self.thread.daemon = True
        global threading_stop
        threading_stop = False
        self.thread.start()

    def update_label(self):
        import serial
        from serial_in import DueData
        global threading_stop
        ser = serial.Serial('com7',115200, timeout=0.5)
        counter = 0 
        while True:
            # Update the label's text
            self.label.config(text=str(time.time()))

            datahex = ser.read(33)
            # global Angle # global 变慢
            Angle = DueData(datahex) 
            if(Angle):
                # counter+=1
                # if counter%20 == 0:
                    # counter = 0
                # print(Angle)
                pass
            Trigger()
            # time.sleep(0.01)
            if threading_stop:
                break
            
        

def main():
    global root, app
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
def shut():
    global threading_stop
    threading_stop = True
    time.sleep(0.1)
    root.destroy()

if __name__ == "__main__":
    main()

