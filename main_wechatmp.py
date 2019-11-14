# coding=utf-8
import itchat
import itchatmp
import admin_config
import msg_handler

itchatmp.update_config(itchatmp.WechatConfig(
    token=admin_config.token,
    appId=admin_config.appId,
    appSecret=admin_config.appSecret
))


@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def text_reply(msg):
    msg_type = msg['MsgType']
    if msg_type == 'text':
        print(msg)
        toUserName = msg['FromUserName']
        content = msg['Content']
        ret_msg = msg_handler.do_action(content)
        return ret_msg
    elif msg_type == 'event':
        print(msg)
        content = msg['Event']
        if content == 'subscribe':
            return '欢迎关注本公众号，可以输入【指令】查看可以操作的内容。'
    return ''


if __name__ == '__main__':
    itchatmp.run()
    pass
