import requests
import os

# 文件 URL
url = "https://github.com/MetaCubeX/meta-rules-dat/raw/refs/heads/meta/geo/geoip/cn.list"

# 下载文件内容
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功
data = response.text

# 分离 IPv4 和 IPv6 地址
ipv4_list = []
ipv6_list = []

ipv6_started = False

for line in data.splitlines():
    line = line.strip()
    if not line:
        continue
    
    if ":" in line:
        ipv6_started = True
    
    if ipv6_started:
        ipv6_list.append(line)
    else:
        ipv4_list.append(line)

# 保存到文件
os.makedirs("release", exist_ok=True)
with open("release/IPV4.txt", "w") as ipv4_file:
    ipv4_file.write("\n".join(ipv4_list))

with open("release/IPV6.txt", "w") as ipv6_file:
    ipv6_file.write("\n".join(ipv6_list))
