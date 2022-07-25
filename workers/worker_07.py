from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker07(BaseWorker):
    worker_id = 7

    def run(self, event, context):
        logger.info('Worker 07')
        logger.info('Event: %s', event)
