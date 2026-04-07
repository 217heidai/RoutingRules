import os

import config
from ip import RuleIP
from domain import RuleDomain

def main():
    ruleIPv4 = RuleIP(config.url_ipv4)
    ruleIPv4.update(config.path_download, config.path_ipv4_china)

    ruleIPv4_cloudflare = RuleIP(config.url_ipv4_cloudflare)
    ruleIPv4_cloudflare.update(config.path_download, config.path_ipv4_cloudflare)

    ruleIPv6 = RuleIP(config.url_ipv6)
    ruleIPv6.update(config.path_download, config.path_ipv6_china)

    ruleIPv6_cloudflare = RuleIP(config.url_ipv6_cloudflare)
    ruleIPv6_cloudflare.update(config.path_download, config.path_ipv6_cloudflare)

    ruledomain_proxy = RuleDomain(config.url_proxy)
    ruledomain_proxy.update(config.path_download, config.path_proxy)
    
    ruledomain_direct = RuleDomain(config.url_direct)
    ruledomain_direct.update(config.path_download, config.path_direct, config.white_direct)

    ruledomain_private = RuleDomain(config.url_private)
    ruledomain_private.update(config.path_download, config.path_private, config.white_private)
    


if __name__ == "__main__":
    main()
