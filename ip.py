import os
import ipaddress
from typing import Dict,List

from loguru import logger

from util import Util


class RuleIP(object):
    def __init__(self, ip:Dict[str, str]) -> None:
        self.__ip = ip
    
    def __merge(self, filelist: List[str], output_file:str):
        try:
            path = os.path.dirname(output_file)
            os.makedirs(path, exist_ok=True)

            tmplist = []
            for filename in filelist:
                with open(filename) as f:
                    tmp = [ipaddress.ip_network(line.strip()) for line in f if line.strip()]
                    tmplist.extend(tmp)

            if len(tmplist) > 0:
                merged = ipaddress.collapse_addresses(tmplist)
                with open(output_file, 'w') as out:
                    for net in merged:
                        out.write(str(net) + "\n")
        except Exception as e:
            logger.error(e)

    def update(self, path_download:str, output_file:str):
        try:
            filelist = []
            for k,v in self.__ip.items():
                filename = os.path.join(path_download, k)
                result = Util.download(filename, v)
                if result:
                    filelist.append(filename)
                else:
                    return False
            
            if len(filelist) > 0:
                self.__merge(filelist, output_file)

            return True
        except Exception as e:
            logger.error(e)
            return False