from robots.base_robot import BaseRobot
from robots.robot_register import robot_register
from settings import logger


@robot_register
class Robot02(BaseRobot):
    robot_id = 2

    def run(self, event, context):
        logger.info('Robot: %s', self.robot_id)
        logger.info('Event: %s', event)
        logger.info('Context: %s', context)
        raise Exception('An expected error')
