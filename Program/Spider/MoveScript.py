from Spider import SpiderObject
import time
from Library import caculater

def update_all(self):
    time.sleep(0.5)
    self.spider.calculate_all_cod()
    self.update_spider_image()
    self.update_all_foot_image()
    self.update_joint_angle()
    self.update_joint_angle_to_message()


def change_support_state(self, state):
    """
    state : 0为1,3,5支撑;1为2,4,6支撑
    """
    if state == 0:
        self.spider.Leg1.fixed_state = True
        self.spider.Leg3.fixed_state = True
        self.spider.Leg5.fixed_state = True
        self.spider.Leg1.root_height = 50
        self.spider.Leg3.root_height = 50
        self.spider.Leg5.root_height = 50
        self.spider.Leg2.fixed_state = False
        self.spider.Leg4.fixed_state = False
        self.spider.Leg6.fixed_state = False
        self.spider.Leg2.root_height = 30
        self.spider.Leg4.root_height = 30
        self.spider.Leg6.root_height = 30
    if state == 1:
        self.spider.Leg1.fixed_state = False
        self.spider.Leg3.fixed_state = False
        self.spider.Leg5.fixed_state = False
        self.spider.Leg1.root_height = 30
        self.spider.Leg3.root_height = 30
        self.spider.Leg5.root_height = 30
        self.spider.Leg2.fixed_state = True
        self.spider.Leg4.fixed_state = True
        self.spider.Leg6.fixed_state = True
        self.spider.Leg2.root_height = 50
        self.spider.Leg4.root_height = 50
        self.spider.Leg6.root_height = 50


def forward_script(self, Spider: SpiderObject):
    # 开始进行支撑
    update_all(self)
    change_support_state(self, 1)
    update_all(self)

    for i in range(0, 5):
        self.spider.move_spider([0, 30], 90)
        self.spider.Leg1.mov_foot_point([0, 60])
        self.spider.Leg3.mov_foot_point([0, 60])
        self.spider.Leg5.mov_foot_point([0, 60])
        update_all(self)

        change_support_state(self, 0)
        update_all(self)

        self.spider.move_spider([0, 30], 90)
        print(self.spider.center_position)
        self.spider.Leg2.mov_foot_point([0, 60])
        self.spider.Leg4.mov_foot_point([0, 60])
        self.spider.Leg6.mov_foot_point([0, 60])
        update_all(self)

        change_support_state(self, 1)
        update_all(self)


def backward_script(self, Spider: SpiderObject):
    # 开始进行支撑

    update_all(self)
    change_support_state(self, 1)
    update_all(self)

    for i in range(0, 5):
        self.spider.move_spider([0, -30], 90)
        self.spider.Leg1.mov_foot_point([0, -60])
        self.spider.Leg3.mov_foot_point([0, -60])
        self.spider.Leg5.mov_foot_point([0, -60])
        update_all(self)

        change_support_state(self, 0)
        update_all(self)

        self.spider.move_spider([0, -30], 90)
        print(self.spider.center_position)
        self.spider.Leg2.mov_foot_point([0, -60])
        self.spider.Leg4.mov_foot_point([0, -60])
        self.spider.Leg6.mov_foot_point([0, -60])
        update_all(self)

        change_support_state(self, 1)
        update_all(self)


def turn_right_script(self, Spider: SpiderObject):
    update_all(self)
    change_support_state(self, 1)
    update_all(self)

    for i in range(0, 12):
        self.spider.move_spider([0, 0], self.spider.forward + 15)
        self.spider.Leg1.route_foot_point(-40,150)
        self.spider.Leg3.route_foot_point(-40,150)
        self.spider.Leg5.route_foot_point(-40,150)
        update_all(self)
        change_support_state(self, 0)
        update_all(self)

        self.spider.move_spider([0, 0], self.spider.forward + 15)
        print(self.spider.center_position)
        self.spider.Leg2.route_foot_point(-40,150)
        self.spider.Leg4.route_foot_point(-40,150)
        self.spider.Leg6.route_foot_point(-40,150)
        update_all(self)

        change_support_state(self, 1)
        update_all(self)


def turn_left_script(self, Spider: SpiderObject):
    update_all(self)
    change_support_state(self, 1)
    update_all(self)

    for i in range(0, 12):
        self.spider.move_spider([0, 0], self.spider.forward - 15)
        self.spider.Leg1.route_foot_point(40, 150)
        self.spider.Leg3.route_foot_point(40, 150)
        self.spider.Leg5.route_foot_point(40, 150)
        update_all(self)
        change_support_state(self, 0)
        update_all(self)

        self.spider.move_spider([0, 0], self.spider.forward - 15)
        print(self.spider.center_position)
        self.spider.Leg2.route_foot_point(40, 150)
        self.spider.Leg4.route_foot_point(40, 150)
        self.spider.Leg6.route_foot_point(40, 150)
        update_all(self)

        change_support_state(self, 1)
        update_all(self)
