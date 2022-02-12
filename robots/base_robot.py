import abc


class BaseRobot(abc.ABC):
    @property
    @abc.abstractmethod
    def robot_id(self):
        pass

    @abc.abstractmethod
    def run(self, event, context):
        pass

    def __call__(self, event, context):
        return self.run(event, context)
