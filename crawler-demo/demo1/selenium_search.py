import os
from selenium import webdriver


def main():

    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    # driver = webdriver.Chrome()
    driver.get('http://example.webscraping.com/search')
    driver.find_element_by_id('search_term').send_keys('.')
    driver.execute_script("document.getElementById('page_size').options[1].text = '1000'");

    driver.find_element_by_id('search').click()
    driver.implicitly_wait(30)
    links = driver.find_elements_by_css_selector('#results a')
    countries = [link.text for link in links]
    driver.close()
    print countries


if __name__ == '__main__':
    main()
