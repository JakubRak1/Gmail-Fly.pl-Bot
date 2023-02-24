import os

from selenium.webdriver.common.by import By
from selenium import webdriver


class FlyPl(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(FlyPl, self).__init__(options=option)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_page(self, url):
        self.get(url)

    def accept_cookies(self):
        accept_cookie_btn = self.find_element(
            By.CSS_SELECTOR, 'button[id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
        )
        accept_cookie_btn.click()

    def change_date(self, date_select):
        date_menu = self.find_element(By.XPATH, '//div[@data-box-name="trp_depDate"]')
        date_menu.click()
        date = self.find_element(By.XPATH, f'//li[@data-sorting-option="{date_select}"]')
        date.click()

    def extract_price_data(self):
        price_data = self.find_element(By.XPATH, '//div[@class="price-per-all"]/span')
        price_data_number = int(price_data.text.replace('zł', '').replace(' ', '').strip())
        return price_data_number

    def extract_hotel_data(self):
        hotel_name = self.find_element(By.CSS_SELECTOR, 'h1[property="schema:name"]')
        return hotel_name.text
