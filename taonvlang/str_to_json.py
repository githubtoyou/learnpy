#-*- coding = utf-8 -*-
#@Time:2021/5/2712:03
#@Author:Charlie
#@File:str_to_json.py
#@Software:PyCharm

s = '''
offset: 0
size: 20
'''

# head1 = '''
# Accept: application/json, text/plain, */*
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
# Connection: keep-alive
# Content-Length: 22
# Content-Type: application/json
# Cookie: _itt=1; _ga=GA1.2.343646757.1613809657; LF_ID=1613809656986-9255435-9968138; GCID=703e66c-f85529d-aab004e-9c42126; GRID=703e66c-f85529d-aab004e-9c42126; _wc_t=1621500290448; GCESS=BQUEAAAAAAoEAAAAAAQEAC8NAAEI1YEbAAAAAAACBDyZq2ALAgUABgRPShMfBwQr2jF.AwQ8matgCAEDCQEBDAEB; _gid=GA1.2.761420527.1621927567; gksskpitn=bbc60b27-8b34-4862-8c1f-424bd0c5be29; tgeo=1622010458000; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1620968966,1621499738,1621566553,1622025157; _r_c=5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221802709%22%2C%22first_id%22%3A%221799deb66530-0ed8c8d9356066-2363163-2073600-1799deb6654b0b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.infoq.cn%2Fnews%22%2C%22%24latest_utm_source%22%3A%22related_read_bottom%22%2C%22%24latest_utm_medium%22%3A%22article%22%7D%2C%22%24device_id%22%3A%22177be8d23d93e4-064e12614e6acf-73e356b-2073600-177be8d23da7a5%22%7D; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1622084159; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1622084163|1622084162
# Host: www.infoq.cn
# Origin: https://www.infoq.cn
# Referer: https://www.infoq.cn/news
# sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
# sec-ch-ua-mobile: ?0
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
# '''
def strToJson(s):
    dict = {}
    tmp_list = s.split("\n")
    for i in tmp_list:
        if i:
            start_index = i.find(':')
            key = i[0:start_index]
            value = i[start_index + 1: ].strip()
            #print(key, value)
            dict[key] = value
    print(dict)
#print(result)
if __name__ == '__main__':
    strToJson(s)

# strToJson(head)