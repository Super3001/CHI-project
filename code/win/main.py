
import tkinter as tk

window_name = ['not in anyone of the windows']*10
trigger = [0]*10

def focus(window_name):
    from pywinauto import Desktop, Application

    # 获取当前桌面
    desktop = Desktop(backend="uia")
    for window in desktop.windows():
        if window_name in window.window_text() :
            window.set_focus()
            break
    else:
        # 如果没有找到匹配的窗口，则打开应用程序
        app = Application()
        print('not found window')

def print_input(event):
    # 从输入框获取内容并打印
    left_command = event.widget.get()
    if left_command[0] != '%%':
        window_name[0] = left_command

root = tk.Tk()

# 创建一个输入框
entry = tk.Entry(root)

# 将回车键与响应函数绑定
entry.bind('<Return>', print_input)

# 将输入框放置在窗口中
entry.grid()

root.mainloop()

import tkinter as tk

def continuous_function1():
    # 在此处编写您需要持续执行的代码
    print("hello")
    root.after(100, continuous_function1)  # 每100毫秒调用一次

def continuous_function2(i):
    # 在此处编写您需要持续执行的代码
    print("hi")
    if i % 10 == 0:
        trigger[0] = True
    else:
        trigger[0] = False
    root.after(100, continuous_function2, i+1)  # 每100毫秒调用一次
    
def continuous_function3():
    # 在此处编写您需要持续执行的代码
    print('ok')
    if trigger[0]:
        focus(window_name[0])
    root.after(100, continuous_function3)  # 每100毫秒调用一次

root = tk.Tk()
root.after(100, continuous_function1)  # 启动函数
root.after(100, continuous_function2, 0)  # 启动函数
root.after(100, continuous_function3)  # 启动函数
root.mainloop()
