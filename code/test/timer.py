import time
import app_test
import tkinter as tk
import tkinter.messagebox as msg

util = "watch"
# util = "key"
# util = "split"

mode = "anchor"
# mode = "hotkey"

task = 1

def Gstart():
    global start
    start = time.time()
    if util == "watch":
        app_test.main()
    else:
        pass
    
def Gstop():
    global end
    end = time.time()
    if util == "watch":
        app_test.shut()
    using = end - start
    print(f'utility: {util} task{task}: {using} = {using:.2f}s')
    
def Gtask1():
    global task
    task = 1
    msg.showinfo('','已设置为task1')

def Gtask2():
    global task
    task = 2
    msg.showinfo('','已设置为task2')

def Gclose():
    if util == "watch":
        app_test.shut()
    time.sleep(0.1)
    exit()


# 创建主窗口对象
root = tk.Tk()

# 设置窗口标题
root.title("Exam")
root.geometry('500x400')

# 创建Button组件并添加到窗口中
button1 = tk.Button(root, text="Start!",activebackground='blue', command=Gstart)
button1.pack(pady=10)
button2 = tk.Button(root, text="Finish!", activebackground='green',command=Gstop)
button2.pack(pady=10)
button1 = tk.Button(root, text="Task1", command=Gtask1)
button1.pack(pady=10)
button2 = tk.Button(root, text="Task2", command=Gtask2)
button2.pack(pady=10)
button2 = tk.Button(root, text="Close", command=Gclose)
button2.pack(pady=10)

# 进入消息循环
root.mainloop()