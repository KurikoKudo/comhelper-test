# coding: utf-8

import subprocess
import shlex

from slackbot_settings import WORKING_DIRECTORY


def commit():

    git_pull_cmd = "git pull origin comhelper"
    try:
        git_pull_cmd_return = subprocess.call(shlex.split(git_pull_cmd), cwd=WORKING_DIRECTORY)
    except subprocess.CalledProcessError:
        return 'pull コマンドでエラーが起きました'

    git_add_cmd = 'git add .'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_add_cmd), cwd=WORKING_DIRECTORY)
    except subprocess.CalledProcessError:
        return 'add コマンドでエラーが起きました'

    git_commit_cmd = 'git commit --allow-empty -F /python_app/comhelper/commit.txt'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_commit_cmd), cwd=WORKING_DIRECTORY)
    except subprocess.CalledProcessError:
        return 'commit コマンドでエラーが起きました'

    git_push_cmd = 'git push origin comhelper'
    try:
        git_cmd_return = subprocess.run(shlex.split(git_push_cmd), cwd=WORKING_DIRECTORY)
    except subprocess.CalledProcessError:
        return 'push コマンドでエラーが起きました'

    cmd = "rm commit.txt"
    try:
        cmd_return = subprocess.run(shlex.split(cmd), cwd="/python_app/comhelper/")
    except subprocess.CalledProcessError:
        return 'ファイル操作コマンドでエラーが起きました'

    cmd = "touch commit.txt"
    try:
        cmd_return = subprocess.run(shlex.split(cmd), cwd="/python_app/comhelper/")
    except subprocess.CalledProcessError:
        return 'ファイル操作コマンドでエラーが起きました'

    return 'comhelper ブランチへの push が完了しました。'

