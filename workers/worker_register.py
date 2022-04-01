class WorkerRegister:
    __workers = {}

    def __call__(self, worker_cls):
        self.__workers[worker_cls.worker_id] = worker_cls
        return worker_cls

    def get_worker_by_id(self, worker_id):
        if worker_id not in self.__workers:
            raise Exception(f'Worker {worker_id} not found')
        return self.__workers[worker_id]


worker_register = WorkerRegister()
