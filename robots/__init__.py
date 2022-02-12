from robots.robot_01 import Robot01
from robots.robot_02 import Robot02
from robots.robot_03 import Robot03
from robots.robot_04 import Robot04
from robots.robot_05 import Robot05
from robots.robot_06 import Robot06
from robots.robot_07 import Robot07
from robots.robot_08 import Robot08
from robots.robot_09 import Robot09
from robots.robot_10 import Robot10


robots = {
    1: Robot01,
    2: Robot02,
    3: Robot03,
    4: Robot04,
    5: Robot05,
    6: Robot06,
    7: Robot07,
    8: Robot08,
    9: Robot09,
    10: Robot10,
}


def get_robot_by_id(robot_id):
    if robot_id not in robots:
        raise Exception(f'Robot {robot_id} not found')
    return robots[robot_id]
