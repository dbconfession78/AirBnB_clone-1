#!/usr/bin/python3
"""
Module: 1-pack_web_static
"""
from fabric.api import *
import time


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
