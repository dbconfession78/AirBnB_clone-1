#!/usr/bin/python3
"""
Module: 2-do_deploy_web_static
"""
from fabric.api import *
from os import path
env.hosts = ['54.159.152.54', '54.82.219.75']


def do_deploy(archive_path):
    """
    distributes an archive to webservers
    """
    if path.isfile(archive_path) != 1:
        return False
    try:
        file = archive_path.split('/')[-1]
        new_folder = '/data/web_static/releases/{}'.format(file.split('.')[0])
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(new_folder))
        run('tar -xzf /tmp/{} -C {}'.format(file, new_folder))
        run('mv {}/web_static/* {}'.format(new_folder, new_folder))
        run('rm -rf {}/web_static'.format(new_folder))
        run('rm /tmp/{}'.format(file))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(new_folder))
        return True
    except:
        return False
