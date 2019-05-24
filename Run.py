import  platform
import  time

from    AO.Scraper      import AO_Login
from    AO.Scraper      import AO_get_data_live
from    AO.Database     import AO_Db
from    XB.Scraper      import XB_get_data_live
from    XB.Database     import XB_Db
from    Calculator.main import Calculator
from    Calculator.db   import AR_Db
from    selenium        import webdriver

def Run():
    print("RUN:    Welcome...\n")

    if platform.system() == 'Windows':
        driverPath = '.\\browser\\win32\\chromedriver'
    elif platform.system() == 'Darwin':
        driverPath = './browser/mac64/chromedriver'

    options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images': 2,
             'disk-cache-size': 4096}

    options.add_argument('--enable-file-cookies')
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--disable-infobars')
    driverXB = webdriver.Chrome(driverPath, options=options)
    driverAO = webdriver.Chrome(driverPath, options=options)

    driverAO.get('https://bet.asianodds88.com/Login.aspx')  # alt: http://ao0188.com/Login.aspx
    AO_Login(driverAO)
    driverXB.get('https://1xbet.cm/en/live/Football/')

    while True:

        AO_Db.create_tbls()
        XB_Db.create_tbls()
        AR_Db.create_tbls()

        AO_get_data_live(driverAO)
        XB_get_data_live(driverXB)

        c = Calculator()
        c.compare2ways()

        print("\nRUN:    Arbs should be above this line if any. \
        Now wait 5 minutes and then we re-run...\n")
        time.sleep(300)

if __name__ == '__main__':
    Run()  # Start the program
