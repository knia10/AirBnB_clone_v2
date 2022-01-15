#!/usr/bin/env bash
'''
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
'''


from datetime import datetime
from fabric.api import local, env, put, run
from os.path import getsize

env.hosts = ['35.237.215.97', '35.231.150.24']
env.user = "ubuntu"


def do_pack():
    """
    Method that return the archive path
    if the archive has beencorrectly generated.
    """

    local("mkdir -p versions")
    time = datetime.now()

    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = time.second

    time_file = local("tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz\
                       web_static".format(time.year, time.month, time.day,
                      time.hour, time.minute, time.second))

    if time_file.success and getsize(time_file) > 0:
       return time_file
     return None


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


def deploy():
    '''
    function that creates and distributes an archive to your web servers
    '''
    archive_path = do_pack()
    if archive_path:
        new_file = do_deploy(archive_path)
        return new_file
    return False
