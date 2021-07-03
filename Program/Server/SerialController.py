import serial
import time


class SerialController:
    def __init__(self):
        self.open_ser()

    # 串口打开函数
    def open_ser(self):
        port = '/dev/serial0'  # 串口号
        baudrate = 115200  # 波特率
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            if (self.ser.isOpen() == True):
                print("串口打开成功")
        except Exception as exc:
            print("串口打开异常", exc)

    # 数据发送
    def send_msg(self, angle):

        pwm_value = [i * 11.11 + 500 for i in angle]
        strs = '{'
        for i in range(0, len(pwm_value)):
            if i < 10:
                if pwm_value[i] < 1000:
                    strs = strs + '#00' + str(i) + 'P' + '0' + str(int(pwm_value[i])) + 'T1000!'
                else:
                    strs = strs + '#00' + str(i) + 'P' + str(int(pwm_value[i])) + 'T1000!'
            else:
                if pwm_value[i] < 1000:
                    strs = strs + '#0' + str(i) + 'P' + '0' + str(int(pwm_value[i])) + 'T1000!'
                else:
                    strs = strs + '#0' + str(i) + 'P' + str(int(pwm_value[i])) + 'T1000!'
        strs = strs + '}'
        send_datas = strs
        self.ser.write(send_datas.encode())
        print("已发送数据:", send_datas)


if __name__ == '__main__':
    Ser_controller = SerialController()
