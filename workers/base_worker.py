import abc
import json

import requests

from settings import settings


class BaseWorker(abc.ABC):
    session = requests.Session()
    xpath_json = None
    xpaths = None

    def __init__(self):
        if self.xpath_json is not None:
            self.xpaths = self.get_xpaths()


    @property
    @abc.abstractmethod
    def robot_id(self):
        pass

    @abc.abstractmethod
    def run(self, event, context):
        pass

    def get_xpaths(self):
        xpath_json_path = settings.extras / f'xpaths/{self.xpath_json}.json'
        with xpath_json_path.open(mode='r') as fp_json:
            return json.load(fp_json)

    def __call__(self, event, context):
        return self.run(event, context)
