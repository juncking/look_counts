from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
# driver.maximize_window()
driver.implicitly_wait(30)

driver.find_elements_by_id("kw")[0].send_keys("你好")

driver.find_element_by_id("su").click()

driver.find_elements_by_css_selector("#content_left a")[3].click()

# driver.find_elements(by=id("s_kw_wrap")).send_keys("nihao")


sleep(5)
driver.quit()
