# 平动方式函数

def translation(angle, moving_state, height):  # angle:目标方向，state:目前机器人状态,height:设定高度
    nextstep = []
    if moving_state == 0:
