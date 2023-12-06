
from .path_names import construct_surl_LCLS

SUPPORTED_VERSION="1.33"


def get_algorithms():
    return {
        'surl': { 'LCLS': construct_surl_LCLS, }
    }


# https://github.com/jamesp-epcc/DUNERucioPolicy/blob/master/path_gen.py

