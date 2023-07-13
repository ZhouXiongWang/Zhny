import time

from selenium.webdriver.common.by import By

from BaseDriver.Base_Page import BasePage
from Page.BrowserClient.PortalMenu.HomePage.HomePage import HomePage


class Testbd():
    ele = (By.XPATH, '//*[@id="s-top-left"]/a[6]')
    def setup_class(self):
        self.main = HomePage()

    def test_baidu(self):
        self.main.driver.get("https://www.baidu.com")
        self.main.do_clickElement(*self.ele)
        headles=self.main.driver.window_handles
        self.main.driver.switch_to.window(headles[0])
        self.main.do_clickElement(*self.ele)
        headles=self.main.driver.window_handles
        self.main.driver.switch_to.window(headles[-1])
        self.main.do_closePageAndSwitchToHeadle()
        self.main.do_sendKey(by=By.XPATH,location='//*[@id="kw"]',key=123)
        time.sleep(2)
        self.main.do_screenshot()


    # def test_baidu2(self):
    #     self.main.driver.get("https://gitee.com/ceshiren/hogwarts-sdetck26/blob/master/app_auto_test/app_po/base/base_page.py")
    #     self.main.do_screenshotForPage()


