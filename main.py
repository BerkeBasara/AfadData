import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
import time
import pandas as pd



driver_path = "C:\webdrivers\chromedriver.exe"
browser = webdriver.Chrome(driver_path)

browser.get("https://tadas.afad.gov.tr/map")

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")
time.sleep(3)
tr_number = 0
page = 1
old_page = 1
common_page = 0
tıkla = browser.find_element(By.XPATH, "/html/body/app-root/div/app-login/div/div/div/div[1]/div/div[3]/div/button")
tıkla.click()
time.sleep(3)
next_page = False


while tr_number <= 10:

        tr_number = tr_number + 1
        #time.sleep(10)
        common_page = 0
        #time.sleep(10)
        browser.get("https://tadas.afad.gov.tr/list-waveform")
        time.sleep(5)

        range_input = browser.find_element(By.XPATH, "./html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/kendo-datepicker/span/kendo-dateinput/span/input")
        value = range_input.get_attribute('aria-valuenow')
        range_input.send_keys("46")
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys("36")
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys("23")
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys("2018")
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys("12")
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys(Keys.ARROW_LEFT)
        #time.sleep(1)
        range_input.send_keys("01")
        #time.sleep(10)

        ara_button = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/button[1]")
        ara_button.click()
        time.sleep(80)
        #time.sleep(10)

        if next_page is False:

                while common_page < (page-1):

                        #time.sleep(10)
                        next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]")
                        next_page.click()
                        #time.sleep(5)
                        common_page = common_page + 1

        else:
                while common_page < page:
                        next_page = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/kendo-pager/kendo-pager-next-buttons/a[1]")
                        next_page.click()
                        #time.sleep(3)
                        common_page = common_page + 1
                        next_page = False
                page = page + 1

        time.sleep(5)

        if tr_number == 1:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 2:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[2]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 3:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[3]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 4:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 5:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[5]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 6:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[6]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 7:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[7]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 8:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[8]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        elif tr_number == 9:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[9]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                next_page = False

        else:
                ham_veri = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-list-waveform/div/div/div/div/div/div[2]/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[10]/td[12]/button")
                time.sleep(5)
                ham_veri.click()
                time.sleep(10)

                veri_süzgeçleme = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process/div[6]/div/button[2]")
                time.sleep(5)
                veri_süzgeçleme.click()
                time.sleep(10)

                veriyi_işle = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-process2/form/div/div[2]/div[5]/div/button[3]")
                time.sleep(5)
                veriyi_işle.click()
                time.sleep(10)

                ham_veriyi_indir = browser.find_element(By.XPATH, "/html/body/app-root/div[2]/app-chart/div/div/div[5]/div/button[1]")
                time.sleep(5)
                ham_veriyi_indir.click()
                time.sleep(10)
                tr_number = 0
                time.sleep(5)
                next_page = True




