# coding: utf-8

import subprocess
import time
import shlex

from slackbot.slackclient import SlackClient
from slackbot_settings import API_TOKEN
from .check_users import get_user_dict


def discussion(discussion_title):

    # fileが空であるかの確認
    file = open('commit.txt', mode='r', encoding='utf-8')
    file.seek(0)
    first_char = file.read(1)
    if first_char:
        return False

    cmd = []
    cmd.append('echo "' + discussion_title + '" > commit.txt')

    # commit.txtを作成
    try:
        cmd_return = subprocess.run(cmd, shell=True)
    except subprocess.SubprocessError as e:
        print("[Error] first echo command")
        return False

    return True


def loop():
    """
    議論終了コマンドが送信されるまでメッセージの書き出しを行う関数
    """

    client = SlackClient(API_TOKEN)
    # ユーザーidからユーザー名を取得するため
    user_dict = get_user_dict()

    keys = [k for k, v in user_dict.items() if v == 'comhelper']
    comhelper_user_id = keys[0]

    return_flag = True

    # 議論終了コマンドが送信されるまでループを続ける
    while return_flag:
        events = SlackClient.rtm_read(client)

        for event in events:
            event_type = event.get('type')

            if event_type == 'message':
                message_text = event.get('text')

                if message_text == '<@' + comhelper_user_id + "> 議論を終了して":
                    # 議論終了コマンドが送信されたらループを抜ける
                    return_flag = False
                else:
                    # ユーザー名を確認しつつ，メッセージをテキストファイルに一時保存
                    send_user_id = event.get('user')
                    send_user_name = user_dict[send_user_id]
                    add_commit_message = []
                    add_commit_message.append('echo "' + send_user_name + ': ' + message_text + '" >> commit.txt')
                    try:
                        cmd_return = subprocess.run(add_commit_message, shell=True)
                    except subprocess.SubprocessError:
                        return 'echo >> commit.txt の実行でエラーが発生しました。'

        time.sleep(1)

    return '議論を終了しました！\n次の議論開始前にコミットしてください。'







