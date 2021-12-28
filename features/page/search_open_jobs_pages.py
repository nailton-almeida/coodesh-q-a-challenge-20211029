from selenium.webdriver.common.by import By
from browser import Browser

class CoodeshSearchJobs(Browser):

    def search_jobs(self, company):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@title="Ver Vagas"]').click()
        self.driver.find_element(By.NAME, "search").click()
        self.driver.find_element(By.NAME, "search").send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()

    def check_results_page(self):
        urlsearch = self.driver.current_url
        return urlsearch
