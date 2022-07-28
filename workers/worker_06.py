from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker06(BaseWorker):
    worker_id = 6

    def run_robot(self, message):
        logger.info('Worker06: %s', message)


