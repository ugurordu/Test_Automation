import time
from random import randint
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')

#for Windows use the next line
chromeDriverPath = r"C:\Users\Ugur\Desktop\chromedriver.exe"   #add your chromedriver path
driver = webdriver.Chrome(chromeDriverPath, chrome_options=options)
driver.maximize_window()
driver.set_page_load_timeout
driver.get('https://www.gittigidiyor.com')

time.sleep(1)
closecookiemenu = driver.find_elements_by_css_selector('a.tyj39b-3.fEwnjq')    #close cookie button
try:
    if closecookiemenu[0].is_displayed():
        try:
            closecookiemenu[0].click()
        except ElementClickInterceptedException:
            print("no cookie menu")
        except IndexError:
            print("no cookie menu")
except ElementClickInterceptedException:
    print("no cookie menu")
except IndexError:
    print("no cookie menu")

login = driver.find_element_by_css_selector('div.ndodpt-1.cESNHb')   # hover login button
action = ActionChains(driver)
action.move_to_element(login).perform()
time.sleep(1)

go_to_login_page = driver.find_element_by_xpath('//a[@data-cy="header-login-button"]').click() #click login button
time.sleep(1)

email = driver.find_element_by_xpath('//input[@name="kullanici"]').send_keys('#####@######') #write your mail account   #####login with mail and password#####
password = driver.find_element_by_xpath('//input[@name="sifre"]').send_keys('############') #write your password
login_button = driver.find_element_by_xpath('//input[@id="gg-login-enter"]').click()  #click login enter button
time.sleep(1)

search = driver.find_element_by_xpath('//input[@data-cy="header-search-input"]').send_keys('bilgisayar')  #search keyword 
search_click = driver.find_element_by_xpath('//button[@data-cy="search-find-button"]').click() #click search button
time.sleep(1)

scroll = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #scroll buttom 
page_click = driver.find_element_by_css_selector('#best-match-right div.pager.pt30.hidden-m.gg-d-24 ul li:nth-child(2) a').click() #click next page
time.sleep(1)

products = driver.find_elements_by_css_selector('ul.catalog-view.clearfix.products-container li a.product-link') #take all product links
pick_random_products = products[randint(0, len(products)-1)] #pick random product
pick_random_products.click()  #click random product
time.sleep(1)

try:                                                                                            #######check price########
    check_first_price = driver.find_element_by_css_selector('#sp-price-discountPrice').text   #discount price 1    
except NoSuchElementException:
    try:
        check_first_price = driver.find_element_by_css_selector('#sp-price-lowPrice').text    #discount price 2
    except NoSuchElementException:
        check_first_price = driver.find_element_by_css_selector('#sp-price-highPrice').text    #normal price 1
    
add_cart = driver.find_element_by_css_selector('#add-to-basket').click()   #add cart
time.sleep(1)

go_to_cart = driver.find_element_by_css_selector('a.gg-ui-btn-default.padding-none').click()  # go to cart
time.sleep(1)

try:
    check_cart_price = driver.find_element_by_css_selector('strong.real-discounted-price').text  #check cart discount price 
except NoSuchElementException:
    check_cart_price = driver.find_element_by_css_selector('div.total-price strong').text #check cart normal price

if check_first_price == check_cart_price :              #compare prices
    print('price is correct')
else:
    print('price changed')

time.sleep(1)

increase_count = driver.find_element_by_css_selector('div.gg-input.gg-input-select select option:nth-child(2)').click()  #increase the piece
time.sleep(1)

check_count = driver.find_element_by_css_selector('div.gg-d-16.detail-text').text   #check the piece count

if '2 Adet' in check_count:             #compare css text with piece count
    print('product count is correct')
else:
    print('product count is not correct')
time.sleep(1)

del_product = driver.find_element_by_css_selector('a.btn-delete.btn-update-item').click()   #dell all products from cart
time.sleep(1)

check_cart = driver.find_element_by_xpath('//*[@id="empty-cart-container"]/div[1]/div[1]/div/div[2]/h2').text   #check cart 
if 'bulunmamaktadır' in check_cart:
    print('cart is empty')

driver.quit()