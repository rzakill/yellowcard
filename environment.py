import behave_webdriver
from behave_webdriver.steps import *



def before_all(context):
    context.browser = behave_webdriver.Chrome()

def after_all(context):
    # cleanup after tests run
    context.browser.quit()