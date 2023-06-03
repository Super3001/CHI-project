from pywinauto import Desktop

# 获取当前桌面
desktop = Desktop(backend="uia")

# 获取最前面的窗口
window = desktop.windows()[0]

"""
# 输出窗口标题和类名
print(window.window_text())
print(window.class_name())

# 所有窗口？
for window in desktop.windows():
    print(window)
    

from pywinauto import Desktop

# 获取当前桌面
desktop = Desktop(backend="uia")

# 获取最前面的窗口
window = desktop.windows()[5]
print(window)

# 将窗口置于最前面
window.set_focus()
"""

from pywinauto import Desktop, Application

# 获取当前桌面
desktop = Desktop(backend="uia")

# 获取用户输入的窗口名
window_name = input("请输入窗口名：")

# 遍历所有窗口，找到匹配的窗口，并将其置于最前面
for window in desktop.windows():
    if  window_name in window.window_text() :
        window.set_focus()
        break
else:
    # 如果没有找到匹配的窗口，则打开应用程序
    path_dict = {}
    app = Application().start(path_dict[window_name])

