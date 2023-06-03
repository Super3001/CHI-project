import time
import app

mode = "watch"
# mode = "key"
# mode = "split"

task = 1

def Gstart():
    global start
    start = time.time()
    if mode == "watch":
        app.main()
    else:
        pass
    
def Gstop():
    global end
    end = time.time()
    if mode == "watch":
        app.shut()
    using = end - start
    print(f'{mode} task{task}: {using} = {using:.2f}s')
    
def Gtask1():
    global task
    task = 1

def Gtask2():
    global task
    task = 2

import tkinter as tk

# 创建主窗口对象
root = tk.Tk()

# 设置窗口标题
root.title("Exam")
root.geometry('400x300')

# 创建Button组件并添加到窗口中
button1 = tk.Button(root, text="Start!",activebackground='blue', command=Gstart)
button1.pack(pady=10)
button2 = tk.Button(root, text="Finish!", activebackground='blue',command=Gstop)
button2.pack(pady=10)
button1 = tk.Button(root, text="Task1", command=Gtask1)
button1.pack(pady=10)
button2 = tk.Button(root, text="Task2", command=Gtask2)
button2.pack(pady=10)
button2 = tk.Button(root, text="Close", command=exit)
button2.pack(pady=10)

# 进入消息循环
root.mainloop()


