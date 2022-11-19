import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@given(u'User is on Home Page')
def step_impl(context):
    open_browser_and_goto_url()

@when(u'User navigates to Login Page')
def step_impl(context):
    driver.get("https://accounts.google.com/")

@when(u'User enters user as "bddtester2022" and password as "!234567*"')
def step_impl(context):
    driver.find_element(By.ID, 'identifierId').send_keys("bddtester2022")
    driver.find_element(By.XPATH, "//span[text() = 'Next']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@name='Passwd']"))).send_keys('!234567*')
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text() = 'Next'][@jsname='V67aGc']"))).click()
    #driver.implicitly_wait(10)

@then(u'Title of the page displayed is "Google Account"')
def step_impl(context):
    time.sleep(5)
    print("*****", driver.title)
    assert driver.title == "Google Account"

def open_browser_and_goto_url():
    global driver
    global wait
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
