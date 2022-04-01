import abc


class BaseWorker(abc.ABC):

    @property
    @abc.abstractmethod
    def worker_id(self):
        pass

    @abc.abstractmethod
    def run(self, event, context):
        pass

    def __call__(self, event, context):
        return self.run(event, context)
