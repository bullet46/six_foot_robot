from flask import Flask, request
from SerialController import SerialController
import ast

# Flask框架
app = Flask(__name__)
#
# ser_device = SerialController()
# 创建全局变量 目前所有角度
now_angle = [None] * 20
ser_controller = SerialController()
now_angle[:18] = [90, 90, 90, 89, 90, 90, 99, 99, 99, 99, 99, 99, 109, 108, 108, 109, 109, 108]
now_angle[18:] = [45, 90]
angle_bias = [-5, 6, -10, -4, -5, 5, 11, 6, 16, 0, 11, 0, -4, -18, -13, 0, -4, 0, 0, 0]


def list_add(a, b):
    c = []
    for i in range(len(a)):
        c.append(max(0, min(a[i] + b[i], 180)))  # 限制偏差角
    return c


@app.route("/", methods=["GET"])
def body_update():
    try:
        if request.method == "GET":
            body_angle_list_str = request.args.get('body_angle')
            cap_angle_list_str = request.args.get('cap_angle')
            global now_angle
            if body_angle_list_str is not None:
                body_angle_list = ast.literal_eval(body_angle_list_str)
                now_angle[:18] = body_angle_list
            if cap_angle_list_str is not None:
                cap_angle_list = ast.literal_eval(cap_angle_list_str)
                now_angle[18:] = cap_angle_list
            now_angle = list_add(now_angle, angle_bias)
            print(now_angle)

            # ser_controller.send_msg(now_angle)
            return 'finish'
    except Exception as e:
        print(e)


@app.route("/get_temp", methods=["GET"])
def get_temp():
    try:
        file = open("/sys/class/thermal/thermal_zone0/temp")
        # 读取结果，并转换为浮点数
        temp = float(file.read()) / 1000
        # 关闭文件
        file.close()
        return temp
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 串口通信对象
    app.run(host="0.0.0.0", port=9600, debug=True)
