from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from datetime import date
from dateutil.rrule import rrule, DAILY
import time
import csv

# initializing the start and end date
start_date = date(2020, 5, 1)
end_date = date(2023, 7, 1)

# all date values from May 1, 2020 to August 1, 2023
all_date_values = []
 
# iterating over the dates
for d in rrule(DAILY, dtstart=start_date, until=end_date):
    all_date_values.append(d.strftime("%d/%m/%Y"))

# Maasin, Southern Leyte Weather Online
driver = webdriver.Chrome()

driver.get('https://www.worldweatheronline.com/maasin-weather-history/southern-leyte/ph.aspx')

town = "Maasin, Southern Leyte"

# get date
# date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# new_date_value = "09/06/2020"
# header = ['date', 'town', 'temp', 'rainfall', 'wind', 'humidity']




with open('Maasin Weather.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["Date", "Town/City", "Temperature (C)", "Rainfall (mm)", "Wind (km/h)", "Humidity (%)"])
	
	for date in range(len(all_date_values)):

		get_date_input = driver.find_element(By.CSS_SELECTOR, "input#ctl00_MainContentHolder_txtPastDate")
		get_weather_btn = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')
		get_date_input.click()
		get_date_input.clear()

		# modify date
		new_date_value = all_date_values[date]
		get_date_input.send_keys(f"{new_date_value}")
		get_weather_btn.send_keys(Keys.RETURN)

		# get 6:00 AM data
		day_temperature	 = driver.find_element(By.XPATH, "//*[@id='aspnetForm']/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[5]/td[3]/p").text[:2]
		day_humidity  	 = driver.find_element(By.XPATH, "//*[@id='aspnetForm']/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[5]/td[6]").text[:2]
		day_rainfall  	 = driver.find_element(By.XPATH, "//*[@id='aspnetForm']/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[5]/td[4]/div/div[3]").text[:4].strip()
		day_windspeed    = driver.find_element(By.XPATH, "//*[@id='aspnetForm']/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[5]/td[8]/div[2]").text[0]

		writer.writerow([new_date_value, 'Maasin', day_temperature, day_rainfall, day_windspeed, day_humidity])

f.close()

time.sleep(10)
