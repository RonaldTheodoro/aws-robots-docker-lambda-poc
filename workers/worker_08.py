from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker08(BaseWorker):
    worker_id = 8

    def run(self, event, context):
        logger.info('Worker 08')
        logger.info('Event: %s', event)
