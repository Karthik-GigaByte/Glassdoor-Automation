# Glassdoor Automation Testing

## Introduction

This repository contains a suite of automated tests for the Glassdoor website, implemented using Selenium and Python. The purpose of these tests is to validate the functionality of key features on the Glassdoor website, including user login, password changes, job postings, company searches, and job searches. This project aims to ensure that these features work as expected and to catch any regressions or failures early in the development cycle.

## Technologies Used


- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Environment Management:** dotenv (.env)

## Test Cases

Below is the table of test cases covered in this Selenium automation suite:

| Test Case ID | Description          | Method                     | Status (Active/Deprecated) |
|--------------|----------------------|----------------------------|----------------------------|
| TC01         | Login functionality  | `test_login()`             | Active                     |
| TC02         | Change Password      | `test_change_password()`   | Active                     |
| TC03         | Posting a test       | `test_posting()`           | Active                     |
| TC04         | Search for companies | `test_search_company()`    | Active                     |
| TC05         | Search for jobs      | `test_search_jobs()`       | Active                     |

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Karthik-GigaByte/Glassdoor-Automation.git
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup the dotenv**:
    ```bash
     pip install dotenv
    ```
    
## Demonstration

Here are some animated GIFs showing the tests in action:

### Login Test

![Login Test GIF](path_to_your_gif/login_test.gif)

### Change Password Test

![Change Password GIF](path_to_your_gif/change_password_test.gif)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
  
