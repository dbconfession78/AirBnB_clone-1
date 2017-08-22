#!/usr/bin/python3
from fabric.api import *
import time
from os import path
env.hosts = ['54.159.152.54', '54.82.219.75']


def do_deploy(archive_path):
    """
    distributes an archive to webservers
    """
    if (path.isfile(archive_path) != 1):
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


def do_pack():
    """
    packages the web_static folders contents into a tar (.tgz)
    """
    try:
        now = time.strftime("%Y%m%d%H%M%S")
        local('mkdir -p ./versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(now))
        return("versions/web_static_{}.tgz".format(now))
    except:
        return None


def deploy():
    """
    packages web static files into a tar (.tgz) file
    uploads .tgz file to servers, uncompresses them and cleans up
    """
    try:
        archive_path = do_pack()
        did_deploy = do_deploy(archive_path)
        return did_deploy
    except:
        return False
