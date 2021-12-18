from lxml import etree
import requests
import time
url = 'https://finance.yahoo.com/quote/TSLA/history?p=TSLA'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

resp = requests.get(url,headers = headers)
#print(resp)

with open('TESLA3.text', 'wb+') as f:
    f.write(resp.content)

#html = etree.HTML(resp.text)
#hrefs = html.xpath('/html/body/section/div[3]/div/article[*]/a/@href')
#print(hrefs)
#table = html.xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/text()')
#print(table)

