from playwright.sync_api import sync_playwright

def test_open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Abre el navegador visible
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        print("✅ Prueba exitosa: el título es correcto.")
        browser.close()
