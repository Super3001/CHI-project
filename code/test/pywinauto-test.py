from pywinauto import Desktop, Application
import time

app = Application()
try:
    app.start(r'C:\Users\songy\AppData\Local\Programs\yuque-desktop\语雀.exe')
except Exception as e:
    print(e)
    exit(0)

time.sleep(1)
# 获取当前桌面上的所有顶层窗口
windows = Desktop(backend="uia").windows()

# 遍历每个窗口并检查其状态
for window in windows:
    # 检查窗口是否可见且已启用
    if window.is_visible() and window.is_enabled():
        # 检查窗口的状态是否为“焦点”
        if window.has_keyboard_focus():
            print(f"{window.window_text()} 是焦点窗口")
        else:
            print(f"{window.window_text()} 不是焦点窗口")
