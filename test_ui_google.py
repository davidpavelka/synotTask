from playwright.sync_api import sync_playwright
from pages.google_search_page import GoogleSearchPage

def test_google_search_contains_synot_games():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        search_page = GoogleSearchPage(page)
        search_page.goto()
        search_page.search("synot games")
        assert search_page.results_present()
        assert search_page.contains_result_with_text("synot games")
        browser.close()
