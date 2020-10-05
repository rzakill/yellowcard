from behave_webdriver.steps import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# common variables are defined in this block
site = 'https://5f71dbf24c4f9b00073240bd--yellowcard-webapp.netlify.app/auth/login'
phone = '8181413926'
password = 'Password1@'
pin = "123456"



@given('user is able to access the yellow card app')
def step_impl(context):
    context.browser.get(site)

    assert context.browser.title == "Yellow Card"


@when('user logs in with correct credentials')
def step_impl(context):
    context.browser.get(site)

    # Input appropriate credentials
    context.browser.find_element_by_class_name("phone-input").send_keys(phone)
    context.browser.find_element_by_class_name("input").send_keys(password)
    context.browser.find_element_by_class_name("main-btn").click()

    # Cause web driver to wait for OTP element to compensate for page load
    WebDriverWait(context.browser, 18).until(
    ec.visibility_of_element_located((By.CLASS_NAME, "codeInput")))

    # OTP is supplied
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_class_name("codeInput").send_keys(pin)
    context.browser.find_element_by_class_name("main-btn").click()

    # Cause web driver to wait for wallet link and compensate for any lag in page load
    WebDriverWait(context.browser, 20).until(
        ec.visibility_of_element_located((By.LINK_TEXT, "Wallet")))

    # Clicking on the actual link requires getting the xpath. Not the preferred method but it's functional
    linkText = context.browser.find_element_by_xpath("//*[@id='available-balance']/div/div/div/div/div[2]/div/div[2]/a").text
    assert linkText == "Wallet"
    context.browser.find_element_by_xpath("//*[@id='available-balance']/div/div/div/div/div[2]/div/div[2]/a").click()

    # Cause web driver to wait for the element required to begin buying
    WebDriverWait(context.browser, 17).until(
        ec.visibility_of_element_located((By.XPATH, "//*[@id='wallets']/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[4]/button[1]")))

    # execute script is used because another element seems intercept the required click
    buy = context.browser.find_element_by_xpath("//*[@id='wallets']/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[4]/button[1]")
    context.browser.execute_script("arguments[0].click();", buy)


    WebDriverWait(context.browser, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[4]/div/div/div[2]/div[4]/div/div[2]/div/div/div[2]")))

    context.browser.find_element_by_xpath("//*[@id='app']/div[4]/div/div/div[2]/div[4]/div/div[2]/div/div/div[2]").click()

    # Clear input field just in case
    context.browser.find_element_by_class_name("bank-input2").clear()
    context.browser.find_element_by_class_name("bank-input2").send_keys("5000")

    # Review and Confirm Transaction
    confirm = context.browser.find_element_by_xpath("//div[@id='review_and_confirm']/div[5]/button")
    context.browser.execute_script("arguments[0].click();", confirm)

    WebDriverWait(context.browser, 30).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='app']/div[4]/div[2]/div/div/div/button")))

    # Verify that transaction was successful
    assert context.browser.find_element_by_xpath("//div[@id='app']/div[4]/div[2]/div/div/div/button").text == 'Done'
    # Let's ensure page loads completely
    context.browser.implicitly_wait(10)
    done = context.browser.find_element_by_xpath("//div[@id='app']/div[4]/div[2]/div/div/div/button")
    context.browser.execute_script("arguments[0].click();", done)

    # Wait for the confirmation modal to be fully rendered
    WebDriverWait(context.browser, 20).until(
        ec.visibility_of_element_located((By.LINK_TEXT, "Wallet")))

    # Clicking on the actual link requires getting the xpath. Not the preferred method but it's functional
    linkText = context.browser.find_element_by_xpath(
        "//*[@id='available-balance']/div/div/div/div/div[2]/div/div[2]/a").text
    assert linkText == "Wallet"
    context.browser.find_element_by_xpath("//*[@id='available-balance']/div/div/div/div/div[2]/div/div[2]/a").click()

    # Cause web driver to wait for the element required to begin buying
    WebDriverWait(context.browser, 17).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='wallets']/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[4]/button[1]")))

    # execute script is used because another element seems intercept the required click
    buy = context.browser.find_element_by_xpath(
        "//*[@id='wallets']/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[4]/button[1]")
    context.browser.execute_script("arguments[0].click();", buy)

    WebDriverWait(context.browser, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[4]/div/div/div[2]/div[4]/div/div[2]/div/div/div[2]")))

    context.browser.find_element_by_xpath(
        "//*[@id='app']/div[4]/div/div/div[2]/div[4]/div/div[2]/div/div/div[2]").click()

    # Clear input field just in case
    context.browser.find_element_by_class_name("bank-input2").clear()
    context.browser.find_element_by_class_name("bank-input2").send_keys("5000")

    # Review and Confirm Transaction
    confirm = context.browser.find_element_by_xpath("//div[@id='review_and_confirm']/div[5]/button")
    context.browser.execute_script("arguments[0].click();", confirm)

    WebDriverWait(context.browser, 30).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='app']/div[4]/div[2]/div/div/div/button")))

    # Verify that transaction was successful
    assert context.browser.find_element_by_xpath("//div[@id='app']/div[4]/div[2]/div/div/div/button").text == 'Done'

    done = context.browser.find_element_by_xpath("//div[@id='app']/div[4]/div[2]/div/div/div/button")
    context.browser.execute_script("arguments[0].click();", done)


@then('user is able to buy bitcoin from wallet')
def step_impl(context):
    assert context.browser.title == "Yellow Card"
    pass



