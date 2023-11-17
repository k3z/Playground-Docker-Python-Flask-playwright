""" Master CLI commands """
import click  # noqa
from flask import Blueprint


bp = Blueprint("cli", __name__, cli_group="app")


@bp.cli.command()
def hello():
    print("world")


@bp.cli.command()
def playwright():
    import re
    from playwright.sync_api import sync_playwright
    from playwright.sync_api import expect

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://nginx/")

        # check if meta title contain "Creative"
        expect(page).to_have_title(re.compile("Creative"))
        print(page.url)
        # Open example menu by click
        page.locator("#examples-nav").click()
        # Go to contact us page
        page.locator("#contact-us").click()
        print(page.url)
