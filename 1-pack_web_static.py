#!/usr/bin/python3

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Method that return the archive path if the archive has been correctly generated.
    """

    dt = datetime.now()

    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second

    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(year, month,
                                                             day, hour,
                                                             minute, second)
    
    local ("mkdir -p versions")
    archive = local("tar -cvzf {} web_static".format(filename))

    if archive.succeded:
        return filename
    