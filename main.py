"""
Open https://tutorialsninja.com/demo/
Create a account / Register
Select 2 I phones
Take 1 Screen Shot
Select One Laptop
Select Delivery Date 28-08-2024
Checkout page and select estimate shipping & taxes fill details
apply flat shipping rates



"""


import time
import uuid
from calendar import calendar, month

from select import select
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()


#navigation
driver.get("https://tutorialsninja.com/demo")
time.sleep(1)

#select my account
my_account = driver.find_element('xpath','//span[text()="My Account"]')
my_account.click()
time.sleep(1)

#Selecting Register
Register = driver.find_element('xpath','//a[text()="Register"]')
Register.click()
time.sleep(2)

#selecting and fill firstname
first_name = driver.find_element('xpath','//input[@name="firstname"]')
first_name.click()
first_name.send_keys('Arjun')
time.sleep(2)

#select and fill last name
last_name = driver.find_element('xpath','//input[@name="lastname"]')
last_name.click()
last_name.send_keys('bhardwaj')
time.sleep(2)

#select and put email
email = driver.find_element('xpath','//input[@name="email"]')
email.click()
email.send_keys('ccyccddswc@gmail.com')

#select and put phone
phone = driver.find_element('xpath','//input[@name="telephone"]')
phone.click()
phone.send_keys('8000080000')

#password
password = driver.find_element('xpath','//input[@name="password"]')
password.click()
password.send_keys('jaishreeshyam123')

#password confirm
password_confirm = driver.find_element('xpath','//input[@name="confirm"]')
password_confirm.click()
password_confirm.send_keys('jaishreeshyam123')
time.sleep(3)

#T&C agree
agree = driver.find_element('xpath','//input[@name="agree"]')
agree.click()

#submitbutton
submit = driver.find_element('xpath','//input[@type="submit"]')
submit.click()
time.sleep(2)

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
time.sleep(1)

#accessing arrow for next image
next_click =driver.find_element("xpath",'//button[@title="Next (Right arrow key)"]')

#accessing all i phone pic using arrow
for i in range(0,5):
    next_click.click()
    time.sleep(1)

#taking screen shot
driver.save_screenshot(f'screenshot_{uuid.uuid4()}.png')

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
time.sleep(1)

#adding in to cart
add_cart = driver.find_element("id","button-cart")
add_cart.click()
time.sleep(1)

#selecting laptop field
laptop = driver.find_element('xpath','//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptop).perform()
time.sleep(1)

#showing all laptop
show_laptop = driver.find_element('xpath','//a[text()="Show AllLaptops & Notebooks"]')
show_laptop.click()
time.sleep(1)

#choosing hp laptop
choose_laptop = driver.find_element('xpath','//a[text()="HP LP3065"]')
choose_laptop.click()
time.sleep(1)

#scroll
add_to_laptop = driver.find_element('xpath','//button[@id ="button-cart"]')
add_to_laptop.location_once_scrolled_into_view
time.sleep(1)

#selecting calender
calendar = driver.find_element('xpath','//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

#august 2024
next_click_calender = driver.find_element('xpath','//th[@class="next"]')
month_year = driver.find_element('xpath','//th[@class="picker-switch"]')
while month_year.text != 'August 2024':
    next_click_calender.click()

time.sleep(1)
#Date 28
calendar_date = driver.find_element('xpath','//td[text()="28"]')
calendar_date.click()
time.sleep(2)
add_to_laptop.click()
time.sleep(1)

#items in cart
item_cart = driver.find_element("id",'cart-total')
item_cart.click()
time.sleep(2)

#select checkout option
checkout = driver.find_element('xpath','//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(2)

#Estimating shipping & Cost Taxes
shipping_cost = driver.find_element('xpath','//a[text()="Estimate Shipping & Taxes "]')
shipping_cost.click()
time.sleep(2)

#selecting dropdown
country_dropdown = driver.find_element('name','country_id')
country_dropdown.click()
time.sleep(3)

#selecting country
select_country = Select(country_dropdown)
select_country.select_by_visible_text('India')
time.sleep(3)

#selecting region dropdown
select_state = driver.find_element('name','zone_id')
select_state.click()
time.sleep(2)

#selecting state
select_state = Select(select_state)
select_state.select_by_visible_text('Haryana')
time.sleep(2)

# click pin-code input field and fill value
pin_field = driver.find_element('id','input-postcode')
pin_field.click()
pin_field.send_keys('123029')
time.sleep(3)

#button Get quotest
get_quotes = driver.find_element('xpath','//button[text()="Get Quotes"]')
get_quotes.click()
time.sleep(3)

#select shipping Rate
flat_shipping = driver.find_element('name','shipping_method')
flat_shipping.click()
time.sleep(3)

#apply shipping
apply_shipping = driver.find_element('id','button-shipping')
apply_shipping.click()
time.sleep(3)

