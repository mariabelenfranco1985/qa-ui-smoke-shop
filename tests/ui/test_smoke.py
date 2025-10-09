from playwright.sync_api import sync_playwright

def test_login_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        base_url = "https://www.saucedemo.com"

        # Login
        page.goto(base_url)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        # Verificar que el ícono del carrito aparece
        assert page.locator(".shopping_cart_link").is_visible()

        # Logout
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")
        page.wait_for_selector("#login-button")

        browser.close()
