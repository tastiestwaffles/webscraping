import requests, bs4

def getPrice(productUrl):
  res = requests.get(productUrl)
  res.raise_for_status()
  
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select('SOME CSS HERE')
  return elems0].text.strip()
  
 price = getPrice('http://SOME SITE HERE') #probably class span or something
 print('The price is ' + price)
