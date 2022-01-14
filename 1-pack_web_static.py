#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
'''
from datetime import datetime
from fabric.api import local


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

    if time_file.failed:
        return None
    return time_file
