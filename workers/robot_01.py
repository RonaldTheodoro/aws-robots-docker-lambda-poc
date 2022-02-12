from settings import logger

from robots.base_robot import BaseWorker
from robots.worker_register import worker_register


@worker_register
class Worker01(BaseWorker):
    robot_id = 1

    def run(self, event, context):
        logger.info('Worker: %s', self.robot_id)
        logger.info('Event: %s', event)
        logger.info('Context: %s', context)
