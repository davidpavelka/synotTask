class GoogleSearchPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.google.com")
        self.page.locator("[name='q']").wait_for()

    def search(self, term):
        self.page.fill("[name='q']", term)
        self.page.press("[name='q']", "Enter")
        self.page.locator("#search").wait_for()

    def results_present(self):
        return self.page.locator("#search .g").count() > 0

    def contains_result_with_text(self, text):
        return self.page.locator(f"#search .g:has-text('{text}')").count() > 0
