import logging

from robots.base_robot import BaseRobot
from robots.robot_register import robot_register


@robot_register
class Robot02(BaseRobot):
    robot_id = 2

    def run(self, event, context):
        logging.error('Robot: %s', self.robot_id)
        logging.error('Event: %s', event)
        logging.error('Context: %s', context)
        raise Exception('An expected error')
