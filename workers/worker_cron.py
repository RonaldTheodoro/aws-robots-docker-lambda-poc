from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class WorkerCron(BaseWorker):
    worker_id = 'cron'

    def run(self, event, context):
        logger.info('Worker cron')
        logger.info('Event: %s', event)
