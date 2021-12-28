from selenium import webdriver

class Browser(object):
    # Start browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Max load time
    driver.set_page_load_timeout(30)
    # Maximize screen
    driver.maximize_window()


    # Quit browser
    def browser_quit(self):
        self.driver.quit()

    # Clean browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()
