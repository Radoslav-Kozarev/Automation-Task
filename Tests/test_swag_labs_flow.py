from playwright.sync_api import Page, expect
import pytest

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(page: Page, username: str = VALID_USERNAME, password: str = PASSWORD):
    page.goto(BASE_URL)
    page.fill("#user-name", username)
    page.fill("#password", password)
    expect(page.locator("#login-button")).to_be_visible()
    page.click("#login-button")


def test_login_with_invalid_credentials(page: Page):
    login(page, "invalid_user", "wrong_password")

    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page).to_have_url(BASE_URL)


def test_login_with_valid_credentials(page: Page):
    login(page)
    expect(page).to_have_url(f"{BASE_URL}inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_add_product_to_cart(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_be_visible()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_verify_cart_contents(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")

    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".inventory_item_desc")).to_be_visible()
    expect(page.locator(".inventory_item_price")).to_have_text("$29.99")
    expect(page.locator(".cart_quantity")).to_have_text("1")
    expect(page.locator("#continue-shopping")).to_be_visible()
    expect(page.locator("#checkout")).to_be_visible()
    expect(page.locator("#remove-sauce-labs-backpack")).to_be_visible()


def test_complete_checkout_information(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "1000")
    expect(page.locator("#cancel")).to_be_visible()
    page.click("[data-test='continue']")

    expect(page).to_have_url(f"{BASE_URL}checkout-step-two.html")
    expect(page.locator(".title")).to_have_text("Checkout: Overview")


def test_verify_checkout_overview(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "1000")
    page.click("[data-test='continue']")

    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".summary_info")).to_contain_text("Payment Information")
    expect(page.locator(".summary_info")).to_contain_text("Shipping Information")
    expect(page.locator(".summary_subtotal_label")).to_be_visible()
    expect(page.locator(".summary_tax_label")).to_be_visible()
    expect(page.locator(".summary_total_label")).to_be_visible()


def test_complete_order_successfully(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "1000")
    page.click("[data-test='continue']")
    page.click("[data-test='finish']")

    expect(page).to_have_url(f"{BASE_URL}checkout-complete.html")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")


def test_return_to_products_after_order_completion(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "1000")
    expect(page.locator("#cancel")).to_be_visible()
    page.click("[data-test='continue']")
    page.click("[data-test='finish']")
    page.click("[data-test='back-to-products']")

    expect(page).to_have_url(f"{BASE_URL}inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_continue_checkout_with_required_fields_empty(page: Page):
    login(page)
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.click("[data-test='continue']")

    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}checkout-step-one.html")


@pytest.mark.skip(reason="Known bug: Checkout with empty cart is allowed")
# Expected behavior. This test is skipped because the app allows checkout with an empty cart(bug logged).
def test_attempt_checkout_with_empty_cart(page: Page):
    login(page)
    page.click(".shopping_cart_link")
    page.click("[data-test='checkout']")
    page.fill("[data-test='firstName']", "Test")
    page.fill("[data-test='lastName']", "User")
    page.fill("[data-test='postalCode']", "1000")
    page.click("[data-test='continue']")

    expect(page).not_to_have_url(f"{BASE_URL}checkout-step-two.html")
