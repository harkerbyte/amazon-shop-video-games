import attrs
from numpy import product
from selenium import webdriver 
import beautifulsoup4
import pandas as pd

driver = webdriver.chrome("usr/lib/chromium-brower/chromedriver")

products=[]
prices= []
ratings=[]
by = []
driver.get("https://www.amazon.com/b?node=16225016011&pf_rd_r=RXRPTNRAQK404Q1CNC2F&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0&pd_rd_r=dd196104-0d5f-4994-8a01-553b24b413e0&pd_rd_w=eJWFx&pd_rd_wg=BrpEz&ref_=pd_gw_unk")

content = driver.page_source
soup = beautifulsoup4(content)
for a in soup.findAll("'a', href=True, attrs={'class':'_octopus-search-result-card_style_apbSearchResultItem__2-mx4':'a-size-base-plus a-color-base a-text-normal'}"):
  Name =a.find('div', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
price = a.find('div', attrs={'class':'a-price-whole'})
rate = a.find('div', attrs={'class':'a-icon a-icon-star-small a-star-small-5 aok-align-bottom'})
maker = a.find('div', attrs={'class':'by PlayStation'})
products.append(Name.text)
prices.append(price.text)
ratings.append(rate.text)
by.append(maker.text)

df = pd.DataFrame({'product name':products,'Price':prices,'rate':ratings,'maker':by})
df.to_txt('products.txt', index=False, encoding='utf-8')

