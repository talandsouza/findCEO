from urllib.request import Request, urlopen

keyword = 'Accenture'

#*********************************************************************

req = Request(
    url='https://www.google.com/search?q=' + str(keyword) + '+ceo&stick=H4sIAAAAAAAAAOPgE-LUz9U3MCwqMErWUsxOttLPL0pPzMusSizJzM9D4Vglp-YvYuVNTE5OzSspLUpVAPIBdq3m60AAAAA&sa=X&ved=2ahUKEwjpnqWIldv6AhWWBd4KHal2As0Q6BMoAHoECDcQAg&biw=371&bih=569&dpr=1.5', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
ceo_html = webpage.decode("UTF-8")
ceo_index = ceo_html.find('<div class="BNeawe deIvCb AP7Wnd">')

ceo_start_index = ceo_index + len('<div class="BNeawe deIvCb AP7Wnd">')

ceo_end_index = ceo_start_index + 50


ceo_title = ceo_html[ceo_start_index:ceo_end_index]

ceo_my_string = ceo_title.find('</div>')

print(ceo_title[0:ceo_my_string])

#*********************************************************************
