"""
Open https://tutorialsninja.com/demo/
Select 2 I phones
Take 1 Screen Shot
Select One Laptop
Select Delivery Date 28-08-2024
Checkout page and see apply filters
print the total price and the confirmation message in the console

"""


import time
import uuid
from calendar import calendar, month

from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()


#navigation
driver.get("https://tutorialsninja.com/demo")
time.sleep(1)


#getting phones
phones = driver.find_element("xpath",'//a[text()="Phones & PDAs"]')
phones.click()
time.sleep(1)

#selecting i phone
iphone = driver.find_element("xpath",'//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

#clicking i phone first image
first_pic = driver.find_element("xpath",'//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

#accessing arrow for next image
next_click =driver.find_element("xpath",'//button[@title="Next (Right arrow key)"]')

#accessing all i phone pic using arrow
for i in range(0,5):
    next_click.click()
    time.sleep(2)

#taking screen shot
#driver.save_screenshot(f'screenshot_{uuid.uuid4()}.png')

#closing pic
x_button = driver.find_element("xpath",'//button[@title="Close (Esc)"]')
x_button.click()

time.sleep(1)

#selecting quantity of i phone
Quantity = driver.find_element("id",'input-quantity')
Quantity.click()
time.sleep(1)
Quantity.clear()
time.sleep(1)
Quantity.send_keys('2')
time.sleep(2)

#adding in to cart
add_cart = driver.find_element("id","button-cart")
add_cart.click()
time.sleep(2)

#selecting laptop field
laptop = driver.find_element('xpath','//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptop).perform()
time.sleep(2)

#showing all laptop
show_laptop = driver.find_element('xpath','//a[text()="Show AllLaptops & Notebooks"]')
show_laptop.click()
time.sleep(2)

#choosing hp laptop
choose_laptop = driver.find_element('xpath','//a[text()="HP LP3065"]')
choose_laptop.click()

#scroll
add_to_laptop = driver.find_element('xpath','//button[@id ="button-cart"]')
add_to_laptop.location_once_scrolled_into_view
time.sleep(2)

#selecting calender
calendar = driver.find_element('xpath','//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(2)

#august 2024
next_click_calender = driver.find_element('xpath','//th[@class="next"]')
month_year = driver.find_element('xpath','//th[@class="picker-switch"]')
while month_year.text != 'August 2024':
    next_click_calender.click()

time.sleep(3)
#Date 28
calendar_date = driver.find_element('xpath','//td[text()="28"]')
calendar_date.click()
time.sleep(2)
add_to_laptop.click()
time.sleep(1)

item_cart = driver.find_element("id",'cart-total')
item_cart.click()
time.sleep(2)

checkout = driver.find_element('xpath','//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(3)
