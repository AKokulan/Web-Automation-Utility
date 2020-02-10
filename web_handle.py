from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def launch_browser_with_chrome(driver_path):
    driver_path=driver_path
    driver=""

    try:
        driver = webdriver.Chrome(driver_path)
        session_id = driver.session_id
        return driver
    except:
        return "Failed to launch chrome browser with the exception: ", driver

def launch_browser_with_ie(driver_path):
    driver_path=driver_path
    driver=""
    try:
        driver = webdriver.Chrome(driver_path)
        session_id = driver.session_id
        return driver
    except:
        return "Failed to launch IE brwoser with the error: ",driver

def launch_browser_with_firefox(driver_path):
    driver_path=driver_path
    driver=""
    try:
        driver = webdriver.Chrome(driver_path)
        session_id = driver.session_id
        return driver
    except:
        return "Failed to launch Firefox brwoser with the error: ",driver

def close_browser(driver):
    driver=driver
    try:
        driver = driver.close()
        return driver
    except:
        return "Failed to launch Firefox brwoser with the error: ",driver

def open_website(driver,url):
    driver, url=driver,url
    open_web=""
    try:
        open_web=driver.get(url)
        success="Successfully the opened website with url: ",url
        return success
    except:
        return "Failed to open the website with the error: ",open_web

def read_text(driver,xpath,wait_time):
    driver, xpath, wait_time=driver,xpath,wait_time
    element=""
    try:
        element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,  xpath)))
        element_text=driver.find_element_by_xpath(xpath).text
        return element_text
    except exceptions.TimeoutException:
        return "TimeoutException"
    except exceptions.NoSuchElementException:
        return "NoSuchElementException"
    except:
        return 'Failed to read the text with the error: ',element

def write_text(driver,xpath,wait_time,text):
    driver, xpath, wait_time, text=driver,xpath,wait_time,text
    element=""
    try:
        element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,  xpath)))
        element = driver.find_element_by_xpath(xpath)
        driver.find_element_by_xpath(xpath).click()
        driver.find_element_by_xpath(xpath).send_keys(text)
        return "Successfully updated the text"

    except exceptions.TimeoutException:
        return "TimeoutException"
    except exceptions.NoSuchElementException:
        return "NoSuchElementException"
    except:
        return 'Failed to update the text with the error: ',element

def click_left_button(driver,xpath,wait_time,number_of_clicks):
    driver, xpath, wait_time, number_of_clicks=driver,xpath,wait_time,number_of_clicks
    element=""
    try:
        element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,  xpath)))
        element=driver.find_element_by_xpath(xpath)

        if number_of_clicks==1:
            element.click()
        if number_of_clicks==2:
            action_chains = ActionChains(driver)
            action_chains.double_click(element).perform()
        return "Successfully clicked button"

    except exceptions.TimeoutException:
        return "TimeoutException"
    except exceptions.NoSuchElementException:
        return "NoSuchElementException"
    except:
        return 'Failed to click the button with the error: ',element

def drag_drop(driver,source_xpath,target_xpath,wait_time):
    driver, source_xpath, target_xpath, wait_time=driver,source_xpath,target_xpath,wait_time
    source_element_wait, target_element_wait="",""
    try:
        source_element_wait = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,  source_xpath)))
        target_element_wait= WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, source_xpath)))
        source_element=driver.find_element_by_xpath(source_xpath)
        target_element = driver.find_element_by_xpath(source_xpath)

        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(source_element,target_element).perform()
        return "Successfully completed drag and drop"

    except exceptions.TimeoutException:
        return "TimeoutException"
    except exceptions.NoSuchElementException:
        return "NoSuchElementException"
    except:
        error='Failed to do drag and drop with the error: ',source_element_wait,target_element_wait
        return error

def enter_keys(driver,key,wait_time,xpath):
    try:
        driver=driver
        key=key
        xpath=xpath

        if key=="ENTER" or key=="enter":
            element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

    except:
        error="unable to click keys"
        print(error)










