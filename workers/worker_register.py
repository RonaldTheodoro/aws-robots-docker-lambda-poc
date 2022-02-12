class WorkerRegister:
    __workers = {}

    def __call__(self, robot_cls):
        self.__workers[robot_cls.robot_id] = robot_cls
        return robot_cls

    def get_robot_by_id(self, robot_id):
        if robot_id not in self.__workers:
            raise Exception(f'Worker {robot_id} not found')
        return self.__workers[robot_id]


worker_register = WorkerRegister()
