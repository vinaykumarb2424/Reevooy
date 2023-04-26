import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self):
        #options = webdriver.ChromeOptions()
        #options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.driver.get("https://todoist.com/")
        self.driver.maximize_window()

    def get_element_by_id(self, id_, timeout=40):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.ID, id_))
        )
        return element

    def get_element_by_class_name(self, class_name, timeout=40):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        return element

    def get_element_by_xpath(self, xpath, timeout=30):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element

    def get_elements_by_xpath(self, xpath, timeout=30):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        return element

    def get_element_by_tag(self,  tag, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, tag))
        )
        return element

    def get_elements_by_tag(self,  tag, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, tag))
        )
        return element

    def get_element_by_presence(self, xpath, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def get_element_by_visible(self, xpath, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element

    def get_elements_by_visible(self, xpath, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((By.XPATH, xpath))
        )
        return element

    def get_elements_by_presence(self, xpath, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
         EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        return element

    def scroll_by_pixel(self):
        scroll = self.driver.execute_script("window.scrollBy(0, 500)", "")
        return scroll

    def switch_frame(self, id_, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, id_))
        )
        return element

    def switch_out_frame(self):
        self.driver.switch_to.default_content()

    def get_page_title(self, title, timeout=30):
        """
        return title of page focused
        :return:
        """
        WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        return self.driver.title

    def capture_screenshot(self, filename):
        directory = str(Path(os.getcwd()).parent) + "/Screenshots"
        print(directory)
        self.driver.save_screenshot("%s/%s" % (directory, filename + ".png"))

    def page_refresh(self):
        self.driver.refresh()



