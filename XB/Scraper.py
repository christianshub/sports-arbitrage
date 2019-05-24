import platform
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

from bs4 import BeautifulSoup


def element_exist_css(DRIVER, element):

    try:
        DRIVER.find_element_by_css_selector(element)
    except NoSuchElementException:
        print('Element doesnt exist')
        return False
    return True


def element_css(DRIVER, element):

    try:
        time.sleep(2)

        return WebDriverWait(DRIVER, 10).until(EC.element_to_be_clickable(
                                              (By.CSS_SELECTOR, element)))

    except StaleElementReferenceException:
        print("element_css: StaleElementReferenceException")
    except WebDriverException:
        print("element_css: WebDriverException")


def login():

    element_css(DRIVER, '#loginout > div.fLogin2 > div').click()
    element_css(DRIVER, '#userLogin').send_keys('') # insert username
    element_css(DRIVER, '#userPassword').send_keys('') # insert password
    element_css(DRIVER, '#userConButton').click()

def history():

    pass

def XB_get_data_live(DRIVER):

    DRIVER.execute_script("window.scrollTo(0, 0);")

    games = DRIVER.find_elements_by_css_selector(
            '.c-events__item.c-events__item_col')

    for i in range(len(games)):
        game = games[i]

        try:
            if element_exist_css(game, 'div.c-events__time'):
                gametime = game.find_element_by_css_selector(
                                'div.c-events__time').text.split('\n')[0]

                if gametime.startswith('45:00'):

                    tab = ('div.c-events__more-wrap > a.c-events__more'
                           + '.c-events__more_bets.js-showMoreBets')

                    if element_exist_css(game, tab):
                        element_css(game, tab).click()
                        time.sleep(2)

                        getteams = game.find_element_by_css_selector(
                            ('.c-events__item.c-events__item_game.' +
                                'c-events-scoreboard__wrap >' +
                                'div.c-events-scoreboard' +
                                '> div:nth-child(1) > a > span')).text

                        teams = getteams.split('\n')
                        home, away = teams[0], teams[1]

                        bet_groups = game.find_elements_by_css_selector(
                                            '#allBetsTable > div > div')
                        for bet_group in bet_groups:

                            html = bet_group.get_attribute('innerHTML')
                            soup = BeautifulSoup(html, 'lxml')

                            title = soup.find(
                                'div', class_='bet-title bet-title_justify') \
                                .text.strip()

                            if title == '1x2':
                                print("*** 1X2 *** ")
                                FT_1X2(soup, 'div', {'class':
                                       'bets betCols3'}, home, away)

                            if title == 'Double Chance':
                                print("*** DOUBLE CHANCE *** ")
                                FT_DC(soup, 'div', {'class':
                                      'bets betCols3'}, home, away)

                            if title == 'Total':
                                print("*** ASIAN TOTAL *** ")
                                FT_OU(soup, 'div', {'class':
                                      'bets betCols2'}, home, away)

                            if title == 'Asian Total':
                                print("*** ASIAN OVER/UNDER *** ")
                                FT_AOU(soup,  'div', {'class':
                                       'bets betCols2'}, home, away)

                            if title == 'Handicap':
                                print("*** HANDICAP *** ")
                                FT_HDP(soup,  'div', {'class':
                                       'bets betCols2'}, home, away)

                            if title == 'Asian Handicap':
                                print("*** ASIAN HANDICAP *** ")
                                FT_AHDP(soup, 'div', {'class':
                                        'bets betCols2'}, home, away)

                        if element_exist_css(DRIVER, tab):
                            element_css(game, tab).click()

        except NoSuchElementException:
            print("NoSuchElementException")
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
        except TimeoutException:
            print("TimeoutException")
        except WebDriverException:
            print("WebDriverException")


if __name__ == '__main__':
    pass

else:
    from XB.Database import XB_Db
    from XB.bettypes.FT_1X2 import FT_1X2
    from XB.bettypes.FT_DC import FT_DC
    from XB.bettypes.FT_OU import FT_OU
    from XB.bettypes.FT_AOU import FT_AOU
    from XB.bettypes.FT_HDP import FT_HDP
    from XB.bettypes.FT_AHDP import FT_AHDP
