import pathlib

from decouple import config
from decouple import Choices


class Settings:
    BASE_DIR = pathlib.Path(__file__).parent.parent
    STAGE = config('STAGE', cast=Choices(['local', 'dev', 'homolog', 'prod']))
    ACCOUNT_ID = config('ACCOUNT_ID')
    REGION: config('REGION', cast=Choices(['us-east-1', 'us-east-2']))

    @property
    def extras(self):
        return self.BASE_DIR / 'extras'

    @property
    def payloads(self):
        return self.BASE_DIR / '.payloads'

    @property
    def is_local(self):
        return self.STAGE == 'local'

    @property
    def is_dev(self):
        return self.STAGE == 'dev'

    @property
    def is_homolog(self):
        return self.STAGE == 'homolog'

    @property
    def is_prod(self):
        return self.STAGE == 'prod'

    @property
    def is_aws(self):
        return any([self.is_dev, self.is_homolog, self.is_prod])


settings = Settings()
