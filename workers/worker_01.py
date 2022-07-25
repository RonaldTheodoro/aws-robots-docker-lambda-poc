from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker01(BaseWorker):
    worker_id = 1

    def run(self, event, context):
        logger.info('Worker 01')
        logger.info('Event: %s', event)
