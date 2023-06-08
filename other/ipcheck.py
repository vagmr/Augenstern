import requests

# 获取公共 IP 地址
url = 'https://api.ipify.org/?format=json'
response = requests.get(url)
data = response.json()
ip_address = data['ip']

# 查询 IP 地址信息，并突出显示国家信息
try:
    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)
    data = response.json()
    country = data['country_name']
    print(f'IP地址：{ip_address}，所在国家：【{country}】\n其它信息：{data}')
except:
    print(f'IP地址：{ip_address}，查询失败')
