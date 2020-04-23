

import pygeoip
import requests



my_ip = requests.get('https://api.ipify.org').text

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(my_ip)





for key, val in res.items():
    print(f'{key} : {val}')

