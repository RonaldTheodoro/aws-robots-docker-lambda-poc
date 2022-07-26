import abc
import json

from settings import logger


class BaseWorker(abc.ABC):

    @property
    @abc.abstractmethod
    def worker_id(self):
        pass

    @property
    @abc.abstractmethod
    def run_robot(self, message):
        pass

    def run(self, record):
        logger.info('Worker %s', self.worker_id)
        message = json.loads(record['body'])
        self.run_robot(message)

    def __call__(self, record):
        return self.run(record)
