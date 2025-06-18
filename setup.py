from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver():
    options = Options()
    options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver