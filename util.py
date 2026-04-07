import os
from typing import Dict,Any

import httpx
from loguru import logger

class Util(object):
    @staticmethod
    def download(filename: str, url: str) -> bool:
        try:
            path = os.path.dirname(filename)
            os.makedirs(path, exist_ok=True)
            
            if os.path.exists(filename):
                return True
                #os.remove(filename)
            
            with httpx.Client() as client:
                logger.info(f'download %s[%s]' % (os.path.basename(filename), url))
                response = client.get(url)
                response.raise_for_status()
                contentType = response.headers.get("Content-Type")
                if contentType.find("text/plain") < 0:
                    raise Exception("Content-Type[%s] error"%(contentType))
                with open(filename,'wb') as f:
                    f.write(response.content)
            
            return True
        except Exception as e:
            logger.error(f'%s download failed: %s' % (filename, e))
            return False