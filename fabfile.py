#!venv/bin/python3
from fabric.api import *
import tarfile
import os.path
import re
from datetime import datetime

env.hosts = ['54.89.25.106', '52.3.241.66']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_pack():
    """distributes an archive to your web servers
    """
    folder = local("mkdir -p ./deployments")
    local("cp -r diskovafrika ./deployments")
    local("cp run.py ./deployments")
    local("cp requirements.txt ./deployments")
    name = str(datetime.now().strftime("%Y_%m_%dT%H_%M_%S"))
    tar = local('tar -cvzf api_v1_{}.tgz deployments'.format(name))
    if os.path.exists("./api_v1_{}.tgz".format(name)):
        return os.path.normpath("./api_v1_{}.tgz".format(name))
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /home/ubuntu/diskovafrika')
        main = "/home/ubuntu/diskovafrika"
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        # sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/deployments/* {}/'.format(main, main))
        # sudo('rm -rf /home/ubuntu/diskovafrika/deployments')
        # sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False


def deploy():
    """distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    f = do_deploy(path)
    return f
