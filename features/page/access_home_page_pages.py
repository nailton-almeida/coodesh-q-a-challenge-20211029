from selenium.webdriver.common.by import By
from browser import Browser


class CoodeshMainPage(Browser):

    def access_page(self, url):
        self.driver.get(url)

    def check_load_page(self):
        textpage = self.driver.find_element(By.LINK_TEXT, "Ver Vagas")
        assert(textpage.is_displayed())
