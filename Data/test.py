import json
from data_find import *


if __name__ == '__main__':
    data = data_find()
    print(data.find_angle( 156,181 ))
    print(data.find_lh(0 , 90))
    print(data.find_lh(170 , 72))