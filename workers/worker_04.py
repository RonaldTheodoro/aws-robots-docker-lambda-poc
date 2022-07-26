from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker04(BaseWorker):
    worker_id = 4

    def run_robot(self, message):
        logger.info('Worker04: %s', message)

