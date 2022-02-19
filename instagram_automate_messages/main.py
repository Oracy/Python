import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

user = ["netoofc94"]
message = "Testing my new bot :)"


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = "https://www.instagram.com/"
        self.bot = driver
        self.login()


    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_all_elements_located((By.NAME, 'oracy_'))
        )
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_all_elements_located((By.NAME, 'Oracy=21'))
        )
        enter_password.send_keys(self.password)

        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # 1st pop-up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
            ).click()
        time.sleep(3)

        # 2nd pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]'
            ).click()
        time.sleep(4)

        # Direct button
        self.bot.find_element_by_xpath(
            '//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]'
            ).click()
        time.sleep(3)

        # Clicks on pencil icon
        self.bot.find_element_by_xpath(
            '//a[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button'
            ).click()
        time.sleep(2)

        for i in user:
            # Enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input'
            ).send_keys(i)
            time.sleep(2)

            # Click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div[2]/div'
            ).click()
            time.sleep(2)

            # Next Button
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[1]/div/div[2]/div/button'
            ).click()
            time.sleep(2)

            # Click on message area
            send = self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
            )

            # Types message
            send.send_keys(self.message)
            time.sleep(1)

            # Send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            # Clicks on direct option or pencil icon
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
            ).click()
            time.sleep(2)


def init():
    bot('oracy_', 'aaa', user, message)

    input("DONE")


init()
