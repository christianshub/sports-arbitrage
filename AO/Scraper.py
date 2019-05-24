from AO.bettypes.FT  import FT
from AO.bettypes.OU  import OU
from AO.bettypes.HDP import HDP

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import platform
import time

def find_elements(driver, css_elements):
    time.sleep(2)
    return driver.find_elements_by_css_selector(css_elements)

def find_element(driver, css_element):
    time.sleep(2)
    try:
        return WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.CSS_SELECTOR, css_element)))

    except StaleElementReferenceException:
        pass


def AO_Login(driver):
    print("AO:     Pressing Buttons...")
    find_element(driver, '#txtUserID').send_keys('') # input username here
    find_element(driver, '#txtPass').send_keys('') # input password here
    find_element(driver, '#btnDoLogin').click()


def AO_get_data_live(driver):

    print("AO:     Waiting 10 seconds to make sure we are logged in...")
    time.sleep(10)  # Is needed to not bug

    print("AO:     Scraping...")
    find_element(driver, '#lbl_running').click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    leagues = soup.find_all('div', class_='ileaugegroup')
    matches = str(leagues).split('game_panel_tmp igametable')

    for i in range(1, len(matches)):
        soup = BeautifulSoup(matches[i], 'lxml')

        gtime = soup.find('span', class_='MatchTime samehidegroup0').text

        if gtime == 'HT':

            try:
                H = soup.find('span', class_='Home samehidegroup1').text
                A = soup.find('span', class_='Away samehidegroup1').text

                FT(soup, H, A)
                OU(soup, H, A)
                HDP(soup, H, A)

            except AttributeError:
                # print('AO:     AttributeError')
                pass
            except StaleElementReferenceException:
                print("AO:     StaleElementReferenceException, returning..")
                return AO_get_data_live(driver)
            except TimeoutException:
                print("AO:     TimeoutException, returning..")
                return AO_get_data_live(driver)

    print("AO:     Scraped...\n")
