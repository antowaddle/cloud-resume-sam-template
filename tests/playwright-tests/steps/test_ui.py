import pytest
from pytest_bdd import scenarios, given, then
from playwright.sync_api import sync_playwright

# Load the feature file
scenarios('../features/ui_tests.feature')

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope='module')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@given("the resume page is loaded")
def load_resume_page(page):
    page.goto("https://anthony-coughlin-resume.com/")

@then('the page title should be "Anthony Coughlin - QA Manager"')
def check_page_title(page):
    assert page.title() == "Anthony Coughlin - QA Manager"
