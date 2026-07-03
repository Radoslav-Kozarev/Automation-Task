# Swag Labs UI Automation

UI automation project for the Swag Labs demo application using *Playwright*, 
*Python*, and *Pytest*.

## Tech Stack

- Python 3.9 or newer
- Playwright
- Pytest

## Prerequisites

Before running the tests, make sure the following are installed:

- Python *3.9 or later*
- Git

Verify your Python version:

python --version

---

## Installation

Clone the repository:

- git clone <repository-url>


Install the project dependencies:

- pip install -r requirements.txt

Install Playwright browsers:

- playwright install

If pip is not available, use:

- python -m pip install -r requirements.txt

- python -m playwright install

---

## Running the Tests

Run all tests:

- pytest

Run tests with a visible browser:

- pytest --headed

Run a specific test file:

- pytest tests/test_swag_labs_flow.py

Run a specific test:

- pytest -k test_login_with_valid_credentials

---

## Test Coverage

The automation currently covers the following scenarios:

- Login with valid credentials
- Login with invalid credentials
- Add product to cart
- Verify cart contents
- Complete checkout information
- Verify checkout overview
- Complete order successfully
- Return to Products page after successful checkout
- Checkout validation for required fields
- Attempt checkout with an empty cart