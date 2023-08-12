from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.worldweatheronline.com/pinabacdao-weather/samar/ph.aspx?day=20&tp=1')

town = "Maasin, Southern Leyte"

search_bar = driver.find_element(By.NAME, "search")
search_bar.clear()
search_bar.send_keys(town)
search_bar.send_keys(Keys.RETURN)

town_link = driver.find_element(By.LINK_TEXT, town)
town_link.click()

print(driver.title)
print(driver.current_url)

hourly_btn = driver.find_element(By.LINK_TEXT, "Hourly")
hourly_btn.click()

time_of_day = '06:00'

day_temp = driver.find_element(By.XPATH, "//table//tbody//tr[position()>8]//td[@class='days-details-row-item']//p[@class='days-table-forecast-p']")
day_rain = driver.find_element(By.XPATH, "//table//tbody//tr[position()>8]//td[@class='days-details-row-item']//div[@class='days-rain-blue']")
day_hum  = driver.find_element(By.XPATH, "//table//tbody//tr[position()>8]//td[6]")
day_wind  = driver.find_element(By.XPATH, "//table//tbody//tr[position()>8]//td[8]")

# /table/tbody/tr/td[count(preceding-sibling::td)+1 = count(ancestor::table/thead/tr/th[.='Price']/preceding-sibling::th)+1]



print("Temp (°C): ", day_temp.text[:2])
print("Rainfall (mm): ", day_rain.text[:4].strip())
print("Humidity (%): ", day_hum.text[:2])
print("Wind speed (km/h): ", day_wind.text[0])


assert "No results found." not in driver.page_source
driver.close()