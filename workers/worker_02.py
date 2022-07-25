from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker02(BaseWorker):
    worker_id = 2

    def run(self, event, context):
        logger.info('Worker 02')
        logger.info('Event: %s', event)
