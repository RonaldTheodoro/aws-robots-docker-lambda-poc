from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class WorkerCron(BaseWorker):
    worker_id = 'cron'

    def run_robot(self, message):
        logger.info('WorkerCron: %s', message)

