from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker09(BaseWorker):
    worker_id = 9

    def run(self, event, context):
        logger.info('Worker 09')
        logger.info('Event: %s', event)
