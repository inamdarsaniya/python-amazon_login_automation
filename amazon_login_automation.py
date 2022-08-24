from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
thing=input("What do you wish to search for on Amazon : ")
driver=webdriver.Chrome(r"O:\SORTED\\exe\\chromedriver.exe")

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

login=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("put your email here")
Submita=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
Submita.click()

time.sleep(1)

passw=driver.find_element_by_id("ap_password")
passw.send_keys("put your password here")

Submitb=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input")
Submitb.click()

time.sleep(1)

searchbox=driver.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys(thing)

time.sleep(1)

Find=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
Find.click()

time.sleep(5)

driver.quit()

