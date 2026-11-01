from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

REGISTER_URL = (
    "https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/register"
)


def test_register_page_loads(driver):
    driver.get(REGISTER_URL)

    field_names = [
        "name",
        "phone",
        "email",
        "password",
        "college",
        "course",
        "graduation_year",
    ]

    for field_name in field_names:
        field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.NAME, field_name))
        )
        assert field.is_displayed()


def test_student_and_recruiter_options_are_visible(driver):
    driver.get(REGISTER_URL)

    student_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(., 'Student')]")
        )
    )
    recruiter_button = driver.find_element(
        By.XPATH, "//button[contains(., 'Recruiter')]"
    )

    assert student_button.is_displayed()
    assert recruiter_button.is_displayed()


def test_register_button_is_displayed(driver):
    driver.get(REGISTER_URL)

    register_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='Register']")
        )
    )

    assert register_button.is_displayed()
    assert register_button.is_enabled()
