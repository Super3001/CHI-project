# trigger_pywin32.py

mode = "anchor"
# mode = "hotkey"

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
    global op, mode
    if mode == "anchor":
        if code[0] == '1':
            if op == 0: 
                focus(0)
                op = 1
            else: 
                focus(0,r=True)
                op = 0
    else:
        if code[0]=='1':
            if op == 0:
                op = 1
                ctrlC()
                
            elif op == 1:
                op=0
                ctrlV()
                
        elif code[1]=='1':
            alt_tab()

        elif code[2] == '1':
            alt_tab_tab()


import win32gui, win32con, win32api
import time
st = time.time()

ls_window_name, path_dict = read_data()
print('len:',len(path_dict))
ls_hwnd = []

for name in ls_window_name:
    hwnd = win32gui.FindWindow(None, name)
    if hwnd == 0:
        win32api.ShellExecute(0, 'open', path_dict[name], '', '', 1)
        time.sleep(0.1)
        hwnd = win32gui.FindWindow(None, name)
    ls_hwnd.append(hwnd)

end = time.time()
print('inital elapsed:', end-st)

def focus(idx, r=False):
    st_ = time.time()
    hwnd = ls_hwnd[idx]
    if hwnd != 0:
        if r: # reverse
            print('reverse')
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        else:
            # print(f'time: {st_}')
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    else:
        # 如果没有找到匹配的窗口，则打开应用程序
        name = ls_window_name[idx]
        win32api.ShellExecute(0, 'open', path_dict[name], '', '', 1)
        time.sleep(0.1)
        ls_hwnd[idx] = win32gui.FindWindow(None, name)

    end_= time.time()
    print('elapsed_:',end_-st_)

def ctrlC():
    # 模拟按下Ctrl键
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)

    # 模拟按下C键
    win32api.keybd_event(ord('C'), 0, 0, 0)

    # 模拟释放C键
    win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_KEYUP, 0)

    # 模拟释放Ctrl键
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

def ctrlV():
    # 模拟按下Ctrl键
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)

    # 模拟按下C键
    win32api.keybd_event(ord('V'), 0, 0, 0)

    # 模拟释放C键
    win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)

    # 模拟释放Ctrl键
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

def alt_tab():
    # 模拟按下Alt键
    win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)

    # 模拟按下Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)

    # 模拟释放Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 模拟释放Alt键
    win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)

def alt_tab_tab():
    # 模拟按下Alt键
    win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)

    # 模拟按下Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)

    # 模拟释放Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 模拟按下Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)

    # 模拟释放Tab键
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 模拟释放Alt键
    win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)

