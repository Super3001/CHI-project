# subprocess_main.py

import subprocess

# 启动另一个Python脚本，并将其标准输出流重定向到管道
p = subprocess.Popen(['python', 'code/test/subprocess_test.py'], stdout=subprocess.PIPE)

# 读取其他脚本的输出，并实时处理每一行
for i, line in enumerate(iter(p.stdout.readline, b'')):
    # 处理每一行输出
    print(f'{i}: ',end='')
    print(line.decode('utf-8').strip())

# 等待子进程结束
p.wait()

# 获取其他脚本的返回值
return_code = p.returncode