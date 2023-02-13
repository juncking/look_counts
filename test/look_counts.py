import time
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    InvalidArgumentException


def do_work():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")

    driver = webdriver.Chrome(chrome_options=chrome_options)

    # 获取视频的url
    f = open("./look_texts", "r")
    str = f.readlines()
    url_list = []
    str = [x.strip() for x in str]
    for s in str:
        if s != "" and s != " ":
            url_list.append(s)

    # 循环播放
    for url in url_list:
        print(url)
        driver.get(url)
        driver.implicitly_wait(30)

        # total_time = driver.find_element_by_class_name("bpx-player-ctrl-time-duration").get_attribute("textContent")
        # print(total_time)
        # hour, mis = total_time.split(":")
        # print(hour, mis)
        # time_counts = int(hour) * 60 + int(mis) + 2
        # print(time_counts)
        time_counts = 40

        # wait = ui.WebDriverWait(driver, 10)
        # lian = wait.until(lambda driver: driver.find_element_by_css_selector('.switch-button.on').is_enabled())
        try:
            driver.find_element_by_css_selector('.switch-button.on').click()
            # lian = driver.find_element_by_css_selector('.switch-button.on').is_enabled()
        except (NoSuchElementException, ElementClickInterceptedException, InvalidArgumentException):
            print("已关闭自动连播")
        # else:
        #     driver.find_element_by_css_selector('.switch-button.on').click()
        # if driver.find_element_by_css_selector('.switch-button.on').is_enabled() is True:
        #     driver.find_element_by_css_selector('.switch-button.on').click()
        # try:
        #     vol = driver.find_element_by_css_selector('.bpx-player-ctrl-btn-icon.bpx-player-ctrl-muted-icon').get_property(
        #         'style') is not None
        # except NoSuchElementException:
        #     print("网页已经静音")
        # else:
        #     driver.find_element_by_css_selector('.bpx-player-ctrl-btn-icon.bpx-player-ctrl-muted-icon').click()
        # vol = driver.find_element_by_css_selector('.bpx-player-ctrl-btn-icon.bpx-player-ctrl-muted-icon').get_property(
        #     'style') == []
        # if vol is True:
        #     m = driver.find_element_by_css_selector('.bpx-player-ctrl-btn.bpx-player-ctrl-volume').click()
        #     print(m)
        # print(vol)
        # driver.maximize_window()

        total_time = driver.find_element_by_class_name("bpx-player-ctrl-time-duration").get_attribute("textContent")
        print(total_time)
        hour, mis = total_time.split(":")
        print(hour, mis)
        timesd = int(hour) * 60 + int(mis) + 2
        print(timesd)

        sleep(timesd)
    driver.quit()


if __name__ == '__main__':
    # 次数变量
    times = input("请输入需要循环的次数：")
    times = int(times)
    for i in range(0, times):
        do_work()
        print("目前播放第" + f"{i}" + "遍")
    # while 1:
    #     do_work()
