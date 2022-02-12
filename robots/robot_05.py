import logging

from robots.base_robot import BaseRobot
from robots.robot_register import robot_register


@robot_register
class Robot05(BaseRobot):
    robot_id = 5

    def run(self, event, context):
        logging.error('Robot: %s', self.robot_id)
        logging.error('Event: %s', event)
        logging.error('Context: %s', context)
