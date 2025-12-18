import pytest
from playwright.sync_api import Page, expect


'''
tag id          tag#id
tag class       tag.class
tag attribute   tag[attribute=value]
tag class attribute     tag.class[attribute=value]

'''


def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag#id
    # page.locator("input#small-searchterms").fill("T-shirt")
    # page.wait_for_timeout(5000)

    #tag.class
    #page.locator("input.search-box-text").fill("Underware")
    # page.locator("search-box-text").fill("Underware")
    # page.wait_for_timeout(5000)


    #tag[attribute=value]
    # page.locator("input[name=q]").fill("Pant")
    # page.wait_for_timeout(5000)

    # tag.class[attribute=value]
    #page.locator("input.search-box-text[value='Search store']").fill("Bag")
    page.locator(".search-box-text[value='Search store']").fill("Bag")
    page.wait_for_timeout(5000)








