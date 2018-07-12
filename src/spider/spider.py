import re
import json
from urllib import request
from camel_and_snake import Converter

# 爬虫库 BeautifulSoup
# 爬虫框架 Scrapy
# 爬虫、反爬虫、反反爬虫
# ip 封

class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_p = r'<div\s*class="video-info">\s*([\s\S]*?)\s*</div>'
    data_p = r'<span\s*class="video-title"[\s\S]*?>\s*([\s\S]*?)\s*</span>\s*' \
             r'<span\s*class="video-nickname"[\s\S]*?</i>\s*([\s\S]*?)\s*</span>\s*' \
             r'<span\s*class="video-number"\s*>\s*([\s\S]*?)\s*</span>[\s\S]*?' \
             r'<i\s*class="video-station-num"\s*>\s*([\s\S]*?)\s*</i>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):

        # 解析出爬取到的 html 中的有效内容块
        root_html_list = re.findall(Spider.root_p, htmls, re.I)

        # 主播列表
        anchors = []

        for root_html in root_html_list:
            parse_obj = re.search(Spider.data_p, root_html, re.I)
            if (not parse_obj):
                continue
            title, anchor_name, watch_num, star_num = parse_obj.group(
                1, 2, 3, 4)
            anchor = {
                'title': title,
                'anchor_name': anchor_name,
                'watch_num': watch_num,
                'star_num': star_num
            }
            anchors.append(anchor)

        return anchors

    def __sort(self, anchors):
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['watch_num'])
        watch_num = float(r[0])
        if '万' in anchor['watch_num']:
            watch_num *= 10000
        return watch_num

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        return self.__sort(anchors)


if __name__ == '__main__':
    spider = Spider()
    anchor_list = Converter.camelify(spider.go())
    print(anchor_list)
