# Assignment_2
## Title
Assignment2
## Installation
## PyPI
```bash
pip install request
```
## Usage
url_api = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={tc}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
## Examples
```bash
Enter the num: 2
[{'id': 1, 'name': 'Bitcoin'}, {'id': 1027, 'name': 'Ethereum'}]
[{'News': "Vitalik Buterin: El Salvador's Bitcoin Approach Is 'Contrary to the Ideals' of Crypto", 'Script': 'The Ethereum creator railed that Nayib Bukele "loves being praised" and said "shame on Bitcoin maximalists who are uncritically praising him."'}, {'News': 'US Senator Reveals That She Had Stacked Up $100K Worth Of BTC In August', 'Script': 'Senator Cynthia Lummis revealed through a filing that she had purchased bitcoin in August. The value of her BTC purchase is worth between $50K to $100K. Senator Lummis is one of the pro-crypto members of the senate, notably saying that she would like bitcoin to form “part of a di...'}, {'News': 'Voting period for Mt. Gox civil rehabilitation plan finally ends', 'Script': 'Tokyo-based crypto exchange Mt. Gox shut down in 2014 after it lost Bitcoin (BTC) worth $450 million at the time...  Continue reading  \n'}, {'News': 'Former Goldman Sachs Exec Explains Why His Crypto Portfolio Is 70% $ETH, 5% $BTC', 'Script': 'In a recent interview, former Goldman Sachs executive&#160;Raoul Pal&#160;talked about&#160;the impending global economic slowdown and what he is doing to prepare for it, in particular explaining the rationale behind the interesting allocation strategy he has used for his crypto ...'}, {'News': 'Powerbridge Technologies Set To Launch Bitcoin And Ethereum Mining In Hong Kong', 'Script': 'Powercrypto Holdings, a subsidiary of the blockchain software provider Powerbridge Technologies, is launching cryptocurrency mining, specifically Bitcoin (BTC)and Ethereum (ETH), in Hong Kong. These cryptocurrency operations will utilize environmental-friendly, green, and sustain...'}]
```
## License
  [MIT](https://choosealicense.com/licenses/mit/)
