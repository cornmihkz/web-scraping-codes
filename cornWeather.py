import requests
from bs4 import BeautifulSoup as bs
r = requests.get('https://www.worldweatheronline.com/pinabacdao-weather/samar/ph.aspx?day=20&tp=1')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = bs(r.content, 'html.parser')

s = soup.find('div', class_ = 'box days-box')
content = s.find_all('p')


print(s.find_all('p', class_='days-comment'))


#//p[@class='days-table-forecast-p']")
# day_temp = driver.find_element(By.CLASS_NAME, 'days-table-forecast-p') //..//td[@class='days-details-row-item']//p[@class='days-comment' == time_of_day] //div[@class='days-rain-blue']//div[@class='days-rain-number]
# for detail in day_details:
# 	print(detail.text)
