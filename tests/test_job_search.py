from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
JOBS_URL = (
    "https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/jobs"
)
def test_jobs_page_loads_and_shows_listings(driver):
    driver.get(JOBS_URL)
    job_links = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[contains(@href, '/jobs/')]")
        )
    )
    assert len(job_links) > 0, "No job listings are displayed"
def test_job_search_by_keyword(driver):
    driver.get(JOBS_URL)
    keyword = driver.find_element(By.NAME, "q")
    keyword.send_keys("Developer")
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Search']"
    ).click()
    WebDriverWait(driver, 15).until(
        lambda browser: browser.execute_script(
            "return document.readyState"
        ) == "complete"
    )
    assert "q=Developer" in driver.current_url or keyword.get_attribute("value") == "Developer"
def test_job_search_by_location(driver):
    driver.get(JOBS_URL)
    location = driver.find_element(By.NAME, "location")
    location.send_keys("India")
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Search']"
    ).click()
    WebDriverWait(driver, 15).until(
        lambda browser: browser.execute_script(
            "return document.readyState"
        ) == "complete"
    )
    assert (
        "location=India" in driver.current_url
        or location.get_attribute("value") == "India"
    )
def test_clear_search_filters(driver):
    driver.get(JOBS_URL)
    keyword = driver.find_element(By.NAME, "q")
    keyword.send_keys("Developer")
    location = driver.find_element(By.NAME, "location")
    location.send_keys("India")
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Search']"
    ).click()
    driver.find_element(
        By.XPATH, "//button[normalize-space()='Clear']"
    ).click()
    WebDriverWait(driver, 10).until(
        lambda browser: browser.find_element(By.NAME, "q").get_attribute("value") == ""
        and browser.find_element(By.NAME, "location").get_attribute("value") == ""
    )
    assert driver.find_element(By.NAME, "q").get_attribute("value") == ""
    assert driver.find_element(By.NAME, "location").get_attribute("value") == ""
