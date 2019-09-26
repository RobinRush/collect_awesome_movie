# coding=utf-8
import urllib.request
from urllib.error import HTTPError

import dao_manager


def test():
    target_url = "https://www.dy2018.com/i/91866.html"
    try:
        response = urllib.request.urlopen(target_url)
        http_code = response.code
        result = response.read().decode('gbk')
        print(result)
    except HTTPError as e:
        print(e)
        http_code = e.code
    dao_manager.insert_dy2018(target_url, http_code)
    pass


if __name__ == '__main__':
    test()
    pass
