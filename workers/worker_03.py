from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker03(BaseWorker):
    worker_id = 3

    def run(self, record):
        logger.info('Worker %s', self.worker_id)
        logger.info('Record: %s', record)

