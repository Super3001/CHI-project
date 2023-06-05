# serial_in_test.py

ACCData=[0.0]*8
GYROData=[0.0]*8
AngleData=[0.0]*8          
FrameState = 0            #通过0x后面的值判断属于哪一种情况
Bytenum = 0               #读取到这一段的第几位
CheckSum = 0              #求和校验位         
 
a = [0.0]*3
w = [0.0]*3
Angle = [0.0]*3
ls_pre = []
flag = 0
def DueData(inputdata):   #新增的核心程序，对读取的数据进行划分，各自读到对应的数组里
    global  FrameState    #在局部修改全局变量，要进行global的定义
    global  Bytenum
    global  CheckSum
    global  a
    global  w
    global  Angle
    if len(inputdata) > 0:
        print(list(inputdata))
    for data in inputdata:  #在输入的数据进行遍历
        if FrameState==0:   #当未确定状态的时候，进入以下判断
            if data==0x55 and Bytenum==0: #0x55位于第一位时候，开始读取数据，增大bytenum
                CheckSum=data
                Bytenum=1
                continue
            elif data==0x51 and Bytenum==1:#在byte不为0 且 识别到 0x51 的时候，改变frame
                CheckSum+=data
                FrameState=1
                Bytenum=2
            elif data==0x52 and Bytenum==1: #同理
                CheckSum+=data
                FrameState=2
                Bytenum=2
            elif data==0x53 and Bytenum==1:
                CheckSum+=data
                FrameState=3
                Bytenum=2
        elif FrameState==1: # acc    #已确定数据代表加速度
            if Bytenum<10:            # 读取8个数据
                ACCData[Bytenum-2]=data # 从0开始
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):  #假如校验位正确
                    a = get_acc(ACCData)
                CheckSum=0                  #各数据归零，进行新的循环判断
                Bytenum=0
                FrameState=0
        elif FrameState==2: # gyro
            if Bytenum<10:
                GYROData[Bytenum-2]=data
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):
                    w = get_gyro(GYROData)
                CheckSum=0
                Bytenum=0
                FrameState=0
        elif FrameState==3: # angle
            if Bytenum<10:
                AngleData[Bytenum-2]=data
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):
                    Angle = get_angle(AngleData)
                    d = a+w+Angle
                    # print("a(g):%10.3f %10.3f %10.3f w(deg/s):%10.3f %10.3f %10.3f Angle(deg):%10.3f %10.3f %10.3f"%d)
                    # print("Angle(deg):%10.3f %10.3f %10.3f"%Angle)
                    CheckSum=0
                    Bytenum=0
                    FrameState=0
                    return d
                CheckSum=0
                Bytenum=0
                FrameState=0
    CheckSum=0
    Bytenum=0
    FrameState=0
            
# 统一判断标准
def parseData(d) -> str:
    global pos
    if pos == 0:
        # if angle[2] < pre_angle[2]-40 and angle[1] > pre_angle[1]: # 主手势（左转手腕）角度触发
        if d[4] < -100: # wy < -150 主手势 角速度触发
            pos = 1
            return '100'
        # if d[6] < 1 and d[8] < 1:  # ax < 1, az < 1: 抬起手臂（辅助手势1）
        if d[5] < -50 and d[3] > 50 :  # wz < -50 and wx > 50: 辅助手势1
            pos = 2
            return '010'
        # if d[6] < 0.5 and d[8] > 1: # 辅助手势2
        if d[4] > 0 and d[5] < -100: # wy>0, wz<-100: 内扣手臂（辅助手势2）
            pos = 3
            return '001'
    elif pos == 1: # 需要复位
        if d[4] > 100:
            pos = 0
            return 'rst'
    elif pos == 2:
        if d[5] > 50 and d[3] < 50: # w（角速度）复位
            pos = 0
            return 'rst'
        # if d[6] > 1 and d[8] > 1: # acc（加速度）复位
            # pos = -1 # 进入unknown状态
    elif pos == 3:
        if d[4] < 0 and d[5] > 100: # w（角速度）复位
            pos = 0
            return 'rst'
        # if d[6] > 1 and d[8] > 1: # acc（加速度）复位
            # pos = -1
    elif pos < 0: # acc复位延迟处理
        if pos == -3: # 静止三次，真正复位  ACC_RST_TIME = 3
            pos = 0
            return 'rst'
        elif d[6] > 1 and d[8] > 1:
            pos = pos-1
        else:
            pos = -1
    return '000' # 注意：默认返回'000'

