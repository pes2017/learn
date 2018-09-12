# ----------------------------------------- #

# 网站：http://www.pesmaster.com/
# 目的：抽取16879个球员的数据

# ----------------------------------------- #
from urllib import request
import re

# 抽取URL
class Spider_url(object):

    # 模板
    url_pattern = '<a target="_blank" class="namelink" href="([\s\S]*?)">'

    # 抽取HTML
    def __fetch_htmls(self, url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding = 'utf-8')
        return htmls

    # 从HTML中抽取URL
    def __get_urls(self, htmls):
        urls = re.findall(Spider_url.url_pattern, htmls)
        for number, url in enumerate(urls):
            url = 'http://www.pesmaster.com{}'.format(url)
            urls[number] = url
        return urls

    # 抽取全部URL // 共16879个
    def all_urls(self):
        all_url_list = []
        for i in range(1, 563):
            url = 'http://www.pesmaster.com/pes-2019/search/search.php?page={}'.format(i)
            htmls = self.__fetch_htmls(url)
            all_url_list += self.__get_urls(htmls)
        return all_url_list

class Spider_content(object):
    pass

if __name__ == '__main__':
    s = Spider_url()
    s.all_urls()


