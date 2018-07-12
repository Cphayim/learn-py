import re
import json
from urllib import request
from time_decorator import time_decorator
from camelify import camelify

class Spider():
    url = 'https://www.panda.tv/cate/lol'

    root_p = '<div\s*class="video-info">\s*([\s\S]*?)\s*</div>'

    data_p = '<span\s*class="video-title"[\s\S]*?>\s*([\s\S]*?)\s*</span>\s*' \
             '<span\s*class="video-nickname"[\s\S]*?</i>\s*([\s\S]*?)\s*</span>\s*' \
             '<span\s*class="video-number"\s*>\s*([\s\S]*?)\s*</span>[\s\S]*?' \
             '<i\s*class="video-station-num"\s*>\s*([\s\S]*?)\s*</i>'

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

    def go(self):
        htmls = self.__fetch_content()
        return self.__analysis(htmls)

@time_decorator(True)
def to_camel_case(obj):
    return camelify(obj)

if __name__ == '__main__':
    spider = Spider()
    anchor_list = spider.go()
    print(to_camel_case(anchor_list))
