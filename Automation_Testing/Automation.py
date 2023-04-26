import time
from common_functionality import *
import obect_repository as map
from log import log_files
logger = log_files("Automation")


class Automation(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.driver = WebDriver()
        self.task_text = None
        self.description_text = None
        self.sub_task_task_name = None
        self.sub_task_description = None

    def click_login_link(self):
        try:
            login = self.driver.get_element_by_xpath(map.login_link)
            login.click()
            logger.info('login link clicked')
        except Exception as ex:
            logger.error('login failed')
            self.driver.capture_screenshot("login")
            raise Exception(ex)

    def enter_email(self, email):
        try:
            email_field = self.driver.get_element_by_id(map.email)
            email_field.click()
            email_field.send_keys(email)
            logger.info(f"entered email:{email} ")
        except Exception as ex:
            logger.error('enter_email failed')
            self.driver.capture_screenshot("enter_email")
            raise Exception(ex)

    def enter_password(self, password):
        try:
            self.password = password
            password_field = self.driver.get_element_by_id(map.password)
            password_field.send_keys(password)
            logger.info(f'entered password: {password}')
        except Exception as ex:
            logger.error('enter_password failed')
            self.driver.capture_screenshot("enter_password")
            raise Exception(ex)

    def click_login_btn(self):
        try:
            login_btn = self.driver.get_element_by_xpath(map.login_btn)
            login_btn.click()
            logger.info('login_btn clicked')
            time.sleep(10)
        except Exception as ex:
            logger.error('click_login_btn failed')
            self.driver.capture_screenshot("click_login_btn")
            raise Exception(ex)

    def verify_login(self):
        try:
            assert "Today: Todoist" == self.driver.get_page_title("Today: Todoist")
            logger.info('verify_login verified')
        except Exception as ex:
            logger.error('verify_login failed')
            self.driver.capture_screenshot("verify_login")
            raise Exception(ex)

    def click_add_task(self):
        try:
            add_task = self.driver.get_element_by_xpath(map.add_task)
            add_task.click()
            logger.info('add_task clicked')
        except Exception as ex:
            logger.error('add_task failed')
            self.driver.capture_screenshot("add_task")
            raise Exception(ex)

    def open_created_task(self):
        try:
            open_created_task = self.driver.get_element_by_presence(map.verify_task % self.task_text)
            open_created_task.click()
            logger.info('open_created_task clicked')
        except Exception as ex:
            logger.error('open_created_task failed')
            self.driver.capture_screenshot("open_created_task")
            raise Exception(ex)

    def cancel_add_task(self):
        try:
            cancel_task_btn = self.driver.get_element_by_xpath(map.cancel_task_btn)
            cancel_task_btn.click()
            logger.info('cancel_task_btn clicked')
        except Exception as ex:
            logger.error('cancel_add_task failed')
            self.driver.capture_screenshot("cancel_add_task")
            raise Exception(ex)

    def enter_task_details(self, task_text, description_text):
        try:
            self.task_text = task_text
            self.description_text = description_text
            task_name = self.driver.get_element_by_xpath(map.task_name)
            task_name.click()
            task_name.send_keys(task_text)
            logger.info(f'{task_text} entered')
            description = self.driver.get_element_by_xpath(map.description)
            description.click()
            description.send_keys(description_text)
            logger.info(f'{description_text} entered')
            add_task_btn = self.driver.get_element_by_xpath(map.add_task_btn)
            time.sleep(20)
            add_task_btn.click()
            logger.info('add_task_btn clicked')
        except Exception as ex:
            logger.error('enter_task_details failed')
            self.driver.capture_screenshot("enter_task_details")
            raise Exception(ex)

    def verify_task_creation(self):
        try:
            verify_task = self.driver.get_element_by_presence(map.verify_task % self.task_text)
            logger.info('task_creation successful')
            self.cancel_add_task()
        except Exception as ex:
            logger.error('verify_task_creation failed')
            self.driver.capture_screenshot("verify_task_creation")
            raise Exception(ex)

    def mark_task_complete(self):
        try:
            mark_task_complete = self.driver.get_element_by_xpath(map.mark_task_complete)
            mark_task_complete.click()
            logger.info('mark_task_complete clicked')
            logger.info('marked as complete successfully.')
        except Exception as ex:
            logger.error('mark_task_complete failed')
            self.driver.capture_screenshot("mark_task_complete")
            raise Exception(ex)

    def add_sub_task(self, sub_task_task_name, sub_task_description):
        try:
            self.sub_task_task_name = sub_task_task_name
            self.sub_task_description = sub_task_description
            add_sub_task = self.driver.get_element_by_xpath(map.add_sub_task)
            add_sub_task.click()
            logger.info('add_sub_task clicked')
            self.enter_task_details(sub_task_task_name, sub_task_description)
            time.sleep(5)
            self.cancel_add_task()
            close_modal = self.driver.get_element_by_xpath(map.close_modal)
            close_modal.click()
            logger.info('close_modal clicked')
            #self.verify_sub_task_creation()
            #logger.info('marked as complete successfully.')
        except Exception as ex:
            logger.error('add_sub_task failed')
            self.driver.capture_screenshot("add_sub_task")
            raise Exception(ex)

    def verify_sub_task_creation(self):
        try:
            self.driver.page_refresh()
            verify_task = self.driver.get_element_by_presence(map.verify_task % self.sub_task_task_name)
            logger.info(verify_task)
            logger.info('verify_sub_task_creation successful')
        except Exception as ex:
            logger.error('verify_sub_task_creation failed')
            self.driver.capture_screenshot("verify_sub_task_creation")
            raise Exception(ex)