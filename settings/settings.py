import pathlib

from decouple import config
from decouple import Choices


class Settings:
    BASE_DIR = pathlib.Path(__file__).parent.parent
    STAGE = config('STAGE', cast=Choices(['local', 'prod']))

    @property
    def is_local(self):
        return self.STAGE == 'local'

    @property
    def is_prod(self):
        return self.STAGE == 'prod'

    @property
    def is_aws(self):
        return any([self.is_prod])


settings = Settings()
