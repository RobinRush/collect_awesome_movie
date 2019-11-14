# coding=utf-8
import random

import dao_manager

address = '地址'


def search(search_words):
    search_mode = False
    if search_words.find(address) == 0:
        search_mode = True
        movie_name = search_words[2:]
        columns = ['title', 'rank', 'base_url']
    else:
        movie_name = search_words
        columns = ['title', 'rank']
    data_list = dao_manager.select_by_cause('dy2018', cause_list=["title like '%{}%'".format(movie_name)],
                                            columns=columns, order='order by rank desc'
                                            )
    result = []
    if len(data_list) == 0:
        return '额...没搜到...'
    if search_mode:
        for data in data_list:
            result.append('《%s》分数:%s ,地址:%s' % data)
    else:
        for data in data_list:
            result.append('《%s》分数:%s' % data)
    return '\n'.join(result)


def get_rand_top():
    data_list = dao_manager.select_by_cause('dy2018', cause_list=["http_code=200 and rank >='8' "],
                                            columns=['title', 'rank'], limit=1, offset=random.randint(0, 700)
                                            )
    result = []
    for data in data_list:
        result.append('《%s》分数:%s' % data)
    return '\n'.join(result)


if __name__ == '__main__':
    print(search('天使'))
    print(get_rand_top())
