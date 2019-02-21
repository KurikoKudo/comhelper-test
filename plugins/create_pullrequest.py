# cording: utf-8

import subprocess

from slackbot_settings import WORKING_DIRECTORY


def create_pullrequest(pr_title):

    git_cmd = "hub pull-request -m " + pr_title

    try:
        git_cmd_return = subprocess.check_output(git_cmd.split(), cwd=WORKING_DIRECTORY)
    except subprocess.CalledProcessError as e:
        return 'hub pull-request -m の実行でエラーが発生しました。'

    return git_cmd_return
