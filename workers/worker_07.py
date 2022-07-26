from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker07(BaseWorker):
    worker_id = 7

    def run_robot(self, message):
        logger.info('Worker07: %s', message)

