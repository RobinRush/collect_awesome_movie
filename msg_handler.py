# coding=utf-8
import movie_utils

cmd_cmds = ['指令']
cmd_get_rand_top = ['好片推荐', '手气不错']


def do_action(msg):
    if msg in cmd_get_rand_top:
        result = movie_utils.get_rand_top()
    elif msg in cmd_cmds:
        result = '指令:好片推荐,手气不错'
    else:
        result = movie_utils.search(msg)
    return result
    pass
