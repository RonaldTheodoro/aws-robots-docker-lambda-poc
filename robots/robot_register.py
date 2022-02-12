class RobotRegister:
    __robots = {}

    def __call__(self, robot_cls):
        self.__robots[robot_cls.robot_id] = robot_cls
        return robot_cls

    def get_robot_by_id(self, robot_id):
        if robot_id not in self.__robots:
            raise Exception(f'Robot {robot_id} not found')
        return self.__robots[robot_id]


robot_register = RobotRegister()
