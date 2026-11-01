from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

JOB_DETAILS_URL = (
    "https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/jobs/8"
)


def test_job_details_page_loads(driver):
    driver.get(JOB_DETAILS_URL)

    job_title = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    assert job_title.text.strip() == "Technical Content Writer"


def test_job_details_sections_are_visible(driver):
    driver.get(JOB_DETAILS_URL)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    page_text = driver.find_element(By.TAG_NAME, "body").text

    expected_sections = [
        "Job Description",
        "Required Skills",
        "Eligibility Criteria",
        "Experience",
        "About TechNova Solutions",
    ]

    for section in expected_sections:
        assert section in page_text, f"Section not found on page: {section}"


def test_apply_now_button_is_displayed(driver):
    driver.get(JOB_DETAILS_URL)

    apply_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='Apply Now']")
        )
    )

    assert apply_button.is_displayed()
    assert apply_button.is_enabled()


def test_back_to_jobs_link(driver):
    driver.get(JOB_DETAILS_URL)

    back_link = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@href, '/jobs') and contains(., 'Back')]")
        )
    )

    assert back_link.is_displayed()
    assert back_link.get_attribute("href").endswith("/jobs")
