import abc


class BaseWorker(abc.ABC):

    @property
    @abc.abstractmethod
    def worker_id(self):
        pass

    @abc.abstractmethod
    def run(self, record):
        pass

    def __call__(self, record):
        return self.run(record)
