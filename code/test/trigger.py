# trigger.py

def read_data():
    with open('code\win\path.txt','r', encoding='utf-8') as f:
        # lines = f.readlines()
        path_dict = {}
        ls_window_name = []
        for line in f.readlines():
            # print(line)
            if len(line) < 2:
                continue
            window_name,path = line.split(': ')
            ls_window_name.append(window_name)
            path = path.replace('\n','')
            path_dict[window_name] = path
    return ls_window_name, path_dict

op = 0
def Trigger(code):
    global op
    if code[0]=='1' and op == 0:
        focus(0)
        op = 1
    # root.after(100)  # 每100毫秒调用一次
    
    elif code[0]=='1' and op == 1:
        # print_windows()
        focus(0, r=True)
        op = 0

import time
st = time.time()

ls_window_name, path_dict = read_data()
print('len:',len(path_dict))
ls_window = [None]*len(ls_window_name)
# 获取当前桌面
from pywinauto import Desktop, Application
desktop = Desktop(backend="uia")
for window in desktop.windows():
    if ls_window_name[0] in window.window_text() :
        ls_window[0] = window
end = time.time()
print('inital elapsed:', end-st)

def focus(idx, r=False):
    st_ = time.time()
    if ls_window[idx] != None:
        if r: # reverse
            ls_window[idx].minimize()
            print('minimize')
        else:
            ls_window[idx].set_focus()
    else:
        # 如果没有找到匹配的窗口，则打开应用程序
        app = Application()
        try:
            app.start(path_dict[ls_window_name[idx]])
        except Exception as e:
            print(e)
            exit(0)
    end_=time.time()
    print('elapsed_:',end_-st_)

# if __name__ == '__main__':
#     focus(0)