from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker05(BaseWorker):
    worker_id = 5

    def run(self, event, context):
        logger.info('Worker 05')
        logger.info('Event: %s', event)
        raise Exception('Worker 05')
