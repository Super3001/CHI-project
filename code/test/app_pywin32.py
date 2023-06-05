# app_pywin32.py

import time
import tkinter as tk
import threading
from serial_in_test import *
from trigger_pywin32 import Trigger

flog = open('flog.txt','a')
def log(s):
    flog.write(s + '\n')

p_stop = False
class App:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Initial Text")
        self.label.pack()
        master.geometry('200x200')
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        global threading_stop
        threading_stop = False
        self.button = tk.Button(self.master,width=100,height=2,activebackground='green',text="开始",command=self.thread.start)
        self.button.pack(pady=10)
        self.quitbt = tk.Button(self.master,width=100,height=2, activebackground="red",text='退出',command=self.quit)
        self.quitbt.pack(pady=10)

    def run(self):
        import serial
        ser = serial.Serial('com7',115200, timeout=1) 
        print('open',ser.is_open)
        print('baudrate',ser.baudrate)
        print('timeout',ser.timeout)
        cnt = 0
        while(1):
            log(str(time.time()) + '  ' + str(ser.readable()))
            datahex = ser.read(33)
            log(str(datahex))
            d = DueData(datahex) # d: a + w + angle
            log(str(d))
            log('')
            # if serial not return data
            if not d:
                continue
            if cnt <= 10:
                get_d_initial(cnt, d)
            sts = parseData(d)
            alter(sts, d)
            sts = remove_shake(sts)
            # if cnt > 10:
            #     print(d[6:9])
            try:
                if sts == '000':
                    self.label.config(text=str(sts),fg='black')
                elif sts == 'rst':
                    self.label.config(text=str(sts),fg="blue")
                else:
                    self.label.config(text=str(sts),fg="red")
            except:
                raise ValueError('no tkinter')
            
            Trigger(sts)
            
            cnt+=1
            time.sleep(0.01)
        ser.close()

    def run_1(self):
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
        if type(code) == str and len(code)==3:
            print(code, end=' ')
            Trigger(code)
        else:
            print(code)
            
    def quit(self):
        global threading_stop
        threading_stop = True
        time.sleep(0.1)
        try:
            root.destroy()
        except:
            print('destroyed')
    

def main():
    global root, app
    root = tk.Tk()
    app = App(root)
    root.mainloop()

def shut(p):
    global p_stop
    p_stop = True
    time.sleep(0.1)
    flog.close()
    try:
        root.destroy()
    except:
        print('destroyed')
        pass



if __name__ == "__main__":
    main()

