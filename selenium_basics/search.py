from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def task_one():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    get_url = driver.current_url
    print(str(get_url))
    driver.quit()

# task_one()

def task_two():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='gh-l-h1']")))
    print(str(driver.current_url))
    driver.quit()

# task_two()

def task_three():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='gh-l-h1']")))
    print(str(driver.current_url))
    element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    element.send_keys("women watch")
    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()
    driver.quit()

# task_three()
def task_four():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='gh-l-h1']")))
    print(str(driver.current_url))
    element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    element.send_keys("women watch")
    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='srp-controls__count-heading']"
                                                         "[contains(., 'results for women watch')]")))
    driver.quit()

# task_four()