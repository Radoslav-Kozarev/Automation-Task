# Swag Labs UI Automation

UI automation project for the Swag Labs demo application using *Playwright*, 
*Python*, and *Pytest*.

## Tech Stack

- Python 3.9 or newer
- Playwright
- Pytest

- I chose Playwright with Python because Playwright is a modern automation 
testing tool that provides fast, reliable, and stable browser automation. 
I have some experience with this tech stack from previous projects. 

## Prerequisites

Before running the tests, make sure the following are installed:

- Python *3.9 or later*
- Git

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