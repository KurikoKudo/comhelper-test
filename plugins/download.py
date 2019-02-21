# cording: utf-8

import subprocess
import requests
import logging

from slackbot_settings import API_TOKEN, WORKING_DIRECTORY


def download(channel, doc_name):
    git_cmd = "git pull origin master"
    git_cmd_return = subprocess.call(git_cmd.split(), cwd=WORKING_DIRECTORY)

    # TODO: 実行環境のルーティングに変更する
    doc_path = WORKING_DIRECTORY + '/docs/' + doc_name + '.md'

    if git_cmd_return != 0:
        logging.info('git pull origin master の実行でエラーが発生しました。')
        return False
    else:

        files = {'file': open(doc_path, 'rb')}
        param = {
            'token': API_TOKEN,
            'channels': channel._body['id'],
            'filetype': 'markdown'
        }
        requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
