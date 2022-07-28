from logger import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class Worker05(BaseWorker):
    worker_id = 5

    def run_robot(self, message):
        logger.info('Worker05: %s', message)
        raise Exception()


