# pywin32_test.py

import win32gui, win32con, win32api

# 打开记事本应用程序
hwnd = win32gui.FindWindow(None, '语雀')
if hwnd == 0:
    # 打开记事本应用程序
    win32api.ShellExecute(0, 'open', r'C:\Users\songy\AppData\Local\Programs\yuque-desktop\语雀.exe', '', '', 1)
else:
    # 最小化应用程序窗口
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    print('打开应用程序')