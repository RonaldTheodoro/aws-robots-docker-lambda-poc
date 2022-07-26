from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker03(BaseWorker):
    worker_id = 3

    def run_robot(self, message):
        logger.info('Worker03: %s', message)


