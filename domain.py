import os
import tldextract
from typing import Dict,List,Tuple,Set

from loguru import logger

from util import Util


class RuleDomain(object):
    def __init__(self, domain:Dict[str, str]) -> None:
        self.__domain = domain
    
    def __merge(self, filelist: List[str], output_file:str, white:Set[str]=None):
        def domains_add(extractor, domains:Dict[str,List[str]], domain:str) -> Dict[str,List[str]]:
            try:
                extracted = extractor(domain)
                registered_domain = extracted.registered_domain
                if len(registered_domain) == 0:
                    if len(extracted.suffix):
                        registered_domain = extracted.suffix
                    else:
                        print("无效规则：%s"%(domain))
                        return domains
                subdomain = extracted.subdomain
                if registered_domain not in domains:
                    domains[registered_domain] = [subdomain]
                else:
                    domains[registered_domain].append(subdomain)
                return domains
            except Exception as e:
                logger.error(e)
                return domains
        try:
            path = os.path.dirname(output_file)
            os.makedirs(path, exist_ok=True)

            extractor = tldextract.TLDExtract()

            domains_regexp:List[str] = list()
            domains_keyword:List[str] = list()
            domains_full:Dict[str,List[str]] = dict()
            domains_domain:Dict[str,List[str]] = dict()
            for filename in filelist:
                with open(filename) as f:
                    for line in f:
                        tmp = line.strip()
                        if tmp.startswith("#"):
                            continue
                        if len(tmp):
                            if tmp.startswith("full:"):
                                domains_full = domains_add(extractor, domains_full, tmp[len("full:"):])
                            elif tmp.startswith("domain"):
                                domains_domain = domains_add(extractor, domains_domain, tmp[len("domain:"):])
                            elif tmp.startswith("regexp:"):
                                domains_regexp.append(tmp)
                            elif tmp.startswith("keyword:"):
                                domains_keyword.append(tmp)
                            elif tmp.startswith("DOMAIN,"):
                                domains_full = domains_add(extractor, domains_full, tmp[len("DOMAIN,"):])
                            elif tmp.startswith("DOMAIN-SUFFIX,"):
                                domains_domain = domains_add(extractor, domains_domain, tmp[len("DOMAIN-SUFFIX,"):])
                            elif tmp.startswith("server=/"):
                                domains_domain = domains_add(extractor, domains_domain, tmp[len("server=/"):tmp.rfind("/")])
                            else:
                                if tmp.find(".") > 0:
                                    domains_domain = domains_add(extractor, domains_domain, tmp)
                                else:
                                    print("无效规则：%s"%(tmp))
            
            # regexp 规则去重、排序
            if len(domains_regexp) > 1:
                domains_regexp = list(set(domains_regexp))
                domains_regexp.sort()

            # keyword 规则去重、排序
            if len(domains_keyword) > 1:
                domains_keyword = list(set(domains_keyword))
                domains_keyword.sort()

            # full 规则子域名去重、排序
            key_remove = []
            for k,v in domains_full.items():
                if '' in v:
                    domains_domain[k] = [''] # full 规则中存在 domain 规则，重新归档到 domains_domain
                    key_remove.append(k)
                else:
                    tmp = list(set(v))
                    tmp.sort()
                    domains_full[k] = tmp
            # 移除已归档到 domains_domain 的域名
            for k in key_remove:
                domains_full.pop(k, None)
            domains_full = {k: domains_full[k] for k in sorted(domains_full)}

            # domain 规则子域名去重、排序
            for k,v in domains_domain.items():
                if '' in v:
                    domains_domain[k] = ['']
                else:
                    tmp = list(set(v))
                    tmp.sort()
                    domains_domain[k] = tmp
            domains_domain = {k: domains_domain[k] for k in sorted(domains_domain)}
            
            # 已在 doamin 规则拦截的，移除 full 规则
            domains_full = {k: v for k, v in domains_full.items() if not (k in domains_domain and '' in domains_domain[k])}

            if len(domains_full) or len(domains_domain) or len(domains_regexp) or len(domains_keyword):
                with open(output_file, 'w') as out:
                    # full
                    if len(domains_full):
                        for k,v in domains_full.items():
                            for item in v:
                                line = item + '.' + k if item != '' else k
                                if white and line in white:
                                    continue
                                out.write("full:" + line + "\n")
                    # domain
                    if len(domains_domain):
                        for k,v in domains_domain.items():
                            for item in v:
                                line = item + '.' + k if item != '' else k
                                if white and line in white:
                                    continue
                                out.write("domain:" + line + "\n")
                    # regexp
                    if len(domains_regexp):
                        for item in domains_regexp:
                            out.write(item + "\n")
                    # keyword
                    if len(domains_keyword):
                        for item in domains_keyword:
                            out.write(item + "\n")
        except Exception as e:
            logger.error(e)

    def update(self, path_download:str, output_file:str, white:Set[str]=None):
        try:
            filelist = []
            for k,v in self.__domain.items():
                filename = os.path.join(path_download, k)
                result = Util.download(filename, v)
                if result:
                    filelist.append(filename)
                else:
                    return False
            
            if len(filelist) > 0:
                self.__merge(filelist, output_file, white)

            return True
        except Exception as e:
            logger.error(e)
            return False