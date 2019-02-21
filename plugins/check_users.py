# coding: utf-8

import requests
from slackbot_settings import USER_TOKEN


def check_all_users_by_slack():
    """
    slackAPIからユーザ情報を取得し、ユーザリストを更新する関数
    :return: users list
    """
    param = {
        'token': USER_TOKEN,
        'pretty': 1
    }
    resp = requests.get(url="https://slack.com/api/users.list", params=param)
    data = resp.json()
    members = data['members']

    update_txt = ''
    return_txt = ''
    for member in members:
        user_id = member['id']
        user_name = member['profile']['display_name']
        if user_name == '':
            user_name = member['profile']['real_name']
        line = user_id + " " + user_name + "\n"
        update_txt += line
        return_txt += user_name + ' '

    file = open('users.txt', mode='w')
    file.write(update_txt)
    file.close()

    return return_txt


def get_user_dict():

    file = open('users.txt', mode='r')
    lines = file.readlines()
    file.close()

    user_dict = {}

    # txt には
    # user_id user_name\n
    # で情報が入っている
    for line in lines:
        user_data = line.rstrip('\n').split()
        user_id = user_data[0]
        user_name = user_data[1]
        user_dict.setdefault(user_id, user_name)

    return user_dict

