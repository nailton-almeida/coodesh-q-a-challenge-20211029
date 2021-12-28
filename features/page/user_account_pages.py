from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from browser import Browser


class CoodeshLoginPage(Browser):

    def login_into_platform(self, email, password):
        self.driver.find_element_by_xpath('//button[text()="Login"]').click()
        self.driver.find_element(By.LINK_TEXT, "Entrar").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".col-12 > .transition-3d-hover").click()

    def create_account(self, name, email, password):
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//button[text()="Login"]').click()
        # first screen to type information users
        self.driver.find_element(By.LINK_TEXT, "Criar conta").click()
        self.driver.find_element(By.ID, "displayName").click()
        self.driver.find_element(By.ID, "displayName").send_keys(name)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password").click()
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.SPACE)
        actions.perform()

        # second screen to type information users
        self.driver.find_element(By.CSS_SELECTOR, ".col-12 > .transition-3d-hover").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[text()='QA / Testes']").click()
        self.driver.find_element_by_xpath("//div[text()='Até um ano']").click()
        professional_moment = Select(self.driver.find_element_by_id('preferences.job_search'))
        professional_moment.select_by_value('searching_asap')
        self.driver.find_element(By.CSS_SELECTOR, ".react-tel-input > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-tel-input > .form-control").send_keys('75992602608')
        self.driver.find_element(By.CSS_SELECTOR, "#address\.city").click()
        self.driver.find_element(By.CSS_SELECTOR, "#address\.city").send_keys('Gandu')
        self.driver.find_element(By.CSS_SELECTOR, ".justify-content-end > .transition-3d-hover").click()

        # Third screen to type information users
        self.driver.implicitly_wait(5)
        race = Select(self.driver.find_element_by_id('race'))
        race.select_by_value('black')
        gender = Select(self.driver.find_element_by_id('gender'))
        gender.select_by_value('noanswer')
        sexual_orientation = Select(self.driver.find_element_by_id('sexual_orientation'))
        sexual_orientation.select_by_value('noanswer')
        disabilities = Select(self.driver.find_element_by_id('disabilities\.type'))
        disabilities.select_by_value('none')
        self.driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .btn-primary").click()
        self.driver.find_element(By.CLASS_NAME, "btn-text").click()

    def check_user_creation(self):
        username = self.driver.find_element(By.CLASS_NAME, 'h2')
        return username.text
