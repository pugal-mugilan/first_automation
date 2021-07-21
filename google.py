from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Lenovo\\Downloads\\chromedriver.exe")
driver.get("http://www.google.com")

que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("tennis")
que.send_keys(Keys.ENTER)
driver.find_element_by_tag_name("cite").click()