import requests as requests

class packet:
    def __init__(self, tc1):
        self.tc1 = tc1

    def info(self, cryp):
        for i in range(len(cryp)):
            if cryp[i] == ' ' or cryp[i] == '.':
                cryp = cryp.replace(' ', '-')

        output_list = []
        tc = self.tc1
        while True:
            url_api = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={tc}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
            responce = requests.get(url=url_api)
            data = responce.json()
            for i in range(0, tc):
                output_list.append({
                    'id': data['data']['cryptoCurrencyList'][i]['id'],
                    'name': data['data']['cryptoCurrencyList'][i]['name']
                })
            print(output_list)
            for i in range(0, tc):
                if 'name' == 'Bitcoin' in output_list:
                    print(output_list.get('id'))
            coin_id = 0
            for i in range(len(output_list)):
                if output_list[i]['name'] == cryp.lower().title():
                    coin_id = output_list[i]['id']
            urls = f'https://api.coinmarketcap.com/content/v3/news?coins={coin_id}'
            res = requests.get(url=urls)
            data_news = res.json()
            data_news_json = []
            for i in range(0, len(data_news['data'])):
                data_news_json.append({
                    'News': data_news['data'][i]['meta']['title'],
                    'Script': data_news['data'][i]['meta']['subtitle']
                })
            return data_news_json


limit = int(input("Enter the num:"))
andd = packet(limit)
print(andd.info("bitcoin"))
