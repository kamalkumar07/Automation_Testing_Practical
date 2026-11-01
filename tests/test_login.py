from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = (
    "https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/login"
)


def test_login_page_loads(driver):
    driver.get(LOGIN_URL)

    email_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    password_field = driver.find_element(By.NAME, "password")

    assert email_field.is_displayed()
    assert password_field.is_displayed()


def test_login_button_is_displayed(driver):
    driver.get(LOGIN_URL)

    login_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )

    assert login_button.is_displayed()
    assert login_button.is_enabled()


def test_create_account_link_is_displayed(driver):
    driver.get(LOGIN_URL)

    register_link = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@href, '/register')]")
        )
    )

    assert register_link.is_displayed()
