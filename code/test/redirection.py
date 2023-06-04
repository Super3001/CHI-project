import os
import time
import sys
# 打印的内容一方面输出到控制台，另一方面输出到文件作为日志保存
class __redirection__:
    def __init__(self): #定义类属性
        self.buff=''
        self.__console__=sys.stdout

    def write(self, output_stream): #定义写方法 output_stream为运行程序print打印内容
        self.buff+=output_stream

    def to_console(self): #输出到控制台
        sys.stdout=self.__console__
        print(self.buff)

    def to_file(self, file_path): #log输出到指定文件保存
        f=open(file_path,'w')
        sys.stdout=f
        print(self.buff)
        f.close()

    def flush(self):
        self.buff=''

    def reset(self):
        sys.stdout=self.__console__