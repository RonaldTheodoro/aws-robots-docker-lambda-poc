import logging

from robots.base_robot import BaseRobot


class Robot04(BaseRobot):
    robot_id = 4

    def run(self, event, context):
        logging.error('Robot: %s', self.robot_id)
        logging.error('Event: %s', event)
        logging.error('Context: %s', context)
