from gettext import gettext
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



def test_search():
    mismatches = []
    # Open eBay watch page ( Watch for sale | eBay  )
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

    # Select option Brand / Rolex in Filter panel
    rolex_checkbox = driver.find_element(By.XPATH, "//input[@aria-label='Rolex']")
    rolex_checkbox.click()
    wait = WebDriverWait(driver, 10)

    # Verify the first two result items contain “rolex” in their title
    rolex_titles = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//span[@role='heading'][@aria-level='3']")))
    rolex_prices = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//span[@class='s-item__price']")))

    if "rolex" not in rolex_titles[0].text.lower():
        mismatches.append("Title 1 doesn't contain 'rolex'")
    if "rolex" not in rolex_titles[1].text.lower():
        mismatches.append("Title 2 doesn't contain 'rolex'")

    # Store title and price of the first two results in a variable
    rolex_results = [
        {
            "title" : rolex_titles[0].text,
            "price" : rolex_prices[0].text.strip('$US ').replace(',', ''),
        },
        {
            "title": rolex_titles[1].text,
            "price": rolex_prices[1].text.strip('$US ').replace(',', ''),
        }
    ]

    # Open item in a new tab and verify the title and the price by comparing them with the stored data
    actions = ActionChains(driver)
    actions.key_down(Keys.COMMAND).click(rolex_titles[0]).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1/span[@class='ux-textspans ux-textspans--BOLD']")))
    price = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='x-price-primary']/span[@class='ux-textspans']")))

    if title.text != rolex_results[0]["title"]:
        mismatches.append(f"Title doesn't match: expected='{rolex_results[0]['title']}', actual='{title.text}'")
    if price.text.strip('$US ').replace(',', '') != rolex_results[0]["price"]:
        mismatches.append(f"Price doesn't match: expected='{rolex_results[0]['price']}', actual='{price.text.strip('$US ').replace(',', '')}'")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    actions.key_down(Keys.COMMAND).click(rolex_titles[1]).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    title = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1/span[@class='ux-textspans ux-textspans--BOLD']")))
    price = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='x-price-primary']/span[@class='ux-textspans']")))

    if title.text != rolex_results[1]["title"]:
        mismatches.append(f"Title doesn't match: expected='{rolex_results[1]['title']}', actual='{title.text}'")
    if price.text.strip('$US ').replace(',', '') != rolex_results[1]["price"]:
        mismatches.append(f"Price doesn't match: expected='{rolex_results[1]['price']}', actual='{price.text.strip('$US ').replace(',', '')}'")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


    # Uncheck “Rolex“ option
    driver.find_element(By.XPATH, "//input[@aria-label='Rolex']").click()

    # Check “Casio“ option
    casio_checkbox = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Casio']")))
    casio_checkbox.click()

    # Verify the last two result items contain “Casio“ in their title
    casio_titles = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//span[@role='heading'][@aria-level='3']")))
    last = len(casio_titles) - 1
    if "casio" not in casio_titles[last].text.lower():
        mismatches.append("Last title doesn't contain 'casio'")
    if "casio" not in casio_titles[last - 1].text.lower():
        mismatches.append("Last but one title doesn't contain 'casio'")

    # Save and print all the mismatches if any
    driver.quit()

    return mismatches

print(test_search())