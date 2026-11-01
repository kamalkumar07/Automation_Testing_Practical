JobConnect Web Application Testing

Automated testing of the live JobConnect student job portal using Python, Selenium WebDriver, and Pytest.

Project Overview

This project automates functional and UI testing of the JobConnect web application. Selenium interacts with the browser, while Pytest executes test cases and verifies expected behavior.

The project includes tests for the homepage, job search, job details, login, and registration pages.

Application Under Test

JobConnect Live Website

Technologies Used

* Python — test scripting
* Selenium WebDriver — browser automation
* Pytest — test execution and assertions
* pytest-html — HTML test reporting
* Terraform — local configuration management demonstration
* CLI / Terminal — running tests and Terraform commands

Test Coverage

Module	Test Cases
Homepage	4
Job Search	4
Job Details	4
Login	3
Registration	3
Total	18

All 18 automated tests passed during the recorded test run.

Project Structure

webapp-testing/
├── tests/
│   ├── test_homepage.py
│   ├── test_job_search.py
│   ├── test_job_details.py
│   ├── test_login.py
│   └── test_register.py
├── terraform/
│   ├── main.tf
│   └── test-environment.txt
├── reports/
│   └── report.html
├── pytest.ini
├── .gitignore
└── README.md

Setup Instructions

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd webapp-testing

Replace YOUR_GITHUB_REPOSITORY_URL with your repository’s URL.

2. Create and activate a virtual environment

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install selenium pytest pytest-html

Selenium Manager can automatically manage the browser driver for supported browsers. Ensure Google Chrome is installed.

Running the Tests

Run the complete test suite:

pytest -v

Run a specific test module:

pytest tests/test_homepage.py -v

Generating the HTML Report

mkdir -p reports
pytest -v --html=reports/report.html --self-contained-html

Open the report on macOS:

open reports/report.html

Terraform Configuration

Terraform was used to demonstrate local configuration management with the Terraform Local Provider.

Commands used:

cd terraform
terraform init
terraform validate
terraform plan
terraform apply

The configuration creates a local test-environment.txt file containing project testing details.

Note: Terraform is not used to execute browser tests. Selenium and Pytest perform the actual web application testing. No AWS infrastructure is provisioned.

Test Results

* Total automated tests: 18
* Passed: 18
* Failed: 0

Disclaimer

This project performs UI and functional checks against the deployed JobConnect application. Tests avoid creating real user accounts or submitting job applications.

Author

Developed as a web application testing project using Selenium, Pytest, and Terraform.
