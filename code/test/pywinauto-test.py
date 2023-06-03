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
    # app = Application()
    windows = desktop.windows()
    for window in windows:
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
    
    get_last_accessed_window()
    
print_windows()
