# Parabank Automation Testing Framework

## Project Overview

Automation testing framework developed for Parabank banking application using Python, Selenium, Behave BDD, and Page Object Model.

## Tech Stack

- Python
- Selenium WebDriver
- Behave BDD
- Page Object Model (POM)
- OpenPyXL
- MySQL
- Requests Library
- Allure Reports

## Automated Features

- User Registration
- Login
- Negative Login
- Logout
- Forgot Password
- Open New Account
- Account Overview
- Transfer Funds
- Bill Pay
- Find Transactions
- Update Contact Info
- Request Loan

## Additional Features

- Data Driven Testing
- Screenshot Capture
- Database Testing
- API Testing
- HTML Reports
- Allure Reports

## Folder Structure

features/
pages/
utils/
testdata/
screenshots/
api_tests/

## Run Tests

behave

## Generate Allure Report

behave -f allure_behave.formatter:AllureFormatter -o allure-results

allure serve allure-results