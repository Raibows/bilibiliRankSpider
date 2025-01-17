from . import main
from FlaskServer.app import db
from flask import request


@main.route('/', methods=['GET', 'POST'])
def index():
    info = '''
    Author:                ChiZuo
    Github:                https://github.com/Raibows/bilibiliRankSVM
    If you like this project, please star it!
    If you have any advice, please contact with me, luckychizuo@gmail.com.
    And I need your help for perfecting this project!
    '''
    return info


@main.route('/config', methods=['GET', 'POST'])
def config():
    from Config import get_all_config_json
    config_json = get_all_config_json()

    return config_json


@main.route('/proxy/get_one/string', methods=['GET'])
def get_one_string():
    temp = db.get_one_string()
    if temp:
        return temp
    else:
        return 'None'


@main.route('/proxy/get_one/dict', methods=['GET'])
def get_one_dict():
    temp = db.get_one_dict()
    if temp:
        return temp
    else:
        return 'None'


@main.route('/proxy/feedback', methods=['POST'])
def feedback():
    '''
    only post allowed
    flag:string, increase or decrease
    :return:
    '''
    flag = request.form.get('flag')
    if flag.lower() == 'increase':
        flag = True
        info = 'increase success'
    elif flag.lower() == 'decrease':
        flag = False
        info = 'decrease success'
    else:
        return 'failed'
    proxy = request.form.get('proxy')
    db.proxy_feedback(
        proxy_string_dict=proxy,
        flag=flag,
    )
    return info
