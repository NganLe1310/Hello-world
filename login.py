from selenium.webdriver.common.by import By
import time
from setup import init_driver  

def perform_login(driver):

    username_field = driver.find_element(By.NAME, "username").send_keys("Admin")
    password_field = driver.find_element(By.NAME, "password").send_keys("admin123")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(3)  

def main():
    driver = init_driver()     
    time.sleep(2)             
    perform_login(driver)
    time.sleep(5)             
    driver.quit()

if __name__ == "__main__":
    main()
