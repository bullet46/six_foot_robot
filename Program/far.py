import requests

from Cilent.Spider.Config import *

if __name__ == '__main__':
    angle_list = [110] * 18
    param = {
        'body_angle': str(angle_list)
    }
    req = requests.get(f"http://192.168.1.2:9600", params=param)
    print(req.text)