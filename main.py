import os
import atexit

from source import tools
tools.确认DM插件后台服务端运行(1)

from source import DMClient
from source import dm_tools
from source import game


if __name__ == '__main__':
    dm = DMClient.dm_client("127.0.0.1","9000",1)
    dm.UnBindWindow()
    


