import time
t_last = 0
SET_INTERVAL = 0.3
pos = 0

# 防抖功能
def remove_shake(code):
    global t_last
    if code!='000':
        now = time.time()
        interval = now - t_last
        if(interval < SET_INTERVAL):    
            code = '000'
        t_last = now
    return code

def get_acc(datahex):  
    axl = datahex[0]                                        
    axh = datahex[1]
    ayl = datahex[2]                                        
    ayh = datahex[3]
    azl = datahex[4]                                        
    azh = datahex[5]
    
    k_acc = 16.0
 
    acc_x = (axh << 8 | axl) / 32768.0 * k_acc
    acc_y = (ayh << 8 | ayl) / 32768.0 * k_acc
    acc_z = (azh << 8 | azl) / 32768.0 * k_acc
    if acc_x >= k_acc:
        acc_x -= 2 * k_acc
    if acc_y >= k_acc:
        acc_y -= 2 * k_acc
    if acc_z >= k_acc:
        acc_z-= 2 * k_acc
    
    return acc_x,acc_y,acc_z
 
def get_gyro(datahex):  
    wxl = datahex[0]                                        
    wxh = datahex[1]
    wyl = datahex[2]                                        
    wyh = datahex[3]
    wzl = datahex[4]                                        
    wzh = datahex[5]
    k_gyro = 2000.0
 
    gyro_x = (wxh << 8 | wxl) / 32768.0 * k_gyro
    gyro_y = (wyh << 8 | wyl) / 32768.0 * k_gyro
    gyro_z = (wzh << 8 | wzl) / 32768.0 * k_gyro
    if gyro_x >= k_gyro:
        gyro_x -= 2 * k_gyro
    if gyro_y >= k_gyro:
        gyro_y -= 2 * k_gyro
    if gyro_z >=k_gyro:
        gyro_z-= 2 * k_gyro
    return gyro_x,gyro_y,gyro_z
 
def get_angle(datahex):   
    print(str(datahex))                              
    rxl = datahex[0]                                        
    rxh = datahex[1]
    ryl = datahex[2]                                        
    ryh = datahex[3]
    rzl = datahex[4]                                        
    rzh = datahex[5]
    k_angle = 180.0
 
    angle_x = (rxh << 8 | rxl) / 32768.0 * k_angle
    angle_y = (ryh << 8 | ryl) / 32768.0 * k_angle
    angle_z = (rzh << 8 | rzl) / 32768.0 * k_angle
    if angle_x >= k_angle:
        angle_x -= 2 * k_angle
    if angle_y >= k_angle:
        angle_y -= 2 * k_angle
    if angle_z >=k_angle:
        angle_z-= 2 * k_angle
 
    return angle_x,angle_y,angle_z


# import queue
# qdata = queue.Queue()
from autoqueue import AutoQueue # 手写类
qdata = AutoQueue(5) # 手写自用队列
cnt_static = 0
# 静态自动校正功能
STATIC_NUM = 100
def alter(code, angle_data):
    global cnt_static
    if code == '000' and pos == 0:
        cnt_static+=1
        qdata.enqueue(angle_data)
    else:
        cnt_static=0
    if cnt_static>=STATIC_NUM: # 连续10个静态数据，进行静态数据校准
        pre_angle=qdata.average()
        print(f'altered({STATIC_NUM} turns): {pre_angle}')
        cnt_static=0

flag = 0
ls_pre = []
pre_d = [0] * 9
def get_d_initial(i, d):
    global flag
    if i >= 5:
        ls_pre.append(d)
    elif i == 10:
        for j in range(9):
            pre_d[j] = sum([x[j] for x in ls_pre]) / len(ls_pre)
        flag = 1

def main():
    import serial, time
    ser = serial.Serial('com9',115200, timeout=0) 
    print(ser.is_open)
    cnt = 0
    while(1):
        datahex = ser.read(33)
        d = DueData(datahex) # d: a + w + angle
        # if serial not return data
        if not d:
            continue
        if cnt <= 10:
            get_d_initial(cnt, d)
        print(d)
        sts=parseData(d)
        alter(sts, d)
        sts = remove_shake(sts)
        # if cnt > 10:
        #     print(d[6:9])
        print(sts)
        cnt+=1
        if(cnt%100 == 0):
            try:
                # ser.close()
                # ser = serial.Serial('com7',115200, timeout=0.5)
                # ser.open()
                pass
            except:
                raise ValueError('serial down')
                
        time.sleep(0.01)
    ser.close()

if __name__ == '__main__':
    main()