from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker02(BaseWorker):
    worker_id = 2

    def run_robot(self, message):
        logger.info('Worker02: %s', message)
