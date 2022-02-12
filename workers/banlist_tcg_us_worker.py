import lxml.html
from settings import logger

from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


@worker_register
class BanlistTCGUSWorker(BaseWorker):
    robot_id = 1
    url_base = 'https://www.yugioh-card.com'
    url_page = f'{url_base}/en/limited/'

    xpath_json = 'banlist_tcg_us_xpath'

    def run(self, event, context):
        response = self.session.get(self.url_page)
        response.raise_for_status()

        root = lxml.html.fromstring(response.content, base_url=self.url_base)
        root.make_links_absolute()

        rows = root.xpath('//table//tr[contains(@class, "monster") or contains(@class, "effect") or contains(@class, "fusion") or contains(@class, "link") or contains(@class, "synchro") or contains(@class, "xyz") or contains(@class, "spell") or contains(@class, "trap")]')
        for row in rows:
            print(row.xpath('./td[1]/text()'))
            print(row.xpath('./td[2]/text()'))
            print(row.xpath('./td[3]/text()'))
            print(row.xpath('./td[4]/text()'))

