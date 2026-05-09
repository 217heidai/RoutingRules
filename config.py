import os

path_pwd             = os.getcwd()
path_download        = os.path.join(path_pwd, "download")
path_ipv4_china      = os.path.join(path_pwd, "rules/ipv4_china.txt")
path_ipv6_china      = os.path.join(path_pwd, "rules/ipv6_china.txt")
path_ipv4_cloudflare = os.path.join(path_pwd, "rules/ipv4_cloudflare.txt")
path_ipv6_cloudflare = os.path.join(path_pwd, "rules/ipv6_cloudflare.txt")
path_proxy           = os.path.join(path_pwd, "rules/proxy.txt")
path_direct          = os.path.join(path_pwd, "rules/direct.txt")
path_private         = os.path.join(path_pwd, "rules/private.txt")

# 下载链接
url_ipv4 = {
    "ipv4_clang_all_cn.txt"        : "https://ispip.clang.cn/all_cn.txt",
    "ipv4_gaoyifan_china.txt"      : "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/refs/heads/ip-lists/china.txt",
    "ipv4_Hackl0us_CN-ip-cidr.txt" : "https://raw.githubusercontent.com/Hackl0us/GeoIP2-CN/release/CN-ip-cidr.txt"
}
url_ipv4_cloudflare = {
    "ipv4_cloudflare.txt"   : "https://www.cloudflare-cn.com/ips-v4/#"
}
url_ipv6 = {
    "ipv6_clang_all_cn_ipv6.txt" : "https://ispip.clang.cn/all_cn_ipv6.txt",
    "ipv6_gaoyifan_china6.txt"   : "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/refs/heads/ip-lists/china6.txt"
}
url_ipv6_cloudflare = {
    "ipv6_cloudflare.txt"   : "https://www.cloudflare-cn.com/ips-v6/#"
}
url_proxy = {
    "proxy_Loyalsoldier_proxy-list.txt" : "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt",
    "proxy_Loyalsoldier_gfw.txt"        : "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/gfw.txt",
    "proxy_Loyalsoldier_greatfire.txt"  : "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/greatfire.txt"
}
url_direct = {
    "direct_Loyalsoldier_direct-list.txt"               : "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/direct-list.txt",
    "direct_Loyalsoldier_apple-cn.txt"                  : "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/apple-cn.txt",
    "direct_blackmatrix7_SteamCN.list"                  : "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/SteamCN/SteamCN.list",
    "direct_blackmatrix7_GameDownloadCN.list"           : "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Game/GameDownloadCN/GameDownloadCN.list",
    "direct_felixonmars_accelerated-domains.china.conf" : "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/refs/heads/master/accelerated-domains.china.conf"
}
url_private = {
    "direct_Loyalsoldier_private.txt" : "https://raw.githubusercontent.com/Loyalsoldier/domain-list-custom/release/private.txt"
}

# 白名单
white_direct = {
    "dl.google.com", 
    "tools.google.com", 
    "clientservices.googleapis.com",
    "fonts.googleapis.com",
    "update.googleapis.com",
    "www.gstatic.com",
    "ssl.gstatic.com"
}
white_private = {
    "msftncsi.com",
    "msftconnecttest.com",
    "captive.apple.com",
    "ping.archlinux.org"
}