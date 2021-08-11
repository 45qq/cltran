import configparser
import platform
import sys
from os import path


config_path = ''
if platform.system() == 'Windows':
    config_path = path.join(path.dirname(path.realpath(sys.argv[0])), 'cltran.ini')
elif platform.system() == 'Linux':
    config_path = path.join(path.dirname(path.realpath(sys.executable)), 'cltran.ini')
else:
    config_path = path.join(sys.path[0], 'cltran.ini')

config = configparser.ConfigParser()
config.read(config_path, 'utf-8')

# api
secretId = config.get('api', 'secretId')
secretKey = config.get('api', 'secretKey')

# cmd
timeout = config.getint('cmd', 'timeout')
show_original_text = config.getboolean('cmd', 'show_original_text')


# regular
def get_relist():
    i = 1
    relist = []
    while True:
        re = 're_%d' % i
        group = 'group_%d' % i
        if config.has_option('regular', re):
            relist.append((config.get('regular', re)[1:-1],
                           config.getint('regular', group) if config.has_option('regular', group) else 0))
        else:
            break
        i += 1
    return relist