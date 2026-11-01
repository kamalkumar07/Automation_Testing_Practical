from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://job-connect-fsd-project-jha2esm1x-kamalkumar17b-3631s-projects.vercel.app/"


def test_homepage_loads(driver):
    driver.get(BASE_URL)

    WebDriverWait(driver, 20).until(
        lambda browser: browser.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    assert driver.title == "JobConnect - Student Job Portal"
    assert driver.find_element(By.TAG_NAME, "body").is_displayed()


def test_homepage_navigation_links(driver):
    driver.get(BASE_URL)

    expected_links = {
        "Home": "/",
        "Find Jobs": "/jobs",
        "About Us": "/about",
        "Login": "/login",
        "Register": "/register",
    }

    for link_text, expected_path in expected_links.items():
        links = driver.find_elements(
            By.XPATH,
            f"//a[contains(normalize-space(.), '{link_text}')]"
        )

        assert links, f"{link_text} link was not found"

        matching_link = any(
            expected_path in (link.get_attribute("href") or "")
            for link in links
        )

        assert matching_link, f"{link_text} link has an incorrect URL"


def test_homepage_job_search_fields(driver):
    driver.get(BASE_URL)

    job_title = driver.find_element(
        By.XPATH,
        "//input[@placeholder='Job title or keyword']"
    )

    location = driver.find_element(
        By.XPATH,
        "//input[@placeholder='Location']"
    )

    search_button = driver.find_element(
        By.XPATH,
        "//button[contains(normalize-space(.), 'Search Jobs')]"
    )

    assert job_title.is_displayed()
    assert location.is_displayed()
    assert search_button.is_displayed()


def test_homepage_job_details_links(driver):
    driver.get(BASE_URL)
    details_links = WebDriverWait(driver, 20).until(
        lambda browser: browser.find_elements(
            By.XPATH,
            "//a[contains(normalize-space(.), 'View Details')]"
        ) or False
    )
    assert len(details_links) > 0, "No job detail links found"
    for link in details_links:
        href = link.get_attribute("href")
        assert href and "/jobs/" in href, (
            f"Unexpected job detail URL: {href}"
        )
