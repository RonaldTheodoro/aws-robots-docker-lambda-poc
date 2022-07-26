from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker10(BaseWorker):
    worker_id = 10

    def run_robot(self, message):
        logger.info('Worker10: %s', message)


