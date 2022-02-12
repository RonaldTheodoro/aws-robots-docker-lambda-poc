from settings import logger

from robots.base_robot import BaseRobot
from robots.robot_register import robot_register


@robot_register
class Robot01(BaseRobot):
    robot_id = 1

    def run(self, event, context):
        logger.info('Robot: %s', self.robot_id)
        logger.info('Event: %s', event)
        logger.info('Context: %s', context)
