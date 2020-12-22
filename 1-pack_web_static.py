#!/usr/bin/python3
"""do pack function"""
from datetime import datetime
from fabric.api import *

def do_pack():
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    result = local('tar -czvf versions/web_static_{}.
                   tgz web_static'.format(now))
    if result.failed:
        return None
    else:
        return result
