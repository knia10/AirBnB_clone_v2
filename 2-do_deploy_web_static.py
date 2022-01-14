#!/usr/bin/python3
'''
Fabric script that distributes an archive to your web servers,
using the function do_deploy
'''
from fabric.api import local, env, put, run
from os.path import isfile

env.hosts = ['35.237.215.97', '35.231.150.24']
env.user = "ubuntu"


def do_deploy(archive_path):
    '''
    function that distributes an archive to your web servers
    '''
    try:
        no_slash = archive_path.split("/")[-1]
        no_extend = no_slash.split(".")[0]
        data_releases = '/data/web_static/releases/'
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(data_releases, no_extend))
        run("tar -xzf /tmp/{} -C {}{}/".format(no_slash, data_releases,
                                               no_extend))
        run("rm /tmp/{}".format(no_slash))
        run("mv {}{}/web_static/* {}{}/".format(data_releases, no_extend,
                                                data_releases, no_extend))
        run("rm -rf {}{}/web_static".format(data_releases, no_extend))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(data_releases,
                                                          no_extend))
        return True
    except:
        return False
