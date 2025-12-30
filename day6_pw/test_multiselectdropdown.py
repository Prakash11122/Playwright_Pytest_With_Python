import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from teh dropdown - 3 ways
    # page.locator("#colors").select_option(["Red","Blue","Green"]) # by label
    # page.locator("#colors").select_option(label=["Red", "Blue", "Green"])  # by label
    #page.locator("#colors").select_option(value=["red","white","green"])  # by values
    page.locator("#colors").select_option(index=[4,2])  # by index



    page.wait_for_timeout(5000)



