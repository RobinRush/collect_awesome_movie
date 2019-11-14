# coding=utf-8
import urllib.request
from urllib.error import HTTPError

import time

import dao_manager
import html_parse


def test(target_url):
    try:
        response = urllib.request.urlopen(target_url, timeout=10)
        http_code = response.code
        result = response.read().decode('gbk')
        title, rank = html_parse.parse(result)
        print(target_url)
    except HTTPError as e:
        print(e)
        http_code = e.code
        title = ''
        rank = ''
        result = ''
    print(title, rank)
    dao_manager.insert_dy2018(target_url, http_code, title, rank, result)
    pass


if __name__ == '__main__':
    start_index = 101425
    url_str = "https://www.dy2018.com/i/%s.html"
    while True:
        test(url_str % start_index)
        start_index += 1
        time.sleep(1)
    pass
