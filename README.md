# collect_awesome_movie
# TODO:

scp * root@xxxx:~/collect_awesome_movie/

nohup python3 -u main_wechatmp.py > log_wechatmp.log 2>&1 &
jobs -p
kill %1
